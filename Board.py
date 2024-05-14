class Board:
    def __init__(self):
        self.player2 = None
        self.player1 = None
        self.rows = 8
        self.cols = 8
        self.cells = [[0] * self.cols for _ in range(self.rows)]
        self.cells[3][3] = self.cells[4][4] = 1
        self.cells[3][4] = self.cells[4][3] = 2
        self.turn = 1
        self.player1_name = ""
        self.player2_name = ""
        self.p1_pieces = 30
        self.p2_pieces = 30
        self.level = 1



    def set_players(self, p1, p2):
        self.player1 = p1
        self.player2 = p2



    def update(self, a, b, p):
        self.cells[a][b] = p.num
        for i in range(b - 1, -1, -1):
            if self.cells[a][i] == 0:
                break
            if self.cells[a][i] == p.num:
                for j in range(i, b):
                    self.cells[a][j] = p.num
        for i in range(b + 1, 8):
            if self.cells[a][i] == 0:
                break
            if self.cells[a][i] == p.num:
                for j in range(b, i):
                    self.cells[a][j] = p.num
        for i in range(a - 1, -1, -1):
            if self.cells[i][b] == 0:
                break
            if self.cells[i][b] == p.num:
                for j in range(i, a):
                    self.cells[j][b] = p.num
        for i in range(a + 1, 8):
            if self.cells[i][b] == 0:
                break
            if self.cells[i][b] == p.num:
                for j in range(a, i):
                    self.cells[j][b] = p.num


    def valid_move(self, a, b, p_num):
        if 0 <= b < 8 and 8 > a >= 0 == self.cells[a][b]:
            if b < 7 and self.cells[a][b + 1] != p_num and self.cells[a][b + 1] != 0:
                for i in range(b + 2, 8):
                    if self.cells[a][i] == 0:
                        break
                    if self.cells[a][i] == p_num:
                        return True
            if b > 0 and self.cells[a][b - 1] != p_num and self.cells[a][b - 1] != 0:
                for i in range(b - 2, -1, -1):
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
                for i in range(a - 2, -1, -1):
                    if self.cells[i][b] == 0:
                        break
                    if self.cells[i][b] == p_num:
                        return True
        return False


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
                return 2
            elif self.player2.available_pieces == 0:
                print("Your pieces have been run out,", self.player2.name, "!")
                return 1
            if self.winner() == self.player1.num:
                print("\nCongratulations", self.player1.name, "( Player", self.player1.num, ") you won!\n")
                print("Hard luck", self.player2.name, "( Player", self.player2.num, ") ..\n")
                return 1
            elif self.winner() == self.player2.num:
                print("\nCongratulations", self.player2.name, "( Player", self.player2.num, ") you won!\n")
                print("Hard luck", self.player1.name, "( Player", self.player1.num, ") ..\n")
                return 2
            else:
                print("\nWow! It is tie ..\n")
                return 0


    def utility(self):
        black_count = sum(row.count(1) for row in self.cells)
        white_count = sum(row.count(2) for row in self.cells)

        if black_count > white_count:
            return 1
        elif white_count > black_count:
            return -1
        else:
            return 0
