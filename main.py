# import math
#
#
# class Board:
#     def __init__(self):
#         self.player2 = None
#         self.player1 = None
#         self.cells = [
#             [0, 0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 2, 1, 0, 0, 0],
#             [0, 0, 0, 1, 2, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 0]
#         ]
#
#     def set_players(self, p1, p2):
#         self.player1 = p1
#         self.player2 = p2
#
#     def update(self, a, b, p):
#         self.cells[a][b] = p.num
#         for i in range(b - 1):
#             if self.cells[a][i] == p.num:
#                 for j in range(i, b):
#                     if self.cells[a][j] != 0:
#                         self.cells[a][j] = p.num
#         for i in range(b + 2, 8):
#             if self.cells[a][i] == p.num:
#                 for j in range(b, i):
#                     if self.cells[a][j] != 0:
#                         self.cells[a][j] = p.num
#         for i in range(a - 1):
#             if self.cells[i][b] == p.num:
#                 for j in range(i, a):
#                     if self.cells[j][b] != 0:
#                         self.cells[j][b] = p.num
#         for i in range(a + 2, 8):
#             if self.cells[i][b] == p.num:
#                 for j in range(a, i):
#                     if self.cells[j][b] != 0:
#                         self.cells[j][b] = p.num
#
#     def instruction_display(self):
#         print("\nPlease, follow the instructions ..")
#         print("Each player has 25 pieces only. If they run out, the game ends.\n")
#         print("Choose cell from the board and enter its indices as shown in the following board ..\n")
#         for i in range(len(self.cells)):
#             print("-----------------------------------------------------------------")
#             print("| ", end='')
#             for j in range(len(self.cells[i])):
#                 print("(", i, ",", j, ") | ", end='', sep='')
#             print()
#         print("-----------------------------------------------------------------")
#
#     def display(self):
#         p1 = 0
#         p2 = 0
#         print("\n\n")
#         for row in self.cells:
#             print("-------------------------------------------------")
#             print("| ", end='')
#             for cell in row:
#                 if cell == 0:
#                     print("   ", end='')
#                 if cell == 1:
#                     print(" B ", end='')
#                     p1 += 1
#                 if cell == 2:
#                     print(" W ", end='')
#                     p2 += 1
#                 print(" | ", end='')
#             print()
#         print("-------------------------------------------------")
#         print("Black =", p1, "\nWhite =", p2, "\n")
#
#     def is_full(self):
#         for row in self.cells:
#             for cell in row:
#                 if cell == 0:
#                     return False
#         return True
#
#     def winner(self):
#         p1 = 0
#         p2 = 0
#         for row in self.cells:
#             for cell in row:
#                 if cell == 1:
#                     p1 += 1
#                 elif cell == 2:
#                     p2 += 1
#         if p1 > p2:
#             return 1
#         elif p2 > p1:
#             return 2
#         return 0
#
#     def check_winner(self):
#         if self.player1.available_pieces == 0 or self.player2.available_pieces == 0 or self.is_full():
#             if self.player1.available_pieces == 0:
#                 print("Your pieces have been run out,", self.player1.name, "!")
#             elif self.player2.available_pieces == 0:
#                 print("Your pieces have been run out,", self.player2.name, "!")
#             if self.winner() == self.player1.num:
#                 print("\nCongratulations", self.player1.name, "( Player", self.player1.num, ") you won!\n")
#                 print("Hard luck", self.player2.name, "( Player", self.player2.num, ") ..\n")
#             elif self.winner() == self.player2.num:
#                 print("\nCongratulations", self.player2.name, "( Player", self.player2.num, ") you won!\n")
#                 print("Hard luck", self.player1.name, "( Player", self.player1.num, ") ..\n")
#             else:
#                 print("\nWow! It is tie ..\n")
#             return True
#         return False
#
#     def valid_move(self, a, b, p_num):
#         if 0 <= b < 8 and 8 > a >= 0 == self.cells[a][b]:
#             if b < 7 and self.cells[a][b + 1] != p_num and self.cells[a][b + 1] != 0:
#                 for i in range(b + 2, 8):
#                     if self.cells[a][i] == 0:
#                         break
#                     if self.cells[a][i] == p_num:
#                         return True
#             if b > 0 and self.cells[a][b - 1] != p_num and self.cells[a][b - 1] != 0:
#                 for i in range(b - 1, 0, -1):
#                     if self.cells[a][i] == 0:
#                         break
#                     if self.cells[a][i] == p_num:
#                         return True
#             if a < 7 and self.cells[a + 1][b] != p_num and self.cells[a + 1][b] != 0:
#                 for i in range(a + 2, 8):
#                     if self.cells[i][b] == 0:
#                         break
#                     if self.cells[i][b] == p_num:
#                         return True
#             if a > 0 and self.cells[a - 1][b] != p_num and self.cells[a - 1][b] != 0:
#                 for i in range(a - 1, 0, -1):
#                     if self.cells[i][b] == 0:
#                         break
#                     if self.cells[i][b] == p_num:
#                         return True
#         return False
#
#     def valid_moves(self, p_num):
#         valid = []
#         for i in range(8):
#             for j in range(8):
#                 if self.valid_move(i, j, p_num):
#                     valid.append((i, j))
#         return valid
#
#     def utility(self):
#         black_count = sum(row.count(1) for row in self.cells)
#         white_count = sum(row.count(2) for row in self.cells)
#
#         if black_count > white_count:
#             return 1
#         elif white_count > black_count:
#             return -1
#         else:
#             return 0
#
#
# class Player:
#     def __init__(self, x, n):
#         self.num = x
#         self.name = n
#         self.available_pieces = 30
#
#
# class AIPlayer(Player):
#
#     def __init__(self, x, n, depth):
#         super().__init__(x, n)
#         self.depth = depth
#
#     def pick_move(self, board):
#         move = self.alpha_beta(board, self.depth, self.num, -math.inf, math.inf)
#         if move is not None:
#             if move[1] is not None:  # Check if the move is not None
#                 board.update(move[1][0], move[1][1], self)
#             else:
#                 print("No valid moves available. Skipping turn.")
#                 self.available_pieces -= 1
#         else:
#             print("No valid moves available. Skipping turn.")
#             self.available_pieces -= 1
#
#     def alpha_beta(self, board, depth, player, alpha, beta):
#         if depth == 0 or board.is_full():
#             return board.utility(), None
#
#         valid_moves = board.valid_moves(player)
#         if not valid_moves:
#             if board.valid_moves(3 - player):
#                 return self.alpha_beta(board, depth - 1, 3 - player, alpha, beta)[0], None
#             else:
#                 return board.utility(), None
#
#         if player == self.num:
#             max_val = -math.inf
#             best_move = None
#             for move in valid_moves:
#                 new_board = self.simulate_move(board, move, player)
#                 val = self.alpha_beta(new_board, depth - 1, 3 - player, alpha, beta)[0]
#                 if val > max_val:
#                     max_val = val
#                     best_move = move
#                 alpha = max(alpha, val)
#                 if alpha >= beta:
#                     break
#             return max_val, best_move
#         else:
#             min_val = math.inf
#             best_move = None
#             for move in valid_moves:
#                 new_board = self.simulate_move(board, move, player)
#                 val = self.alpha_beta(new_board, depth - 1, 3 - player, alpha, beta)[0]
#                 if val < min_val:
#                     min_val = val
#                     best_move = move
#                 beta = min(beta, val)
#                 if alpha >= beta:
#                     break
#             return min_val, best_move
#
#     def simulate_move(self, board, move, player):
#         new_board = Board()
#         new_board.cells = [row[:] for row in board.cells]
#         new_board.update(move[0], move[1], self)
#         return new_board
#
#
# class Game:
#     def run(self):
#         print("\nWelcome to Othello Game !!\n")
#         Quit = False
#         while not Quit:
#             print("Please choose :\n")
#             print("     (1) Play with computer.")
#             print("     (2) Quit the game.\n")
#             main_choice = int(input("Enter your choice : "))
#
#             if main_choice == 1:
#                 print("\nPlayer 1 starts (Black) ..\n")
#                 choice = int(input("Do you want to be player 1 or 2 ? "))
#                 name = input("Enter your name : ")
#                 player = Player(choice, name)
#                 hardLevel = int(input("\n(1) Easy .\n(2) Medium .\n(3) Hard.\n  "))
#                 if (hardLevel < 4):
#                     if choice == 1:
#                         AI_player = AIPlayer(2, "Computer", hardLevel + 3)  # Computer
#                     else:
#                         AI_player = AIPlayer(1, "Computer", hardLevel + 3)  # Computer
#
#                 board = Board()
#                 board.instruction_display()
#                 board.set_players(player, AI_player)
#                 board.display()
#
#                 while True:
#                     valid_move = False
#                     while not valid_move:
#                         print("Player", player.num, ":\nYour turn,", player.name, "..\nYour available pieces =",
#                               player.available_pieces, "\n")
#                         valid_moves = board.valid_moves(player.num)
#                         if len(valid_moves) == 0:
#                             player.available_pieces -=1
#                             print("Sorry! No valid moves for you :(")
#                             print("I have to skip your turn ..\n")
#                             break
#                         else:
#                             print("Your valid choices are :")
#                             for move in valid_moves:
#                                 print("     ", move)
#                             x = int(input("\nEnter first index (row) : "))
#                             y = int(input("Enter second index (column) : "))
#
#                             if board.valid_move(x, y, player.num):
#                                 board.update(x, y, player)
#                                 player.available_pieces -= 1
#                                 valid_move = True
#                             else:
#                                 print("Invalid cell ..\nPlease choose a valid one ..\n")
#
#                     board.display()
#                     if board.check_winner():
#                         break
#
#                     AI_player.pick_move(board)
#                     board.display()
#                     if board.check_winner():
#                         break
#
#             elif main_choice == 2:
#                 print("\nThank you for playing our Othello Game !!!")
#                 print("We hope you enjoyed and this is not the last time to play it .. Bye.")
#                 Quit = True
#
#             else:
#                 print("\nInvalid choice :(\nTry again ..\n")
#
#
# if __name__ == "__main__":
#     game = Game()
#     game.run()





