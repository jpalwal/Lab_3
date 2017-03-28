import abc

class NotANumber(Exception):
    pass


class AbstractValidator(object):
    __metaclass__  = abc.ABCMeta
    @abc.abstractmethod
    def validate(self, to_be_validated):
        """validate the input"""


class InputExpressionValidator(AbstractValidator):

    def __init__(self, to_be_validated):
        self.expression = to_be_validated

    def validate(self):
        if not self._is_number():
            raise NotANumber()
        else:
            return True
    def _is_number(self):
        return isinstance(self.expression, int)
