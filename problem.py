
class Problem:
    """
    Takes (2) inputs: list and optional, boolean expression.
    Default bool is False.
    """

    def __init__(self, list, bool=False):
        self.list = list
        self.boolean = bool

    def addition(self, x, y):
        return int(x) + int(y)

    def subtraction(self, x, y):
        return int(x) - int(y)

    def bottom(self, element):
        t = self.list[element]
        return t.split()[2]

    def top(self, element):
        t = self.list[element]
        return t.split()[0]

    def length(self, element):
        t = self.list[element]
        return max(len(t.split()[0]), len(t.split()[2]))

    def sign(self, element):
        t = self.list[element]
        return t.split()[1]

    def dash(self, element):
        return "-" * (self.length(element) + 2)

    def number_of_problems(self):
        return len(self.list)

    def answer(self, element):
        """
        Checks for addition() via "+", defaults
        to subtraction() otherwise.
        """
        t = self.list[element]
        t = t.split()

        if t[1] == "+":
            return str(self.addition(t[0], t[2]))
        return str(self.subtraction(t[0], t[2]))

    def all_tops(self):
        t = []
        for i in self.list:
            t.append(i.split()[0])
        return t

    def all_bottoms(self):
        t = []
        for i in self.list:
            t.append(i.split()[2])
        return t

    def all_max_lengths(self):
        """
        Returns the longest for each set of values.
        """
        t = []
        for i in self.list:
            t.append(max(len(i.split()[0]), len(i.split()[2])))
        return t

    def all_operators(self):
        t = []
        for i in self.list:
            t.append(i.split()[1])
        return t

    def format_row_header(self):
        """
        Uses the length of format_row_one() for spacing.
        """
        t = []
        t.append("*")
        t.append("-" * (len(self.format_row_one()) - 2))
        t.append("*")
        return("".join(t))

    def format_row_spacer(self):
        """
        Uses the length of format_row_one() for spacing.
        """
        t = []
        t.append("|")
        t.append(" " * (len(self.format_row_one()) - 2))
        t.append("|")
        return("".join(t))

    def format_row_one(self):
        """
        Value 1.
        """
        t = []
        for i in range(0, self.number_of_problems()):
            if i == 0:
                t.append("|    ")
            t.append(self.top(i).rjust(self.length(i) + 2))
            t.append("    ")
        t.append("|")
        return "".join(t)

    def format_row_two(self):
        """
        Value 2.
        """
        t = []
        for i in range(0, self.number_of_problems()):
            if i == 0:
                t.append("|    ")
            t.append(self.sign(i))
            t.append(self.bottom(i).rjust(self.length(i) + 1))
            t.append("    ")
        t.append("|")
        return "".join(t)

    def format_row_three(self):
        """
        The dashes.
        """
        t = []
        for i in range(0, self.number_of_problems()):
            if i == 0:
                t.append("|    ")
            t.append(self.dash(i))
            t.append("    ")
        t.append("|")
        return "".join(t)

    def format_row_four(self):
        """
        The answers.
        """
        t = []
        for i in range(0, self.number_of_problems()):
            if i == 0:
                t.append("|    ")
            t.append(self.answer(i).rjust(self.length(i) + 2))
            t.append("    ")
        t.append("|")
        return "".join(t)
