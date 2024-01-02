import random
import pygame
from snake import *


class Game_objects(Snake):

    def __init__(self):
        super().__init__()
        self.food_x = round(random.randrange(self.snake_size + 30, width - self.snake_size - 30) / self.snake_size) * self.snake_size
        self.food_y = round(random.randrange(self.snake_size + 60, height - self.snake_size - 60) / self.snake_size) * self.snake_size

        self.boost_x = round(random.randrange(self.snake_size + 30, width - self.snake_size - 30) / self.snake_size) * self.snake_size
        self.boost_y = round(random.randrange(self.snake_size + 60, height - self.snake_size - 60) / self.snake_size) * self.snake_size

        self.bomb_x = round(random.randrange(self.snake_size + 30, width - self.snake_size - 30) / self.snake_size) * self.snake_size
        self.bomb_y = round(random.randrange(self.snake_size + 60, height - self.snake_size - 60) / self.snake_size) * self.snake_size

        self.apple_img = pygame.image.load("photos/apple.png")
        self.boost_img = pygame.image.load("photos/startup.png")
        self.bomb_img = pygame.image.load("photos/bomb.png")

        self.sound = pygame.mixer.Sound("sounds/sound.wav")
        self.bomb_sound = pygame.mixer.Sound("sounds/bomb_sound.wav")
        self.power_sound = pygame.mixer.Sound("sounds/power.wav")


    def draw_food(self):
        self.apple_img = pygame.transform.scale(self.apple_img,(self.snake_size, self.snake_size))
        win.blit(self.apple_img, (self.food_x, self.food_y))

        self.boost_img = pygame.transform.scale(self.boost_img, (self.snake_size, self.snake_size))
        win.blit(self.boost_img, (self.boost_x, self.boost_y))

        self.bomb_img = pygame.transform.scale(self.bomb_img,(self.snake_size,self.snake_size))
        win.blit(self.bomb_img, (self.bomb_x, self.bomb_y))

    def check_objects(self, man):

        if self.bomb_x == 720 and self.bomb_y == 520:
            self.bomb_x = self.random_position_generator_x()
            self.bomb_y = self.random_position_generator_y()

        if self.boost_x == self.bomb_x and self.boost_y == self.bomb_y:
            self.boost_x = self.random_position_generator_x()
            self.boost_y = self.random_position_generator_y()

        if self.food_x == self.bomb_x and self.food_y == self.bomb_y:
            self.food_x = self.random_position_generator_x()
            self.food_y = self.random_position_generator_y()

        if self.food_x == self.boost_x and self.food_y == self.boost_y:
            self.food_x = self.random_position_generator_x()
            self.food_y = self.random_position_generator_y()

        if man.x == self.food_x and man.y == self.food_y:
            self.food_x = self.random_position_generator_x()
            self.food_y = self.random_position_generator_y()
            man.snake_length += 1
            self.sound.play()

        for o in man.snake_pixels:
            if self.food_x == int(o[0]) and self.food_y == int(o[1]):
                self.food_x = self.random_position_generator_x()
                self.food_y = self.random_position_generator_y()

        if man.x == self.boost_x and man.y == self.boost_y:
            self.boost_x = self.random_position_generator_x()
            self.boost_y = self.random_position_generator_y()
            man.snake_length += 3
            self.power_sound.play()
        for o in man.snake_pixels:
            if self.boost_x == int(o[0]) and self.boost_y == int(o[1]):
                self.boost_x = self.random_position_generator_x()
                self.boost_y = self.random_position_generator_y()

        if man.x == self.bomb_x and man.y == self.bomb_y:
            if man.snake_length <= 3:
                return True
            self.bomb_x = self.random_position_generator_x()
            self.bomb_y = self.random_position_generator_y()
            man.snake_pixels.pop(0)
            man.snake_pixels.pop(0)
            man.snake_pixels.pop(0)
            man.snake_length -= 3
            self.bomb_sound.play()
            for o in man.snake_pixels:
                if self.bomb_x == int(o[0]) and self.bomb_y == int(o[1]):
                    self.bomb_x = self.random_position_generator_x()
                    self.bomb_y = self.random_position_generator_y()
            if man.snake_length <= 0:
                return True

    def new_bomb(self, man):
        if man.x == self.food_x and man.y == self.food_y and not man.snake_length % 3:
            self.bomb_x = self.random_position_generator_x()
            self.bomb_y = self.random_position_generator_y()
        if man.x == self.boost_x and man.y == self.boost_y and not man.snake_length % 5:
            self.bomb_x = self.random_position_generator_x()
            self.bomb_y = self.random_position_generator_y()
        for o in man.snake_pixels:
            if self.bomb_x == int(o[0]) and self.bomb_y == int(o[1]):
                self.bomb_x = self.random_position_generator_x()
                self.bomb_y = self.random_position_generator_y()

    def random_position_generator_x(self):
        position_x = round(random.randrange(self.snake_size + 30, width - self.snake_size - 30) / self.snake_size) * self.snake_size
        return position_x

    def random_position_generator_y(self):
        position_y = round(random.randrange(self.snake_size + 60, height - self.snake_size - 60) / self.snake_size) * self.snake_size
        return position_y




