import re


def validate_age(prompt: str, lower_bound: int = 1, upper_bound: int = 99) -> int:
    """Get and check that user input age is valid."""
    while True:
        user_input = input(prompt)
        try:
            input_age = int(user_input)
        except ValueError:
            print(f"Invalid input! '{user_input}' is not an integer value!")
            continue

        if input_age < lower_bound:
            print(f"Entered age should be greater than or equal to {lower_bound}")
        elif input_age > upper_bound:
            print(f"Entered age should be smaller than or equal to {upper_bound}")
        else:
            return input_age


def get_input_choice_menu(option: dict) -> str:
    """Get and check that user menu choice is valid."""
    while True:
        user_input = input("Choose one of the options: ").lower()

        if user_input in option:
            return user_input

        elif not user_input:
            print("Invalid input! Input can't be empty")

        else:
            print(
                f"Invalid input! Only {', '.join(map(str, option))} options are available"
            )


def validate_str(prompt: str, field: str) -> str:
    """
    Get and check that user input is valid for fields: surname, name, phone number, email.
    """
    if field == "surname" or field == "name":
        regex = r"[A-Za-z]+"
    elif field == "phone_number":
        regex = r"\+1\d{10}$"
    elif field == "email":
        regex = r"[\w.-]+@[A-Za-z]+\.[a-z]{2,}"
    else:
        raise Exception("Invalid field")
    while True:
        user_input = input(prompt)
        if re.fullmatch(regex, user_input):
            return user_input
        print(f"Invalid input! Please, enter correct {field}.")
