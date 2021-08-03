
from problem import Problem
from motd import motd

# Prints the Message of the Day.
motd()

while True:

    try:

        j_input = input("Enter your problem here: ")
        j_input = j_input.lower()

        if j_input == "quit":
            break

        j_input = j_input.split(", ")

        # Checks to see if the user passes a class bool
        # Both this variable and class are False by default.
        # True will show answers and problems.
        # False will show problems only.
        class_bool_found = False

        if "true" in j_input:
            j_input.remove("true")
            class_bool_found = True

        if "false" in j_input:
            j_input.remove("false")
            class_bool_found = False

        # instantiate class
        prob_one = Problem(j_input, class_bool_found)

        error_found = False

        while error_found is False:

            if len(j_input) > 5:
                print("Error: Too many problems.")
                error_found = True

            for i in prob_one.all_operators():
                if i != "+" and i != "-":
                    print("Error: Operator must be '+' or '-'.")
                    error_found = True

            for i in prob_one.all_bottoms():
                if i.isdigit() is True and i is not bool:
                    print("Error: Numbers must only contain digits.")
                    error_found = True

                if type(i) is float and i is not bool:
                    print("Error: Only whole numbers are allowed.")
                    error_found = True

            for i in prob_one.all_tops():
                if i.isdigit() is True and i is not bool:
                    print("Error: Numbers must only contain digits.")
                    error_found = True

                if type(i) is float and i is not bool:
                    print("Error: Only whole numbers are allowed.")
                    error_found = True

            for i in prob_one.all_max_lengths():
                if i > 4:
                    print("Error: Numbers cannot be more than four digits.")
                    error_found = True

            if error_found is False:
                if prob_one.boolean is True:
                    print(prob_one.format_row_header())
                    print(prob_one.format_row_spacer())
                    print(prob_one.format_row_one())
                    print(prob_one.format_row_two())
                    print(prob_one.format_row_three())
                    print(prob_one.format_row_four())
                    print(prob_one.format_row_spacer())
                    print(prob_one.format_row_header())
                else:
                    print(prob_one.format_row_header())
                    print(prob_one.format_row_spacer())
                    print(prob_one.format_row_one())
                    print(prob_one.format_row_two())
                    print(prob_one.format_row_three())
                    print(prob_one.format_row_spacer())
                    print(prob_one.format_row_spacer())
                    print(prob_one.format_row_header())
                break

    except IndexError:
        print("Invalid input. Try again.")
