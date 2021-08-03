
from problem import Problem


class FormatRow(Problem):
    """
    Inherits from Problem.
    """

    def __init__(self, list, bool):
        super().__init__(list, bool)

    def header(
        self,
        left_corner="*",
        padding="-",
        right_corner="*"
    ):
        """
        Uses the length of self.value_one() for spacing.
        """
        t = []
        t.append(left_corner)
        t.append(padding * (len(self.value_one()) - 2))
        t.append(right_corner)
        return("".join(t))

    def spacer(
        self,
        left_column="|",
        padding=" ",
        right_column="|"
    ):
        """
        Uses the length of self.value_one() for spacing.
        """
        t = []
        t.append(left_column)
        t.append(padding * (len(self.value_one()) - 2))
        t.append(right_column)
        return("".join(t))

    def value_one(
        self,
        left_column="|",
        padding=" ",
        right_column="|",

    ):
        """
        Value 1.
        """
        t = []
        for i in range(0, self.number_of_problems()):
            if i == 0:
                t.append(left_column)
                t.append(padding * 4)
            t.append(self.top(i).rjust(self.length(i) + 2))
            t.append(padding * 4)
        t.append(right_column)
        return "".join(t)

    def value_two(
        self,
        left_column="|",
        padding=" ",
        right_column="|",
    ):
        """
        Value 2.
        """
        t = []
        for i in range(0, self.number_of_problems()):
            if i == 0:
                t.append(left_column)
                t.append(padding * 4)
            t.append(self.sign(i))
            t.append(self.bottom(i).rjust(self.length(i) + 1))
            t.append(padding * 4)
        t.append(right_column)
        return "".join(t)

    def value_dash(
        self,
        left_column="|",
        padding=" ",
        right_column="|"
    ):
        """
        The dashes.
        """
        t = []
        for i in range(0, self.number_of_problems()):
            if i == 0:
                t.append(left_column)
                t.append(padding * 4)
            t.append(self.dash(i))
            t.append(padding * 4)
        t.append(right_column)
        return "".join(t)

    def value_answer(
        self,
        left_column="|",
        padding=" ",
        right_column="|"
    ):
        """
        The answers.
        """
        t = []
        for i in range(0, self.number_of_problems()):
            if i == 0:
                t.append(left_column)
                t.append(padding * 4)
            t.append(self.answer(i).rjust(self.length(i) + 2))
            t.append(padding * 4)
        t.append(right_column)
        return "".join(t)
