import threading
from threading import Thread
from pygame.image import load
import os
import pygame
import noise
import PIL.Image

seed = 5
points = []
sizeX, sizeY = 500, 500
sky_color = (77, 143, 248)


class MyThread(Thread):
    """
    A threading example
    """

    def __init__(self, name):
        """Инициализация потока"""
        Thread.__init__(self)
        self.name = name

    def run(self):
        """Запуск потока"""
        msg = "%s is running" % self.name
        print(msg)


def load_image(filename, old_img=None):
    if os.path.exists(f"{filename}.png"):
        return load(f"{filename}.png")
    return old_img


def generate_image(g=180):
    global image
    img = PIL.Image.new('RGB', (sizeX, sizeY))
    for y in range(sizeY):
        for x in range(sizeX):
            s = noise.pnoise3(float(x)*0.005, float(y)*0.005, seed, 30)
            f = int(180 + 40 * s)
            if f > g:
                f2 = (255 + 140 * s)
                if f2 > 220:
                    f2 = 220
                color = (int((f2 + sky_color[0]) / 2 * s), int((f2 + sky_color[1]) / 2 * s), int((f2 + sky_color[2]) / 2 * s))
                # color = (225, 225, 225)
                img.putpixel((x, y), color)
            else:
                img.putpixel((x, y), sky_color)
    img.save("perlin_test.png")
    print("new_frame", g)
    image = load_image("perlin_test")


k = 160
generate_image(k)
pygame.init()
pygame.mixer.init()  # для звука
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
k +=1
x = 0
running = True
image = load_image("perlin_test")
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            t1 = threading.Thread(target=generate_image, args=(k,))
            t1.start()
            # t1.join()
            k += 1
    x += 1
    if x > 520:
        x -= 520
    screen.blit(image, (0, 0))
    pygame.draw.circle(screen, (255, 0, 255), (x, 10), 5)
    pygame.display.flip()