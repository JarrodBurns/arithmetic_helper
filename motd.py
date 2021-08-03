
message = [
    "Welcome to the Virtual Chalkboard Arithmetic Formatter!",
    "",
    "To get started type the problem you would like",
    "to solve in the following format:",
    "",
    "1 + 2",
    "",
    "Up to (5) problems may be submitted at once.",
    "",
    "1 + 2, 4 - 3 ...",
    "",
    "To display the solution with you problem",
    "type True or False.",
    "",
    "1 + 2, True",
    "",
    "When submitting multiple problems:",
    "",
    "1 + 2, 4 - 3 ..., True",
    "",
    "Only Addition and subtraction are supported.",
    "Numbers may not exceed (4) digits in length.",
    "",
    'You may exit this program at anytime by typing "Quit"'
]


def motd(padding=61):
    """
    Displays the current Message of the Day.
    Default centerline padding is 61.
    """
    for i in message:
        # padding = int(padding)

        if i == message[0]:
            print("*", "-" * padding, "*")
            print("|", " " * padding, "|")
        if i == message[-1]:
            print("|", i.center(padding), "|")
            print("|", " " * padding, "|")
            print("*", "-" * padding, "*")
        else:
            print("|", i.center(padding), "|")
