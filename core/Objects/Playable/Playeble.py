import pygame
import math


class Playable:
    def __init__(self, game, name, x, y, animation):
        self.game = game
        self.name = name
        self.pos = [x, y]
        self.animation = animation
        self.speed = 15
        self.speed_running = 30
        self.jump = 30
        self.pixels_per_frame = 15
        self.delta_image = 0
        self.acceleration = [0, 0]
        self.is_on_ground = True
        self.is_g = False
        self.is_on_focus_mouse = True
        self.is_on_focus_keys = True
        self.look_to = [1, 0]

    def move(self, x, y, special):
        v_x, v_y = self.acceleration

        if self.is_g:
            if not special:
                v_x = x * self.speed
            else:
                v_x = x * self.speed_running

            if y and self.is_on_ground:
                v_y = self.jump
                self.is_on_ground = False
            elif not self.is_on_ground:
                v_y -= 9.81 * self.game.delta
        else:
            if not special:
                v_x = x * self.speed
                v_y = y * self.speed
            else:
                v_x = x * self.speed_running
                v_y = y * self.speed_running
            if x and y:
                v_x *= 0.7
                v_y *= 0.7
        self.acceleration = [v_x, v_y]
        if self.acceleration[0]:
            self.look_to[0] = self.acceleration[0]
        if self.acceleration[1]:
            self.look_to[1] = self.acceleration[1]
        self.pos[0], self.pos[1] = (self.pos[0] + self.acceleration[0] * self.game.delta,
                                    self.pos[1] + self.acceleration[1] * self.game.delta)
        self.animation.step += (math.hypot(*[accel * self.game.delta for accel in self.acceleration]) / \
                                self.pixels_per_frame)

    def update(self):
        keys = pygame.key.get_pressed()
        if self.is_on_focus_keys:
            self.move(-1 if keys[pygame.K_a] else 1 if keys[pygame.K_d] else 0,
                      -1 if keys[pygame.K_s] else 1 if keys[pygame.K_w] else 0, keys[pygame.K_LSHIFT])

    def draw(self):
        if self.look_to[1] > 0 and self.animation.have_animation("moveUp"):
            self.game.screen.blit(self.animation.get("moveUp"), (self.pos[0], -self.pos[1]))
        if self.look_to[1] < 0 and self.animation.have_animation("moveDown"):
            self.game.screen.blit(self.animation.get("moveDown"), (self.pos[0], -self.pos[1]))
        if self.look_to[0] > 0 and self.animation.have_animation("moveRight"):
            self.game.screen.blit(self.animation.get("moveRight"), (self.pos[0], -self.pos[1]))
        if self.look_to[0] < 0 and self.animation.have_animation("moveLeft"):
            self.game.screen.blit(self.animation.get("moveLeft"), (self.pos[0], -self.pos[1]))

    def change_focus_keys(self):
        self.is_on_focus_keys = not self.is_on_focus_keys

    def change_focus_mouse(self):
        self.is_on_focus_mouse = not self.is_on_focus_mouse