import math
import pygame
import sys


class Board:
    def __init__(self):
        self.player2 = None
        self.player1 = None
        self.cells = [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 2, 1, 0, 0, 0],
            [0, 0, 0, 1, 2, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ]

    def set_players(self, p1, p2):
        self.player1 = p1
        self.player2 = p2

    def update(self, a, b, p):
        self.cells[a][b] = p.num
        for i in range(b - 1):
            if self.cells[a][i] == p.num:
                for j in range(i, b):
                    if self.cells[a][j] != 0:
                        self.cells[a][j] = p.num
        for i in range(b + 2, 8):
            if self.cells[a][i] == p.num:
                for j in range(b, i):
                    if self.cells[a][j] != 0:
                        self.cells[a][j] = p.num
        for i in range(a - 1):
            if self.cells[i][b] == p.num:
                for j in range(i, a):
                    if self.cells[j][b] != 0:
                        self.cells[j][b] = p.num
        for i in range(a + 2, 8):
            if self.cells[i][b] == p.num:
                for j in range(a, i):
                    if self.cells[j][b] != 0:
                        self.cells[j][b] = p.num

    def display(self):
            p1 = 0
            p2 = 0
            print("\n\n")
            for row in self.cells:
                print("-------------------------------------------------")
                print("| ", end='')
                for cell in row:
                    if cell == 0:
                        print("   ", end='')
                    if cell == 1:
                        print(" B ", end='')
                        p1 += 1
                    if cell == 2:
                        print(" W ", end='')
                        p2 += 1
                    print(" | ", end='')
                print()
            print("-------------------------------------------------")
            print("Black =", p1, "\nWhite =", p2, "\n")

    def is_full(self):
        for row in self.cells:
            for cell in row:
                if cell == 0:
                    return False
        return True

    def winner(self):
        p1 = 0
        p2 = 0
        for row in self.cells:
            for cell in row:
                if cell == 1:
                    p1 += 1
                elif cell == 2:
                    p2 += 1
        if p1 > p2:
            return 1
        elif p2 > p1:
            return 2
        return 0

    def check_winner(self):
        if self.player1.available_pieces == 0 or self.player2.available_pieces == 0 or self.is_full():
            if self.player1.available_pieces == 0:
                print("Your pieces have been run out,", self.player1.name, "!")
            elif self.player2.available_pieces == 0:
                print("Your pieces have been run out,", self.player2.name, "!")
            if self.winner() == self.player1.num:
                print("\nCongratulations", self.player1.name, "( Player", self.player1.num, ") you won!\n")
                print("Hard luck", self.player2.name, "( Player", self.player2.num, ") ..\n")
            elif self.winner() == self.player2.num:
                print("\nCongratulations", self.player2.name, "( Player", self.player2.num, ") you won!\n")
                print("Hard luck", self.player1.name, "( Player", self.player1.num, ") ..\n")
            else:
                print("\nWow! It is tie ..\n")
            return True
        return False

    def valid_move(self, a, b, p_num):
        if 0 <= b < 8 and 8 > a >= 0 == self.cells[a][b]:
            if b < 7 and self.cells[a][b + 1] != p_num and self.cells[a][b + 1] != 0:
                for i in range(b + 2, 8):
                    if self.cells[a][i] == 0:
                        break
                    if self.cells[a][i] == p_num:
                        return True
            if b > 0 and self.cells[a][b - 1] != p_num and self.cells[a][b - 1] != 0:
                for i in range(b - 1, 0, -1):
                    if self.cells[a][i] == 0:
                        break
                    if self.cells[a][i] == p_num:
                        return True
            if a < 7 and self.cells[a + 1][b] != p_num and self.cells[a + 1][b] != 0:
                for i in range(a + 2, 8):
                    if self.cells[i][b] == 0:
                        break
                    if self.cells[i][b] == p_num:
                        return True
            if a > 0 and self.cells[a - 1][b] != p_num and self.cells[a - 1][b] != 0:
                for i in range(a - 1, 0, -1):
                    if self.cells[i][b] == 0:
                        break
                    if self.cells[i][b] == p_num:
                        return True
        return False

    def valid_moves(self, p_num):
        valid = []
        for i in range(8):
            for j in range(8):
                if self.valid_move(i, j, p_num):
                    valid.append((i, j))
        return valid

    def utility(self):
        black_count = sum(row.count(1) for row in self.cells)
        white_count = sum(row.count(2) for row in self.cells)

        if black_count > white_count:
            return 1
        elif white_count > black_count:
            return -1
        else:
            return 0




