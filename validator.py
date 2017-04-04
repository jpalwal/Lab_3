import abc


class NotANumber(Exception):
    pass


class OutOfBoard(Exception):
    pass


class AbstractValidator(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def validate(self, coord_x, coord_y, board_size):
        """validate the input"""


class InputExpressionValidator(AbstractValidator):

    def __init__(self, coord_x, coord_y, board_size):
        self.x = coord_x
        self.y = coord_y
        self.boardSize = board_size

    def validate(self):
        if not self._is_number():
            raise NotANumber()
        elif self._out_of_board():
            raise OutOfBoard()
        else:
            return True

    def _is_number(self):
        return isinstance(self.x, int) and isinstance(self.y, int) and isinstance(self.boardSize, int)

    def _out_of_board(self):
        return (self.x < 0) or (self.y > self.boardSize) or (self.y < 0) or (self.y > self.boardSize)