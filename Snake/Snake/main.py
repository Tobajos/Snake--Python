from game_objects import *
from snake import *
from ScoreBoard import *
import time
import pygame
import random
import textwrap
pygame.init()


food = Game_objects()
man = Snake()
button = Score_Board(man.snake_length)

border_size = 10
offset = 10
grid_size = 40

black = (0, 204, 255)
blue = (0, 204, 255)
white = (255, 255, 255)
green = (39, 43, 65)
frame_rect = pygame.Rect(30, 70, width - 60, height - 100)
border_color = (0, 204, 255)

clock = pygame.time.Clock()
pygame.display.set_caption("Snake")

class Menu:
    def __init__(self):
        self.message_font = pygame.font.Font('fonts/MouldyCheeseRegular-WyMWG.ttf', 50)
        self.message_font2 = pygame.font.Font('fonts/MouldyCheeseRegular-WyMWG.ttf', 20)
        self.message_font3 = pygame.font.Font('fonts/MouldyCheeseRegular-WyMWG.ttf', 25)
        self.score_font = pygame.font.Font('fonts/MouldyCheeseRegular-WyMWG.ttf', 40)
        self.score = 1
        self.logo = pygame.image.load("photos/Snake_Game2.png")
        self.button1 = pygame.image.load("buttons/start.png")
        self.button11 = pygame.image.load("buttons/start_5.png")
        self.button1_rect = self.button1.get_rect(center=(width / 2, 380))
        self.button2 = pygame.image.load("buttons/controls.png")
        self.button22 = pygame.image.load("buttons/controls_2.png")
        self.button2_rect = self.button2.get_rect(center=(width / 2, 510))
        self.button3 = pygame.image.load("buttons/score.png")
        self.button33 = pygame.image.load("buttons/score_2.png")
        self.button3_rect = self.button3.get_rect(center=(width / 2, 630))
        self.button4 = pygame.image.load("buttons/easy.png")
        self.button44 = pygame.image.load("buttons/easy_2.png")
        self.button4_rect = self.button4.get_rect(center=(width / 2, 380))
        self.button5 = pygame.image.load("buttons/normal.png")
        self.button55 = pygame.image.load("buttons/normal_2.png")
        self.button5_rect = self.button5.get_rect(center=(width / 2, 510))
        self.button6 = pygame.image.load("buttons/hard.png")
        self.button66 = pygame.image.load("buttons/hard_2.png")
        self.button6_rect = self.button6.get_rect(center=(width / 2, 630))
        self.button_back = pygame.image.load("buttons/back.png")
        self.button7 = pygame.image.load("buttons/back_2.png")
        self.button_back_rect = self.button_back.get_rect(center=(150, 900))
        self.scaled_logo = pygame.transform.scale(self.logo,(int(self.logo.get_width()/2),int(self.logo.get_height()/2)))
        self.logo_rect = self.scaled_logo.get_rect(center=(width/2, 100))
        self.apple_rules = pygame.image.load("photos/apple.png")
        self.boost_rules = pygame.image.load("photos/startup.png")
        self.bomb_rules = pygame.image.load("photos/bomb.png")
        self.apple_text = self.message_font3.render(" gives the snake 1 point ", True, blue)
        self.boost_text = self.message_font3.render(" gives the snake 3 points ", True, blue)
        self.bomb_text = self.message_font3.render("  takes 3 snake's points", True, blue)
        self.easy_text = self.message_font.render("Easy - Speed = 5 ", True, blue)
        self.normal_text = self.message_font.render("Normal - Speed = 10 ", True, blue)
        self.hard_text = self.message_font.render("Hard - Speed = 15 ", True, blue)
        self.up_text = self.message_font3.render(" -  move up ", True, blue)
        self.down_text = self.message_font3.render(" - move down ", True, blue)
        self.right_text = self.message_font3.render(" - move right ", True, blue)
        self.left_text = self.message_font3.render(" - move left ", True, blue)
        self.space_text = self.message_font3.render(" Space ", True, white)
        self.pause_text = self.message_font3.render("             - Pause ", True, blue)
        self.level_text = self.message_font.render("Chose Level", True, blue)
        self.down_rules = pygame.image.load("photos/down_rules.png")
        self.right_rules = pygame.image.load("photos/right_rules.png")
        self.up_rules = pygame.image.load("photos/up_rules.png")
        self.left_rules = pygame.image.load("photos/left_rules.png")
        self.logo3 = pygame.image.load("photos/Controls2.png")
        self.scaled_logo3 = pygame.transform.scale(self.logo3,(int(self.logo3.get_width()/2),int(self.logo3.get_height()/2)))
        self.logo_rect3 = self.scaled_logo3.get_rect(center=(width/2, 100))
        self.game_over_soound = pygame.mixer.Sound("sounds/game_over_sound.wav")
    def print_score(self,score):
        text = self.score_font.render(f"Score: {score}", True, black)
        win.blit(text, [20, 13])

    def game_level(self):
        game_level = True
        while game_level:
            win.fill(green)
            win.blit(self.scaled_logo, self.logo_rect)
            win.blit(self.button4, self.button4_rect)
            win.blit(self.button5, self.button5_rect)
            win.blit(self.button6, self.button6_rect)
            win.blit(self.button_back, self.button_back_rect)
            win.blit(self.level_text, (width / 2 - 150 , height / 2 - 250))
            button.mouse_button(self.button4_rect, self.button4, self.button44)
            button.mouse_button(self.button5_rect, self.button5, self.button55)
            button.mouse_button(self.button6_rect, self.button6, self.button66)
            button.mouse_button(self.button_back_rect, self.button_back, self.button7)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.button4_rect.collidepoint(mouse_pos):
                        return 5
                    elif self.button5_rect.collidepoint(mouse_pos):
                        return 10
                    elif self.button6_rect.collidepoint(mouse_pos):
                        return 15
                    elif self.button_back_rect.collidepoint(mouse_pos):
                        menu.game_menu()

    def rules(self):
        rules = True
        while rules:
            win.fill(green)
            x = 200
            y = 200
            row_height = 50
            col_width = 200
            pygame.draw.rect(win, black, (x + 100, y, 2 * col_width, 4 * row_height), 5)
            level_text = self.message_font2.render('Level', True, black)
            speed_text = self.message_font2.render('Snake Speed', True, black)
            win.blit(level_text, (x + col_width - level_text.get_width() // 2, y + 20))
            win.blit(speed_text, (x + 2 * col_width - speed_text.get_width() // 2, y + 20))
            win.blit(self.button_back, self.button_back_rect)
            content_font = pygame.font.Font('fonts/MouldyCheeseRegular-WyMWG.ttf', 25)
            levels = ['Easy', 'Normal', 'Hard']
            speeds = [5, 10, 15]
            for i in range(len(levels)):
                level_name = levels[i]
                snake_speed = speeds[i]
                level_text = content_font.render(level_name, True, white)
                speed_text = content_font.render(str(snake_speed), True, black)
                win.blit(level_text, (x + col_width - level_text.get_width() // 2, y + (i + 1) * row_height))
                win.blit(speed_text, (x + 2 * col_width - speed_text.get_width() // 2, y + (i + 1) * row_height))
            win.blit(self.scaled_logo3, self.logo_rect3)
            pygame.draw.rect(win, black, (300, 480, 400, 300), 5)
            self.apple_rules = pygame.transform.scale(self.apple_rules, (40, 40))
            win.blit(self.apple_rules, (310, 500))
            self.boost_rules = pygame.transform.scale(self.boost_rules, (40, 40))
            win.blit(self.boost_rules, (310, 600))
            self.bomb_rules = pygame.transform.scale(self.bomb_rules, (40, 40))
            win.blit(self.bomb_rules, (310, 700))
            win.blit(self.apple_text, (380, 513 ))
            win.blit(self.boost_text, (380, 607))
            win.blit(self.bomb_text, (380, 715))
            self.up_rules = pygame.transform.scale(self.up_rules, (50, 50))
            win.blit(self.up_rules, (900,210))
            self.down_rules = pygame.transform.scale(self.down_rules, (50, 50))
            win.blit(self.down_rules, (900, 310))
            self.right_rules = pygame.transform.scale(self.right_rules, (50, 50))
            win.blit(self.right_rules, (900,410))
            self.left_rules = pygame.transform.scale(self.left_rules, (50, 50))
            win.blit(self.left_rules, (900, 510))
            pygame.draw.rect(win, black, (890, 200, 260, 580), 5)
            win.blit(self.up_text, (950, 225))
            win.blit(self.down_text, (950, 325))
            win.blit(self.right_text, (950, 425))
            win.blit(self.left_text, (950, 525))
            win.blit(self.space_text, (900, 625))
            win.blit(self.pause_text, (900, 625))
            win.blit(self.button_back, self.button_back_rect)
            button.mouse_button(self.button_back_rect, self.button_back, self.button7)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.button_back_rect.collidepoint(mouse_pos):
                        return

    def game_menu(self):
        game_menu = True
        game_menu_obj = Menu()
        while game_menu:
            win.fill(green)
            win.blit(self.scaled_logo, self.logo_rect)
            win.blit(self.button1, self.button1_rect)
            win.blit(self.button2, self.button2_rect)
            win.blit(self.button3, self.button3_rect)
            button.mouse_button(self.button1_rect, self.button1, self.button11)
            button.mouse_button(self.button2_rect, self.button2, self.button22)
            button.mouse_button(self.button3_rect, self.button3, self.button33)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.button1_rect.collidepoint(mouse_pos):
                        return
                    elif self.button2_rect.collidepoint(mouse_pos):
                        game_menu_obj.rules()
                    elif self.button3_rect.collidepoint(mouse_pos):
                        show_record = Score_Board(man.snake_length)
                        show_record.show_records()

    def game_over(self, points):
        game_over = True
        while game_over:
            self.game_over_soound.play()
            record = Score_Board(points - 1)
            record.records()
            run_game()
            final_message = pygame.font.Font('MouldyCheeseRegular-WyMWG.ttf', 40)
            if man.snake_length <= 0:
                final_title = final_message.render("Game Over! Your Score: " + str(points), True, blue)
            else:
                final_title = final_message.render("Game Over! Your Score: "+str(points - 1), True, blue)
            win.blit(final_title, (width / 2 - final_title.get_width() / 2, 100))
            record.mouse_button(self.button_back_rect, self.button_back, self.button7)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.button_back_rect.collidepoint(mouse_pos):
                        run_game()

    def paused(self):
        pause = True
        while pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pause = False
            text = self.score_font.render(f"Pause, Click SPACE to continue", True, white)
            win.blit(text, [width / 2 - 250, height / 2 - 300])
            pygame.display.update()
            clock.tick(5)
menu = Menu()

def run_game():
    global menu, music
    game_over = False
    game_close = False
    man = Snake()
    menu.game_menu()
    man.snake_speed = menu.game_level()

    while not game_over:
        while game_close:
            menu.game_over(man.snake_length)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if not man.head_direction == 'right':
                    if event.key == pygame.K_LEFT:
                        man.head_direction = 'left'
                        man.x_speed = - man.snake_size
                        man.y_speed = 0
                if not man.head_direction == 'left':
                    if event.key == pygame.K_RIGHT:
                        man.head_direction = 'right'
                        man.x_speed = man.snake_size
                        man.y_speed = 0
                if not man.head_direction == 'down':
                    if event.key == pygame.K_UP:
                         man.head_direction = 'up'
                         man.x_speed = 0
                         man.y_speed = - man.snake_size
                if not man.head_direction == 'up':
                    if event.key == pygame.K_DOWN:
                        man.head_direction = 'down'
                        man.x_speed = 0
                        man.y_speed = man.snake_size
                if event.key == pygame.K_SPACE:
                    menu.paused()
        game_close = man.update_position()
        if game_close == False:
            win.fill(green)
            pygame.draw.rect(win, border_color, frame_rect, border_size)
            food.draw_food()
            food.new_bomb(man)
            man.snake_pixels.append([man.x, man.y])
            if len(man.snake_pixels) > man.snake_length:
                del man.snake_pixels[0]
            man.draw_snake()
            menu.print_score(man.snake_length - 1)
            game_close = food.check_objects(man)
            pygame.display.update()
            clock.tick(man.snake_speed)
    pygame.quit()
    quit()
run_game()