class Player:
    def __init__(self, x, n):
        self.num = x
        self.name = n
        self.available_pieces = 30


class AIPlayer(Player):

    def __init__(self, x, n, depth):
        super().__init__(x, n)
        self.depth = depth

    def pick_move(self, board):
        move = self.alpha_beta(board, self.depth, self.num, -math.inf, math.inf)
        if move is not None:
            if move[1] is not None:  # Check if the move is not None
                board.update(move[1][0], move[1][1], self)
            else:
                print("No valid moves available. Skipping turn.")
                self.available_pieces -= 1
        else:
            print("No valid moves available. Skipping turn.")
            self.available_pieces -= 1

    def alpha_beta(self, board, depth, player, alpha, beta):
        if depth == 0 or board.is_full():
            return board.utility(), None

        valid_moves = board.valid_moves(player)
        if not valid_moves:
            if board.valid_moves(3 - player):
                return self.alpha_beta(board, depth - 1, 3 - player, alpha, beta)[0], None
            else:
                return board.utility(), None

        if player == self.num:
            max_val = -math.inf
            best_move = None
            for move in valid_moves:
                new_board = self.simulate_move(board, move, player)
                val = self.alpha_beta(new_board, depth - 1, 3 - player, alpha, beta)[0]
                if val > max_val:
                    max_val = val
                    best_move = move
                alpha = max(alpha, val)
                if alpha >= beta:
                    break
            return max_val, best_move
        else:
            min_val = math.inf
            best_move = None
            for move in valid_moves:
                new_board = self.simulate_move(board, move, player)
                val = self.alpha_beta(new_board, depth - 1, 3 - player, alpha, beta)[0]
                if val < min_val:
                    min_val = val
                    best_move = move
                beta = min(beta, val)
                if alpha >= beta:
                    break
            return min_val, best_move

    def simulate_move(self, board, move, player):
        new_board = Board()
        new_board.cells = [row[:] for row in board.cells]
        new_board.update(move[0], move[1], self)
        return new_board


