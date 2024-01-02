import random
import time

import pygame

black = (0, 204, 255)
green = (39, 43, 65)
width = 1440
height = 960
white = (255, 255, 255)
win = pygame.display.set_mode((width, height))

LEFT_IMG_PATH = "photos/left.png"
RIGHT_IMG_PATH = "photos/right.png"
UP_IMG_PATH = "photos/up.png"
DOWN_IMG_PATH = "photos/down.png"


class Snake(object):
    global  win, blue

    def __init__(self):
        self.snake_speed = 15
        self.snake_size = 40
        self.x = width / 2
        self.y = height / 2
        self.x_speed = 0
        self.y_speed = 0
        self.snake_pixels = []
        self.snake_length = 1
        self.head_imgs = {
            'left': pygame.image.load(LEFT_IMG_PATH),
            'right': pygame.image.load(RIGHT_IMG_PATH),
            'up': pygame.image.load(UP_IMG_PATH),
            'down': pygame.image.load(DOWN_IMG_PATH)
        }
        self.snake_img = pygame.image.load("photos/body_4.png")
        self.snake_img2 = pygame.image.load("photos/body_3.png")
        self.snake_img2 = pygame.transform.scale(self.snake_img2, (self.snake_size, self.snake_size))
        self.corner = pygame.image.load("photos/corner2.png")
        self.corner_2 = pygame.image.load("photos/corner_22.png")
        self.corner_3 = pygame.image.load("photos/corner_32.png")
        self.corner_4 = pygame.image.load("photos/corner_42.png")

        self.tail_up = pygame.image.load("photos/tail_up_2.png")
        self.tail_up_img = pygame.transform.scale(self.tail_up, (self.snake_size, self.snake_size))
        self.tail_down = pygame.image.load("photos/tail_down_2.png")
        self.tail_down_img = pygame.transform.scale(self.tail_down, (self.snake_size, self.snake_size))
        self.tail_left = pygame.image.load("photos/tail_left_2.png")
        self.tail_left_img = pygame.transform.scale(self.tail_left, (self.snake_size, self.snake_size))
        self.tail_right = pygame.image.load("photos/tail_right_2.png")
        self.tail_right_img = pygame.transform.scale(self.tail_right, (self.snake_size, self.snake_size))

        self.head_direction = random.choice(list(self.head_imgs.keys()))
        self.snake_img = pygame.transform.scale(self.snake_img, (self.snake_size, self.snake_size))
        self.corner_img = pygame.transform.scale(self.corner, (self.snake_size, self.snake_size))
        self.corner_img_2 = pygame.transform.scale(self.corner_2, (self.snake_size, self.snake_size))
        self.corner_img_3 = pygame.transform.scale(self.corner_3, (self.snake_size, self.snake_size))
        self.corner_img_4 = pygame.transform.scale(self.corner_4, (self.snake_size, self.snake_size))
        self.snake_img5 = pygame.image.load("photos/snake_5.png")
        self.snake_img5 = pygame.transform.scale(self.snake_img5, (self.snake_size, self.snake_size))


    def draw_tail(self):
        if len(self.snake_pixels) > 1:
            tail = self.snake_pixels[0]
            tail_2 = self.snake_pixels[1]
            if tail[0] < tail_2[0] and tail[1] == tail_2[1]:
                win.blit(self.tail_left_img, [tail[0], tail[1]])
            elif tail[0] > tail_2[0] and tail[1] == tail_2[1]:
                win.blit(self.tail_right_img, [tail[0], tail[1]])
            elif tail[0] == tail_2[0] and tail[1] > tail_2[1]:
                win.blit(self.tail_down_img, [tail[0], tail[1]])
            elif tail[0] == tail_2[0] and tail[1] < tail_2[1]:
                win.blit(self.tail_up_img, [tail[0], tail[1]])

    def draw_body(self):
        for pixel in self.body_pixels:
            for i in range(len(self.snake_pixels)):
                if (i + 2) == len(self.snake_pixels):
                    break
                previous = self.snake_pixels[i]
                mid = self.snake_pixels[i + 1]
                next = self.snake_pixels[i + 2]
                if previous[0] == next[0]:
                    win.blit(self.snake_img2, [mid[0], mid[1]])
                elif previous[1] == next[1]:
                    win.blit(self.snake_img, [mid[0], mid[1]])
                if previous[0] < next[0] and previous[1] > next[1] and mid[1] == next[1] or\
                        previous[0] > next[0] and previous[1] < next[1] and mid[0] == next[0]:
                    win.blit(self.corner_img, [mid[0], mid[1]])
                elif previous[0] > next[0] and previous[1] < next[1] and mid[1] == next[1] or\
                        previous[0] < next[0] and previous[1] > next[1] and mid[0] == next[0]:
                    win.blit(self.corner_img_3, [mid[0], mid[1]])
                elif previous[0] < next[0] and previous[1] < next[1] and mid[1] == next[1] or\
                        previous[0] > next[0] and previous[1] > next[1] and mid[0] == next[0]:
                    win.blit(self.corner_img_4, [mid[0], mid[1]])
                elif previous[0] < next[0] and previous[1] < next[1] and mid[0] == next[0] or\
                        previous[0] > next[0] and previous[1] > next[1] and mid[1] == next[1]:
                    win.blit(self.corner_img_2, [mid[0], mid[1]])

    def draw_snake(self):
        self.draw_tail()
        if self.snake_pixels:
            self.head_pixels = [self.snake_pixels[-1]]
            self.body_pixels = self.snake_pixels[:-1]
            for pixel in self.head_pixels:
                self.head_img = self.head_imgs[self.head_direction]
                self.head_img = pygame.transform.scale(self.head_img, (self.snake_size, self.snake_size))
                win.blit(self.head_img,(pixel[0], pixel[1]))
            self.draw_body()

    def update_position(self):
        self.x += self.x_speed
        self.y += self.y_speed
        if self.x >= width - 79 or self.x < 30 or self.y >= height - 60 or self.y < 70:
            return True
        for pixel in self.snake_pixels[:-1]:
            if pixel == [self.x, self.y]:
                return True
        return False






