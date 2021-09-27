import pygame

from core.Objects.Playable.Ghoost import Ghost


class Game:
    def __init__(self,  size, name, full_screen):
        pygame.init()
        if full_screen:
            self.screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption(name)
        self.delta = 1/120
        self.person = Ghost(self, "Rjkzavr", 0, 0)

    def update(self):
        self.person.update()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.on_close()
                    pygame.quit()
                    return
            self.update()
            self.screen.fill((50, 50, 150))
            self.draw()
            pygame.display.update()

    def draw(self):
        self.person.draw()

    def on_close(self):
        pass