class Game:
    def run(self):
        print("\nWelcome to Othello Game !!\n")
        Quit = False
        while not Quit:
            print("Please choose :\n")
            print("     (1) Play with computer.")
            print("     (2) Quit the game.\n")
            main_choice = int(input("Enter your choice : "))

            if main_choice == 1:
                print("\nPlayer 1 starts (Black) ..\n")
                choice = int(input("Do you want to be player 1 or 2 ? "))
                name = input("Enter your name : ")
                player = Player(choice, name)
                hardLevel = int(input("\n(1) Easy .\n(2) Medium .\n(3) Hard.\n  "))
                if (hardLevel < 4):
                    if choice == 1:
                        AI_player = AIPlayer(2, "Computer", hardLevel + 3)  # Computer
                    else:
                        AI_player = AIPlayer(1, "Computer", hardLevel + 3)  # Computer

                board = Board()
                board.instruction_display()
                board.set_players(player, AI_player)
                board.display()

                while True:
                    valid_move = False
                    while not valid_move:
                        print("Player", player.num, ":\nYour turn,", player.name, "..\nYour available pieces =",
                              player.available_pieces, "\n")
                        valid_moves = board.valid_moves(player.num)
                        if len(valid_moves) == 0:
                            player.available_pieces -=1
                            print("Sorry! No valid moves for you :(")
                            print("I have to skip your turn ..\n")
                            break
                        else:
                            print("Your valid choices are :")
                            for move in valid_moves:
                                print("     ", move)
                            x = int(input("\nEnter first index (row) : "))
                            y = int(input("Enter second index (column) : "))

                            if board.valid_move(x, y, player.num):
                                board.update(x, y, player)
                                player.available_pieces -= 1
                                valid_move = True
                            else:
                                print("Invalid cell ..\nPlease choose a valid one ..\n")

                    board.display()
                    if board.check_winner():
                        break

                    AI_player.pick_move(board)
                    board.display()
                    if board.check_winner():
                        break

            elif main_choice == 2:
                print("\nThank you for playing our Othello Game !!!")
                print("We hope you enjoyed and this is not the last time to play it .. Bye.")
                Quit = True

            else:
                print("\nInvalid choice :(\nTry again ..\n")



