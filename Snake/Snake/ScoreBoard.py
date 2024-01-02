from snake import *

import pygame
import json
import re



class Score_Board():
    def __init__(self, snake_length):
        super().__init__()
        pygame.init()
        self.snake_length = snake_length
        self.message_font = pygame.font.Font('fonts/MouldyCheeseRegular-WyMWG.ttf', 50,)
        self.title_font = pygame.font.Font('fonts/MouldyCheeseRegular-WyMWG.ttf', 20)
        self.points_font = pygame.font.Font('fonts/MouldyCheeseRegular-WyMWG.ttf', 50)
        self.button_back = pygame.image.load("buttons/back.png")
        self.button_back_rect = self.button_back.get_rect(center=(150, 900))
        self.button7 = pygame.image.load("buttons/back_2.png")
        self.logo2 = pygame.image.load("photos/leader3.png")
        self.scaled_logo = pygame.transform.scale(self.logo2,
                                                  (int(self.logo2.get_width()), int(self.logo2.get_height())))

        self.logo_rect = self.scaled_logo.get_rect(center=(width / 2 + 50, 80))
        self.logo_rect2 = self.scaled_logo.get_rect(center=(width / 2, 150))

    def read_list(self):
        try:
            with open('wyniki.json', 'r') as file:
                json_data = file.read()
                return json.loads(json_data)
        except FileNotFoundError:
            return []

    def save_list(self, players_list):
        json_data = json.dumps(players_list, indent=4, sort_keys=False)
        with open('wyniki.json', 'w') as file:
            file.write(json_data)


    def add_record(self,player_name):
        players_list = self.read_list()
        new_player = {
            'player_name': player_name,
            'points': self.snake_length
        }
        players_list.append(new_player)
        self.save_list(players_list)

    def show_points(self):
        your_points = self.points_font.render("Game Over! Your Score: " + str(self.snake_length), True, white)
        win.blit(your_points, (width / 2 - 255, 200))

    def draw_table(self, players_list,):
        sorted_list = sorted(players_list, key=lambda x: x.get('points', 0), reverse=True)
        best_players = sorted_list[:10]
        x = width / 2 - 220
        y = 280
        row_height = 50
        col_width = 250

        pygame.draw.rect(win, black, (x  - 20, y, 3 *col_width - 200, (len(best_players) + 1) * row_height), 5)

        nick_text = self.title_font.render('Nickname', True, black)
        points_text = self.title_font.render('Points', True, black)
        win.blit(points_text, (x + col_width  + 180, y + 20))
        win.blit(nick_text, (x + col_width - 70, y + 20))
        win.blit(self.button_back, self.button_back_rect)


        content_font = pygame.font.Font('fonts/MouldyCheeseRegular-WyMWG.ttf', 25)
        for i, player in enumerate(best_players):
            lp = i + 1
            name = player.get('player_name', '')
            points = player.get('points', 0)
            lp_text = content_font.render(str(lp), True, black)
            name_text = content_font.render(name, True, white)
            points_text = content_font.render(str(points), True, black)
            win.blit(lp_text, (x + 30, y + (i + 1) * row_height))
            win.blit(name_text, (x + col_width - 70, y + (i + 1) * row_height))
            win.blit(points_text, (x + 2 * col_width - 50, y + (i + 1) * row_height))

    def show_records(self):
        clock = pygame.time.Clock()
        zatrzymanie = False
        while not zatrzymanie:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    zatrzymanie = True
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.button_back_rect.collidepoint(mouse_pos):
                        return
            win.fill(green)

            win.blit(self.scaled_logo, self.logo_rect2)
            players_list = self.read_list()
            self.draw_table(players_list)
            self.mouse_button(self.button_back_rect, self.button_back, self.button7)
            pygame.display.update()
            clock.tick(60)
        pygame.quit()

    def mouse_button(self, rect, old_button, new_button):
        mouse_pos_x , mouse_pos_y = pygame.mouse.get_pos()
        if rect[0] < mouse_pos_x < rect[0] + rect[2] and rect[1] < mouse_pos_y < rect[1] + rect[3]:
            button = new_button
            win.blit(button, rect)
        else:
            button = old_button
            win.blit(button, rect)

    def records(self):
        player_name = ""
        clock = pygame.time.Clock()
        zatrzymanie = False
        wprowadzanie_nicku = True

        while not zatrzymanie:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    zatrzymanie = True
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.button_back_rect.collidepoint(mouse_pos):
                        return

                elif event.type == pygame.KEYDOWN:
                    if wprowadzanie_nicku:
                        if event.key == pygame.K_RETURN:
                            if player_name != "":
                                if re.match(r'^.{1,9}$', player_name) is not None:
                                    self.add_record(player_name)
                                    player_name = ""
                                    wprowadzanie_nicku = False
                        elif event.key == pygame.K_BACKSPACE:
                            player_name = player_name[:-1]
                        else:
                            if len(player_name) < 9 and re.match(r'^[a-zA-Z0-9]$', event.unicode):
                                player_name += event.unicode

            win.fill(green)
            win.blit(self.scaled_logo, self.logo_rect)
            self.show_points()
            players_list = self.read_list()
            self.draw_table(players_list)
            wpisz_nazwe = self.message_font.render("Your Nickname:", True, black)
            pole_tekstowe = self.message_font.render(player_name, True, black)
            win.blit(wpisz_nazwe, (width / 2 - 250, height / 2 + 390))
            win.blit(pole_tekstowe, (width / 2 + 150, height / 2 + 390))
            pygame.draw.rect(win, (black), (width / 2 + 145, height / 2 + 380, 400, 60), width=2)
            self.mouse_button(self.button_back_rect, self.button_back, self.button7)
            pygame.display.update()
            clock.tick(60)


        pygame.quit()