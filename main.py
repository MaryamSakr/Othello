import math


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
                    self.cells[a][j] = p.num
        for i in range(b + 2, 8):
            if self.cells[a][i] == p.num:
                for j in range(b, i):
                    self.cells[a][j] = p.num
        for i in range(a - 1):
            if self.cells[i][b] == p.num:
                for j in range(i, a):
                    self.cells[j][b] = p.num
        for i in range(a + 2, 8):
            if self.cells[i][b] == p.num:
                for j in range(a, i):
                    self.cells[j][b] = p.num

    def instruction_display(self):
        print("\nPlease, follow the instructions ..")
        print("Each player has 25 pieces only. If they run out, the game ends.\n")
        print("Choose cell from the board and enter its indices as shown in the following board ..\n")
        for i in range(len(self.cells)):
            print("-----------------------------------------------------------------")
            print("| ", end='')
            for j in range(len(self.cells[i])):
                print("(", i, ",", j, ") | ", end='', sep='')
            print()
        print("-----------------------------------------------------------------")

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
        move = self.minimax(board, self.depth, self.num, -math.inf, math.inf)
        if move is not None:
            if move[1] is not None:  # Check if the move is not None
                board.update(move[1][0], move[1][1], self)
            else:
                print("No valid moves available. Skipping turn.")
                self.available_pieces -= 1
        else:
            print("No valid moves available. Skipping turn.")
            self.available_pieces -= 1

    def minimax(self, board, depth, player, alpha, beta):
        if depth == 0 or board.is_full():
            return board.utility(), None

        valid_moves = board.valid_moves(player)
        if not valid_moves:
            if board.valid_moves(3 - player):
                return self.minimax(board, depth - 1, 3 - player, alpha, beta)[0], None
            else:
                return board.utility(), None

        if player == self.num:
            max_val = -math.inf
            best_move = None
            for move in valid_moves:
                new_board = self.simulate_move(board, move, player)
                val = self.minimax(new_board, depth - 1, 3 - player, alpha, beta)[0]
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
                val = self.minimax(new_board, depth - 1, 3 - player, alpha, beta)[0]
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
                if choice == 1:
                    AI_player = AIPlayer(2, "Computer", 3)  # Computer
                else:
                    AI_player = AIPlayer(1, "Computer", 3)  # Computer

                board = Board()
                board.instruction_display()
                board.set_players(player, AI_player)
                while True:
                    board.display()
                    valid_move = False
                    while not valid_move:
                        print("Player", player.num, ":\nYour turn,", player.name, "..\nYour available pieces =",
                              player.available_pieces, "\n")
                        valid_moves = board.valid_moves(player.num)
                        if len(valid_moves) == 0:
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


if __name__ == "__main__":
    game = Game()
    game.run()
