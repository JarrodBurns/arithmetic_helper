
from problem import Problem


class ErrorChecker(Problem):
    """
    Inherits from Problem.
    """

    def __init__(self, list, bool):
        super().__init__(list, bool)

    def more_than_five(self, user_input):

        if len(user_input) > 5:
            return True
        return False

    def not_add_or_sub(self):

        for i in self.all_operators():
            if i != "+" and i != "-":
                return True
        return False

    def too_many_digits(self):

        for i in self.all_max_lengths():
            if i > 4:
                return True
        return False

    def not_a_number(self):

        for i in self.all_tops():
            if i.isdigit() is False and i is not bool:
                return True

        for i in self.all_bottoms():
            if i.isdigit() is False and i is not bool:
                return True
        return False

    def is_a_float(self):

        for i in self.all_tops():
            if type(i) is float and i is not bool:
                return True

        for i in self.all_bottoms():
            if type(i) is float and i is not bool:
                return True
        return False
