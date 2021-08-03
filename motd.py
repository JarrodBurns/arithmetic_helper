
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


def motd(
    padding=61,
    corner="*",
    left_and_right_column="|",
    top_and_bottom_row="-",
    white_space=" "

):
    """
    Displays the current Message of the Day.
    Default centerline padding is 61.
    """
    for i in message:

        if i == message[0]:
            print(corner,
                  top_and_bottom_row * padding,
                  corner
                  )
            print(left_and_right_column,
                  white_space * padding,
                  left_and_right_column
                  )

        if i == message[-1]:
            print(
                left_and_right_column,
                i.center(padding),
                left_and_right_column
            )
            print(
                left_and_right_column,
                white_space * padding,
                left_and_right_column
            )
            print(
                corner,
                top_and_bottom_row * padding,
                corner
            )

        else:
            print(left_and_right_column,
                  i.center(padding),
                  left_and_right_column
                  )
