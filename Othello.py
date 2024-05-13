###############################################################
#                            Board                            #
###############################################################

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
            if board.winner() == board.player1.num:
                print("\nCongratulations", board.player1.name, "( Player", board.player1.num, ") you won!\n")
                print("Hard luck", board.player2.name, "( Player", board.player2.num, ") ..\n")
            elif board.winner() == board.player2.num:
                print("\nCongratulations", board.player2.name, "( Player", board.player2.num, ") you won!\n")
                print("Hard luck", board.player1.name, "( Player", board.player1.num, ") ..\n")
            else:
                print("\nWow! It is tie ..\n")
            return True
        return False

    def valid_move(self, a, b, p_num):
        if 0 <= b < 8 and 8 > a >= 0 == self.cells[a][b]:
            if b < 7 and self.cells[a][b + 1] != p_num and self.cells[a][b + 1] != 0:
                for i in range(b + 2, 8):
                    if self.cells[a][i] == p_num:
                        return True
            if b > 0 and self.cells[a][b - 1] != p_num and self.cells[a][b - 1] != 0:
                for i in range(b - 1):
                    if self.cells[a][i] == p_num:
                        return True
            if a < 7 and self.cells[a + 1][b] != p_num and self.cells[a + 1][b] != 0:
                for i in range(a + 2, 8):
                    if self.cells[i][b] == p_num:
                        return True
            if a > 0 and self.cells[a - 1][b] != p_num and self.cells[a - 1][b] != 0:
                for i in range(a - 1):
                    if self.cells[i][b] == p_num:
                        return True
        return False

    def valid_moves(self, p_num):
        valid = []
        for i in range(8):
            for j in range(8):
                if board.valid_move(i, j, player.num):
                    valid.append("(" + str(i) + "," + str(j) + ")")
        return valid


##############################################################
#                           Player                           #
##############################################################

class Player:
    def __init__(self, x, n):
        self.num = x
        self.name = n
        self.available_pieces = 30


###############################################################
#                          AI Player                          #
###############################################################

class AIPlayer(Player):

    def pick_move(self, b):
        print("Not implemented yet :(\n")
        self.available_pieces -= 1


###############################################################
#                          Main Game                          #
###############################################################

print("\nWelcome to Othello Game !!\n")
Quit = False
while not Quit:
    print("Please choose :")
    print("     (1) For one player.")
    print("     (2) For two players.")
    print("     (3) Quit the game.\n")
    main_choice = int(input("Enter your choice : "))

    if main_choice == 1:
        print("\nPlayer 1 starts (Black) ..\n")
        choice = int(input(print("Do you want to be player 1 or 2 ? ")))
        name = input("Enter your name : ")
        player = Player(choice, name)
        if choice == 1:
            AI_player = AIPlayer(2, "Computer")             # Computer
        else:
            AI_player = AIPlayer(1, "Computer")             # Computer

        board = Board()
        board.instruction_display()
        board.set_players(player, AI_player)
        while True:
            board.display()
            valid_move = False
            while not valid_move:
                print("Player", player.num, ":\nYour turn,", player.name, "..\nYour available pieces =", player.available_pieces, "\n")
                print("Your valid choices are :")
                valid_moves = board.valid_moves(player.num)
                if len(valid_moves) == 0:
                    print("Sorry! No valid moves for you :(")
                    print("I have to skip your turn ..\n")
                    break
                else:
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
        print("\nPlayer 1 (Black) starts ..\n")
        name1 = input("Enter player-1's name : ")
        player1 = Player(1, name1)
        name2 = input("Enter player-2's name : ")
        player2 = Player(2, name2)

        board = Board()
        board.instruction_display()
        board.set_players(player1, player2)
        board.display()

        while True:
            valid_move = False
            while not valid_move:
                print("Player 1 :\n", player1.name, "'s turn ..\nYour available pieces = ", player1.available_pieces, "\n", sep='')
                print("Your valid choices are :")
                valid_moves1 = board.valid_moves(player1.num)
                if len(valid_moves1) == 0:
                    print("Sorry! No valid moves for you :(")
                    print("I have to skip your turn ..\n")
                    break
                else:
                    for move in valid_moves1:
                        print("     ", move)
                    x1 = int(input("\nEnter first index (row) : "))
                    y1 = int(input("Enter second index (column) : "))
                    if board.valid_move(x1, y1, 1):
                        board.update(x1, y1, player1)
                        player1.available_pieces -= 1
                        valid_move = True
                    else:
                        print("\nInvalid cell ..\nPlease choose a valid one ..\n")
            board.display()
            if board.check_winner():
                break

            valid_move = False
            while not valid_move:
                print("Player 2 :\n", player2.name, "'s turn ..\nYour available pieces = ", player2.available_pieces, "\n", sep='')
                print("Your valid choices are :")
                valid_moves2 = board.valid_moves(player2.num)
                if len(valid_moves2) == 0:
                    print("Sorry! No valid moves for you :(")
                    print("I have to skip your turn ..\n")
                    break
                else:
                    for move in valid_moves2:
                        print("     ", move)
                    x2 = int(input("\nEnter first index (row) : "))
                    y2 = int(input("Enter second index (column) : "))
                    if board.valid_move(x2, y2, 2):
                        board.update(x2, y2, player2)
                        player2.available_pieces -= 1
                        valid_move = True
                    else:
                        print("\nInvalid cell :(\nPlease choose a valid one ..\n")
            board.display()
            if board.check_winner():
                break

    elif main_choice == 3:
        print("\nThank you for playing our Othello Game !!!")
        print("We hope you enjoyed and this is not the last time to play it .. Bye.")
        Quit = True

    else:
        print("\nInvalid choice :(\nTry again ..\n")

