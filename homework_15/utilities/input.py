import os
import re
from typing import Callable

from .field import Field


def validate_age(value, lower_bound: int = 1, upper_bound: int = 99) -> int:
    """Get and check that user input age is valid."""
    if not value.isdigit():
        raise ValueError(f"Invalid input! '{value}' is not an integer value!")
    value = int(value)
    if value < lower_bound:
        raise ValueError(
            f"Entered age should be greater than or equal to {lower_bound}"
        )
    elif value > upper_bound:
        raise ValueError(
            f"Entered age should be smaller than or equal to {upper_bound}"
        )
    else:
        return value


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


def validate_str(field: Field, value) -> bool:
    """
    Get and check that user input is valid for fields: surname, name, phone number, email.
    """
    if field == Field.SURNAME or field == Field.NAME:
        regex = r"[A-Za-z]+"
    elif field == Field.PHONE_NUMBER:
        regex = r"\+1\d{10}$"
    else:
        regex = r"[\w.-]+@[A-Za-z]+\.[a-z]{2,}"
    if re.fullmatch(regex, value):
        return value
    else:
        raise ValueError("Invalid input! Please, enter correct value.")


def validate_filename(filename):
    if not os.path.exists(filename):
        raise FileExistsError(f"'{filename}' not found. Check the file name and path.")
    return filename


def input_value(prompt: str, validator: Callable, field=None):
    while True:
        value = input(prompt)
        try:
            if field:
                value = validator(field, value)
                return value
            else:
                value = validator(value)
                return value
        except ValueError as e:
            print(str(e))
        except FileExistsError as err:
            print(str(err))