pygame.init()

# Set screen dimensions
screen_width = 800
screen_height = 600
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


def draw_text(text, font, color, x, y):
    lines = text.split('\n')
    for i, line in enumerate(lines):
        text_surface = font.render(line, True, color)
        text_rect = text_surface.get_rect(center=(x, y + i * font.get_height()))
        screen.blit(text_surface, text_rect)


class HomeScreen:
    def __init__(self):
        self.choose_input_text = ""
        self.name_input_text = ""
        self.level_input_text = ""
        self.choose_input_active = False
        self.name_input_active = False
        self.level_input_active = False
        self.choose_field = pygame.Rect(screen_width // 2 - 150, 150, 300, 40)
        self.name_field = pygame.Rect(screen_width // 2 - 150, 250, 300, 40)
        self.level_field = pygame.Rect(screen_width // 2 - 150, 350, 300, 40)
        self.submit_button_rect = pygame.Rect(screen_width // 2 + 175, 450, 100, 40)
        self.choose_button_color = blue
        self.message = "_"

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.choose_field.collidepoint(event.pos):
                    self.choose_input_active = True
                    self.name_input_active = False
                    self.level_input_active = False
                elif self.name_field.collidepoint(event.pos):
                    self.name_input_active = True
                    self.choose_input_active = False
                    self.level_input_active = False
                elif self.level_field.collidepoint(event.pos):
                    self.level_input_active = True
                    self.choose_input_active = False
                    self.name_input_active = False
                elif self.submit_button_rect.collidepoint(event.pos):
                    if self.name_input_text.strip() and self.choose_input_text in ["1", "2"] and self.level_input_text in ["1", "2", "3"]:
                        self.message = "Please, follow the instructions .. \nEach player has 30 pieces only. " \
                                       "If they run out, the game ends. \nChoose cell from the board and enter its " \
                                       "indices as shown in the following board .."
                        return "instruction"
                    else:
                        if not self.name_input_text.strip():
                            self.message = "Please enter your name"
                        if self.choose_input_text not in ["1", "2"]:
                            self.message = "Please enter 1 or 2(Player Number)"
                        if self.level_input_text not in ["1", "2", "3"]:
                            self.message = "Please enter 1 or 2 or 3 (Level)"

            elif event.type == pygame.KEYDOWN:
                if self.choose_input_active:
                    if event.key == pygame.K_BACKSPACE:
                        self.choose_input_text = self.choose_input_text[:-1]
                    elif event.unicode.isdigit():
                        self.choose_input_text += event.unicode

                elif self.name_input_active:
                    if event.key == pygame.K_BACKSPACE:
                        self.name_input_text = self.name_input_text[:-1]
                    else:
                        self.name_input_text += event.unicode
                elif self.level_input_active:
                    if event.key == pygame.K_BACKSPACE:
                        self.level_input_text = self.level_input_text[:-1]
                    else:
                        self.level_input_text += event.unicode

    def draw(self):
        screen.fill(black)

        draw_text("Welcome to Othello!", font_large, white, screen_width // 2, 50)
        draw_text("Player 1 starts (Black) ..", font_small, white, screen_width // 2, 100)
        draw_text("Do you want to be player 1 or 2 ?", font_small, white, screen_width // 2, 130)

        if self.message == "Please enter your name":
            pygame.draw.rect(screen, red, self.name_field.inflate(5, 5), border_radius=20)
            pygame.draw.rect(screen, white, self.name_field, border_radius=20)
        if self.message == "Please enter 1 or 2(Player Number)":
            pygame.draw.rect(screen, red, self.choose_field.inflate(5, 5), border_radius=20)
            pygame.draw.rect(screen, white, self.choose_field, border_radius=20)
        if self.message == "Please enter 1 or 2 or 3 (Level)":
            pygame.draw.rect(screen, red, self.level_field.inflate(5, 5), border_radius=20)
            pygame.draw.rect(screen, white, self.level_field, border_radius=20)

        pygame.draw.rect(screen, white, self.choose_field, border_radius=20)

        draw_text(self.choose_input_text, font_small, black, self.choose_field.centerx, self.choose_field.centery)

        draw_text("Enter Your Name", font_small, white, screen_width // 2, 230)
        pygame.draw.rect(screen, white, self.name_field, border_radius=20)
        draw_text(self.name_input_text, font_small, black, self.name_field.centerx, self.name_field.centery)

        draw_text("(1) Easy. (2) Medium. (3) Hard.", font_small, white, screen_width // 2, 330)
        pygame.draw.rect(screen, white, self.level_field, border_radius=20)
        draw_text(self.level_input_text, font_small, black, self.level_field.centerx, self.level_field.centery)
        pygame.draw.rect(screen, self.choose_button_color, self.submit_button_rect)
        draw_text("Submit", font_small, white, screen_width // 2 + 227, 470)

        draw_text(self.message, font_small, white, screen_width // 2, 450)



class InstructionScreen:
    def __init__(self):
        self.name_button_rect = pygame.Rect(screen_width // 2 - 60, screen_height//2, 100, 40)

    def handle_events(self , events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.name_button_rect.collidepoint(event.pos):
                    return "game"

    def draw(self):
        pygame.draw.rect(screen,blue, self.name_button_rect)
        draw_text("Start", font_small, white, screen_width // 2 -10,  screen_height//2 + 20)

        draw_text("Please, follow the instructions .. \nEach player has 30 pieces only. "
              "If they run out, the game ends. \nChoose a cell from the board and enter its "
              "indices as shown in the following board ..", font_small, white, screen_width // 2, screen_height//2 - 100)

class GameState:
    def __init__(self, player_name, player_num, level):
        self.player_name = player_name
        self.board = Board()
        self.player_num = player_num
        self.level = level

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Handle mouse clicks for player interaction
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Get the position of the mouse click
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # Check if the click is within the board area
                if 50 <= mouse_x <= 450 and 200 <= mouse_y <= 600:
                    # Calculate the row and column of the clicked square
                    row = (mouse_y - 200) // 50
                    col = (mouse_x - 50) // 50
                    # Implement logic for player moves here
                    print("Clicked on square:", row, col)
                    # You can call a method to handle the player's move based on the row and column

    def draw(self):
        p1 = Player(self.player_num, self.player_name)
        if self.player_num == 1:
            p2 = AIPlayer(2, "computer", self.level)
        else:
            p2 = AIPlayer(1, "computer", self.level)

        self.board.set_players(p1, p2)
        screen.fill(black)
        draw_text("Player: " + self.player_name, font_small, white,screen_width // 2, 60)
        draw_text("Opponent: Computer", font_small, white, screen_width // 2, 90)
        draw_text("Black: " + str(self.board.player1.available_pieces), font_small, white, screen_width // 2, 120)
        draw_text("White: " + str(self.board.player2.available_pieces), font_small, white, screen_width // 2, 150)

        cell_size = 50
        board_offset_x = 50
        board_offset_y = 200
        for i in range(8):
            for j in range(8):
                cell_x = board_offset_x + j * cell_size
                cell_y = board_offset_y + i * cell_size
                pygame.draw.rect(screen, green, (cell_x, cell_y, cell_size, cell_size))
                pygame.draw.rect(screen, black, (cell_x, cell_y, cell_size, cell_size), 1)
                # Add row and column numbers
                draw_text(str(i + 1), font_small, white, board_offset_x - 30, cell_y + cell_size // 2)
                draw_text(str(j+1), font_small, white, cell_x + cell_size // 2, board_offset_y - 30)

        # Display messages or instructions
        draw_text("Welcome to Othello!", font_large, white, screen_width // 2, 30)
        # Add more messages as needed

        pygame.display.flip()

def main():
    clock = pygame.time.Clock()
    home_state = HomeScreen()
    instruction_state = InstructionScreen()
    game_state = None
    current_state = "home"

    while True:
        events = pygame.event.get()

        if current_state == "home":
            next_state = home_state.handle_events(events)
            if next_state:
                current_state = next_state

        elif current_state == "instruction":
            next_state = instruction_state.handle_events(events)
            if next_state:
                game_state = GameState(home_state.name_input_text, home_state.choose_input_text , home_state.level_input_text)
                current_state = next_state
        elif current_state == "game":
            next_state = game_state.handle_events(events)
            if next_state:
                current_state = next_state

        screen.fill(black)

        if current_state == "home":
            home_state.draw()

        elif current_state == "instruction":
            instruction_state.draw()

        elif current_state == "game":
            game_state.draw()

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()

