import re


def get_input_int(prompt, lower_bound=1, upper_bound=99):
    """Get and check user input age."""
    while True:
        user_input = input(prompt)
        try:
            input_age = int(user_input)

            if input_age < lower_bound:
                print(f"Entered age should be greater than or equal to {lower_bound}")
            elif input_age > upper_bound:
                print(f"Entered age should be smaller than or equal to {upper_bound}")
            else:
                return input_age

        except ValueError:
            print(f"Invalid input! '{user_input}' is not an integer value!")


def get_input_choice_menu(option):
    """Get and check user input"""
    while True:
        user_input = input("Choose one of the options: ")

        if user_input.lower() in option:
            return user_input

        elif not user_input:
            print("Invalid input! Input can't be empty")

        else:
            print(
                f"Invalid input! Only {', '.join(map(str, option))} options are available"
            )


def get_input_str(prompt, field):
    if field == "surname" or field == "name":
        regex = r'[A-Za-z]+'
    elif field == "phone_number":
        regex = r'\+1\d{10}$'
    else:
        regex = r'[\w.-]+@[A-Za-z]+\.[a-z]{2,}'
    while True:
        user_input = input(prompt)
        if re.fullmatch(regex, user_input):
            return user_input
        print(f"Invalid input! Please, enter correct {field}.")