import sys
import time

import pygame

from Players import *

pygame.init()

screen_width = 800
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Othello")

# Define fonts
font_large = pygame.font.SysFont(None, 36)
font_small = pygame.font.SysFont(None, 24)

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
gray = (200, 200, 200)
red = (255, 0, 0)
green = (0, 107, 50)
baby_green = (17, 147, 57)


def draw_text(text, font, color, x, y):
    lines = text.split('\n')
    for i, line in enumerate(lines):
        text_surface = font.render(line, True, color)
        text_rect = text_surface.get_rect(center=(x, y + i * font.get_height()))
        screen.blit(text_surface, text_rect)

pygame.mixer.init()
move_sound = pygame.mixer.Sound("move.wav")

class GameState:
    def __init__(self, player_name, player_num, level):
        self.player_name = player_name
        self.board = Board()
        self.player_num = player_num
        self.level = level
        self.choose_field = pygame.Rect(screen_width // 2 - 150, 150, 300, 40)
        self.p1 = Player(int(self.player_num), self.player_name)
        if self.player_num == "1":
            self.p2 = AIPlayer(2, "computer", self.level)
        else:
            self.p2 = AIPlayer(1, "computer", self.level)
        self.check = False
        if self.player_num == "1":
            self.is_player_turn = True
        else:
            self.is_player_turn = False
        self.selected_cell = None

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and self.is_player_turn:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if 50 <= mouse_x <= 450 and 200 <= mouse_y <= 600:
                    row = (mouse_y - 200) // 50
                    col = (mouse_x - 50) // 50
                    print("Clicked on square:", row, col)
                    if self.board.valid_move(row, col, int(self.player_num)):
                        self.selected_cell = (row, col)
                    else:
                        print("Invalid cell ..\nPlease choose a valid one ..\n")

    def draw(self):


        self.board.set_players(self.p1, self.p2)
        screen.fill(black)
        draw_text("Player: " + self.player_name, font_small, white, screen_width // 2, 60)
        draw_text("Opponent: Computer", font_small, white, screen_width // 2, 90)
        draw_text("Black: " + str(self.board.player1.available_pieces), font_small, white, screen_width // 2, 120)
        draw_text("White: " + str(self.board.player2.available_pieces), font_small, white, screen_width // 2, 150)

        for i in range(8):
            draw_text(str(i), font_small, white, 20, 210 + i * 50 + 25)

        for j in range(8):
            draw_text(str(j), font_small, white, 45 + j * 50 + 25, 180)


        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0:
                    pygame.draw.rect(screen, green, pygame.Rect(50 + j * 50, 200 + i * 50, 50, 50))
                else:
                    pygame.draw.rect(screen, baby_green, pygame.Rect(50 + j * 50, 200 + i * 50, 50, 50))

                # Draw disks
                if self.board.cells[i][j] == 1:  # Player 1's disk
                    pygame.draw.circle(screen, black, (75 + j * 50, 225 + i * 50), 20)
                elif self.board.cells[i][j] == 2:  # Player 2's disk
                    pygame.draw.circle(screen, white, (75 + j * 50, 225 + i * 50), 20)

        draw_text("Welcome to Othello!", font_large, white, screen_width // 2, 30)
        black_count = sum(row.count(1) for row in self.board.cells)
        white_count = sum(row.count(2) for row in self.board.cells)
        draw_text("Score:", font_large, white, screen_width//2+100, 200)
        draw_text("Black Score: " + str(black_count) +"       White Score: " + str(white_count) , font_small , white , screen_width//2+230, 230 )

        if self.is_player_turn:
            draw_text("Player" + str(self.player_num) + ":\nYour turn," + self.player_name +
                      "..\nYour available pieces =" + str(self.p1.available_pieces), font_small, white,
                      screen_width // 2 + 250, screen_height // 2 - 50)
            valid_moves = self.board.valid_moves(int(self.player_num))
            if len(valid_moves) == 0:
                self.p1.available_pieces -= 1
                draw_text("Sorry! No valid moves for you :(\nI have to skip your turn ..\n", font_small, white,
                          screen_width // 2 + 250, screen_height // 2)
                self.is_player_turn = False
                self.check = True
            else:
                draw_text("Your valid moves are:", font_small, white, screen_width // 2 + 250, screen_height // 2)
                move_y = screen_height // 2 + 30
                for move in valid_moves:
                    move_text = "Row: " + str(move[0]) + ", Col: " + str(move[1])
                    draw_text(move_text, font_small, white, screen_width // 2 + 250, move_y)
                    move_y += 30

        if self.selected_cell is not None:
            row, col = self.selected_cell
            self.board.update(row, col, self.p1)
            self.p1.available_pieces -= 1
            self.check = True
            self.selected_cell = None
            self.is_player_turn = False
            move_sound.play()

        if self.board.check_winner() == 1 or self.board.check_winner() == 2 or self.board.check_winner() == 0 :
            # draw_text(self.board.check_winner(), font_small, white, screen_width // 2 + 250, screen_height // 2)

            if self.board.check_winner() == 1:
                draw_text("Player 1 Is Winner", font_small, white, screen_width // 2 + 250, screen_height // 2)
                time.sleep(3)
            elif self.board.check_winner() == 2:
                draw_text("Player 2 Is Winner", font_small, white, screen_width // 2 + 250, screen_height // 2)
                time.sleep(3)
            else:
                draw_text("Wow it is Tie !", font_small, white, screen_width // 2 + 250, screen_height // 2)
            time.sleep(3)

            sys.exit()
        if not self.is_player_turn:
            self.p2.pick_move(self.board)
            self.p2.available_pieces -= 1
            self.is_player_turn = True
        pygame.display.flip()