import validator
import enum
import numpy


class MarkSquare(enum.Enum):
    FREE = 0
    CIRCLE = 'o'
    CROSS = 'x'


class CheckGameResult(enum.Enum):
    PLAYING = 0
    CIRCLE = 'o'
    CROSS = 'x'
    DRAW = 'r'


class Game():
    def __init__(self, board_size):
        self.checkMove = validator.InputExpressionValidator
        self.user = MarkSquare.CROSS
        self.computer = MarkSquare.CIRCLE
        self.emptySquares = board_size**2
        self.board = [[MarkSquare.FREE for y in range(board_size)] for x in range(board_size)]
        self.nowPlaying = 'u'

    def choose_square(self,x,y):
        if self.checkMove.validate(x,y, len(self.board)):
            if self.board[x][y] == MarkSquare.FREE:
                self.board[x][y] = self.user if self.nowPlaying == 'u' else self.computer
                self.emptySquares -= 1
                return True
            else:
                return False

    def switch_player(self):
        self.nowPlaying = 'u' if self.nowPlaying == 'c' else  'c'

    def game_over(self):
        if not self.emptySquares:
            return CheckGameResult.DRAW
        for i in range(len(self.board)):
            for j in range((len(self.board))):
                if self.board[i][j] == 'o':
                    break
            else:
                return CheckGameResult.CROSS
        for i in range(len(self.board)):
            for j in range((len(self.board))):
                if self.board[i][j] == 'x':
                    break
            else:
                return CheckGameResult.CROSS
        return CheckGameResult.PLAYING
