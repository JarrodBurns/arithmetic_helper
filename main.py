
from formatrow import FormatRow
from errorchecker import ErrorChecker
from motd import motd


# Prints the Message of the Day.
motd()

while True:

    try:

        user_input = input("Enter your problem here: ")
        user_input = user_input.lower()

        if user_input == "quit":
            break

        user_input = user_input.split(", ")

        # Checks to see if the user passes a boolean.
        # If yes, that boolean is passed on to the class.
        # Both this variable and class are False by default.
        # True will show answers and problems.
        # False will show problems only.
        class_bool_found = False

        if "true" in user_input:
            user_input.remove("true")
            class_bool_found = True

        if "false" in user_input:
            user_input.remove("false")
            class_bool_found = False

        # instantiate class
        prob_one = FormatRow(user_input, class_bool_found)
        prob_check = ErrorChecker(user_input, class_bool_found)

        error_found = False

        while error_found is False:

            if prob_check.more_than_five(user_input) is True:
                print("Error: Too many problems.")
                error_found = True
                break

            if prob_check.not_a_number() is True:
                print("Error: Numbers must only contain digits.")
                error_found = True
                break

            if prob_check.not_add_or_sub() is True:
                print("Error: Operator must be '+' or '-'.")
                error_found = True
                break

            if prob_check.is_a_float() is True:
                print("Error: Only whole numbers are allowed.")
                error_found = True
                break

            if prob_check.too_many_digits() is True:
                print("Error: Numbers cannot be more than four digits.")
                error_found = True
                break

            if error_found is False:
                if prob_one.show_answer is True:
                    print(prob_one.header())
                    print(prob_one.spacer())
                    print(prob_one.value_one())
                    print(prob_one.value_two())
                    print(prob_one.value_dash())
                    print(prob_one.value_answer())
                    print(prob_one.spacer())
                    print(prob_one.header())
                else:
                    print(prob_one.header())
                    print(prob_one.spacer())
                    print(prob_one.value_one())
                    print(prob_one.value_two())
                    print(prob_one.value_dash())
                    print(prob_one.spacer())
                    print(prob_one.spacer())
                    print(prob_one.header())

                break

    except IndexError:
        print("Invalid input. Try again.")
