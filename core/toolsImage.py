from pygame.image import load
from pygame import Rect
import pygame
import os
pygame.display.init()


def load_image(filename):
    # print(f"{os.getcwd()}{os.altsep}source{os.altsep}image{os.altsep}{filename}.png")
    a = pygame.transform.scale2x(load(f"source{os.altsep}image{os.altsep}{filename}.png"))
    return a.convert(a)


class TileSet:
    def __init__(self, img, tile_size):
        if type(img) != str:
            self.tile_set = img
        else:
            self.tile_set = load_image(img)
        self.tile_size = tile_size
        self.count_x = int(self.tile_set.get_width() / tile_size[0])
        self.count_y = int(self.tile_set.get_height() / tile_size[1])

    def get_width(self):
        return self.tile_set.get_width()

    def get_height(self):
        return self.tile_set.get_height()

    def get(self, x, y):
        return self.tile_set.subsurface(Rect(x * self.tile_size[0], y * self.tile_size[0], *self.tile_size))


class AnimationDefault:
    def __init__(self, tile_set, **animations):
        self.tile_set = tile_set
        self.step = 0
        self.animations = animations

    def have_animation(self, name):
        return name in self.animations

    def update(self, step):
        self.step = step

    def get(self, name):
        if self.have_animation(name):
            return self.tile_set.get(*self.animations[name][int(self.step % len(self.animations[name]))])
        print(f"Error: Does not have animation '{name}'!")
