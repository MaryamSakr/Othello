import math

from Board import Board


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
                return self.alpha_beta(board, int(depth) - 1, 3 - player, alpha, beta)[0], None
            else:
                return board.utility(), None

        if player == self.num:
            max_val = -math.inf
            best_move = None
            for move in valid_moves:
                new_board = self.simulate_move(board, move, player)
                val = self.alpha_beta(new_board, int(depth) - 1, 3 - player, alpha, beta)[0]
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


