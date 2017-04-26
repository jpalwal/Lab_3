import validator
import enum


class Game:
    def __init__(self, board_size):
        self.checkMove = validator.InputExpressionValidator
        self.emptySquares = board_size**2
        self.board = [[MarkSquare.FREE for x in range(board_size)] for y in range(board_size)]
        self.nowPlaying = 'u'

    def choose_square(self,x,y):
        if self.checkMove.validate(x,y, len(self.board)):
            if self.board[y][x] == MarkSquare.FREE:
                self.board[y][x] = MarkSquare.CROSS if self.nowPlaying == 'u' else MarkSquare.CIRCLE
                self.emptySquares -= 1
                return True
            else:
                return False

    def switch_player(self):
        self.nowPlaying = 'u' if self.nowPlaying == 'c' else 'c'

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

    def computer_turn(self):
        return self.nowPlaying == 'c'

    def board(self):
        return self.board


class MarkSquare(enum.Enum):
    FREE = 0
    CIRCLE = 'o'
    CROSS = 'x'


class CheckGameResult(enum.Enum):
    PLAYING = 0
    CIRCLE = 'o'
    CROSS = 'x'
    DRAW = 'r'


# zapis jest źle
class MakeAndPrintBoard():
    @staticmethod
    def print_board(board):
        print('\n')
        print('\t')
        print(''.join(str([i for i in range(len(board.board))])))
        for i in range(len(board.board)):
            marker = '{}\t'.format(i)
            for j in range(len(board.board[i])):
                if board.board[i][j] == MarkSquare.FREE:
                    marker.join('_')
                elif board.board[i][j] == MarkSquare.CROSS:
                    marker.join('X')
                elif board.board[i][j] == MarkSquare.CIRCLE:
                    marker.join('O')
            marker.join('\t')
            marker.join(str(i))
            print(marker)
        print('\t')
        print(''.join(str([i for i in range(len(board.board))])))


class Lan:
    @staticmethod
    def send_data(connection, data):
        connection.sendall('#start#{}#end'.format(data).encode('ASCII'))
    @staticmethod
    def request_data(connection):
        data=''
        while True:
            buffer=connection.recv(16)
            data += buffer.decode('ASCII')
            if '#end' in data:
                break
            elif '#start#' in data:
                data = data.replace('#start#','')
            elif buffer:
                pass
            else:
                break
        return data.replace('#start#','').replace('#end','')
    @staticmethod
    def send_and_request_data(connection, data):
        Lan.send_data(connection,data)
        return Lan.request_data(connection)
