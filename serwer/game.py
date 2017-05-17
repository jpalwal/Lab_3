import validator
import enum
import logging
from os import path, remove

class Game:
    def __init__(self, board_size):
        self.checkMove = validator.InputExpressionValidator
        self.emptySquares = board_size**2
        self.board = [[MarkSquare.FREE for x in range(board_size)] for y in range(board_size)]
        self.nowPlaying = 'u'
        self.boardSize = board_size
        if path.isfile("game.log"):
            remove("game.log")
        logging.basicConfig(filename="game.log", level=logging.INFO)
        logging.info("Game initialization")


    def choose_square(self,x,y):
        logging.info("Check if coords are ok and if field ({}, {}) is emptyd to place a marker".format(x, y))
        try:
            self.checkMove.validate(x,y, len(self.board))
        except validator.OutOfBoard():
            logging.info("Cordinates ({}, {}) are invalid".format(x, y))
            return -1
        if self.board[y][x] == MarkSquare.FREE:
            self.board[y][x] = MarkSquare.CROSS if self.nowPlaying == 'u' else MarkSquare.CIRCLE
            self.emptySquares -= 1
            logging.info("field ({}, {}) is empty and marker placed".format(x, y))
            return True
        else:
            logging.info("field ({}, {}) is not empty and quit".format(x, y))
            return False


    def switch_player(self):
        self.nowPlaying = 'u' if self.nowPlaying == 'c' else 'c'
        logging.info("switching player for user") if self.nowPlaying == 'c' else logging.info("switching player for computer")

    def game_over(self):
        if not self.emptySquares:
            logging.info("No empty squares, draw")
            return CheckGameResult.DRAW
        check = 0
        #horizontal
        for i in range(len(self.board)):
            for j in range((len(self.board))):
                if self.board[i][j] == MarkSquare.CIRCLE or self.board[i][j] == MarkSquare.FREE:
                    check=1
            if not check:
                logging.info("horizontal winning, winner is cross")
                return CheckGameResult.CROSS
            check = 0
        for i in range(len(self.board)):
            for j in range((len(self.board))):
                if self.board[i][j] == MarkSquare.CROSS or self.board[i][j] == MarkSquare.FREE:
                    check = 1
            if not check:
                logging.info("horizontal winning, winner is circle")
                return CheckGameResult.CIRCLE
            check = 0
        #vertical
        for i in range(len(self.board)):
            for j in range((len(self.board))):
                if self.board[j][i] == MarkSquare.CIRCLE or self.board[j][i] == MarkSquare.FREE:
                    check=1
            if not check:
                logging.info("vertical winning, winner is cross")
                return CheckGameResult.CROSS
            check = 0
        for i in range(len(self.board)):
            for j in range((len(self.board))):
                if self.board[j][i] == MarkSquare.CROSS or self.board[j][i] == MarkSquare.FREE:
                    check = 1
            if not check:
                logging.info("vertical winning, winner is circle")
                return CheckGameResult.CIRCLE
            check = 0
        logging.info("no winner, still playing")
        return CheckGameResult.PLAYING

    def computer_turn(self):
        logging.info("checking whose turn it is")
        print("check if comp turn")
        print(self.nowPlaying == 'c')
        return self.nowPlaying == 'c'

    def board(self):
        return self.board



class MarkSquare(enum.Enum):
    FREE = 0
    CIRCLE = 'o'
    CROSS = 'x'


class CheckGameResult(enum.Enum):
    PLAYING = 'p'
    CIRCLE = 'o'
    CROSS = 'x'
    DRAW = 'r'



class MakeAndPrintBoard():
    @staticmethod
    def print_board(board):
        print("print_board")
        print('\n')
        print('\t' + ''.join(['{}    '.format(i) for i in range(0, len(board.board))]))
        for i in range(0, len(board.board)):
            marker=[]
            for j in range(0, len(board.board[i])):
                if board.board[i][j] == MarkSquare.FREE:
                    marker.append('_')
                elif board.board[i][j] == MarkSquare.CROSS:
                    marker.append('X')
                elif board.board[i][j] == MarkSquare.CIRCLE:
                    marker.append('O')
                else:
                    marker.append('_')
            print(i, marker)
        print('\t' + ''.join(['{}    '.format(i) for i in range(0, len(board.board))]))
