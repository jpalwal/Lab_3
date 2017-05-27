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

    @staticmethod
    def validate(x,y,n):
        if (not InputExpressionValidator._is_number(x)) and (not InputExpressionValidator._is_number(y)) and (not InputExpressionValidator._is_number(n)):
            raise NotANumber("input is not a number")
        elif InputExpressionValidator._out_of_board(x,n) or InputExpressionValidator._out_of_board(y,n):
            raise OutOfBoard("coords out of booard")
        else:
            return True

    @staticmethod
    def _is_number(a):
        return isinstance(a, int)

    @staticmethod
    def _out_of_board(a,n):
        return (a < 0) or (a >= n)