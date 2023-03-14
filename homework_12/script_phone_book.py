"""Phone book

This script allows the user to apply CRUD operations to the phone contacts.

Script also allows to search records by fields, count records in phone book,
count average age, load from file and save from file.


To run the program use parameters:
    filename - Path to File
    verbose (True/False) - allows to ON/OFF decorator for detailed processing info
"""

import json
import os
import argparse

from utilities.input import get_input_str, get_input_int, get_input_choice_menu
from utilities.wrapper import verbose_mode

verbose = False


def display_record(number, record):
    print("--[ %s ]--------------------------" % number)
    print("| Surname: %20s |" % record["surname"])
    print("| Name:    %20s |" % record["name"])
    print("| Age:     %20s |" % record["age"])
    print("| Phone:   %20s |" % record["phone_number"])
    print("| Email:   %20s |" % record["email"])


@verbose_mode(verbose)
def display_phonebook(phone_book):
    """Print all records from phone book"""
    print("#########  Phone book  ##########")

    for number, record in enumerate(phone_book):
        display_record(number + 1, record)


def find_by_field(phone_book, field, field_value):
    """Allows to search by field name and value"""
    found = False
    for idx, el in enumerate(phone_book):
        if el[field] == field_value:
            display_record(idx, el)
            found = True
    if not found:
        display_error(f"Records with {field} '{field_value}' not found")


@verbose_mode(verbose)
def find_record_by_name(phone_book):
    user_input = get_input_str("Enter name: ", "name")
    find_by_field(phone_book, "name", user_input)


@verbose_mode(verbose)
def find_record_by_age(phone_book):
    user_input = get_input_int("Enter desired age: ")
    find_by_field(phone_book, "age", user_input)


@verbose_mode(verbose)
def find_record_by_email(phone_book):
    user_input = get_input_str("Enter email: ", "email")
    find_by_field(phone_book, "email", user_input)


def delete_by_field(phone_book, field, field_value):
    """Allows to delete record by field name and value"""
    copy_phonebook = phone_book[:]
    found = False
    for idx, el in enumerate(copy_phonebook):
        if el[field] == field_value:
            del phone_book[idx]
            found = True
    if not found:
        print(f"Records with {field} '{field_value}' not found")


@verbose_mode(verbose)
def delete_record_by_name(phone_book):
    input_name = get_input_str("Enter name: ", "name")
    delete_by_field(phone_book, "name", input_name)


@verbose_mode(verbose)
def delete_record_by_surname(phone_book):
    input_surname = get_input_str("Enter surname: ", "surname")
    delete_by_field(phone_book, "surname", input_surname)


@verbose_mode(verbose)
def add_record_to_phonebook(phone_book):
    """Add 1 record to phone book"""
    record = {
        "surname": get_input_str("Enter surname: ", "surname"),
        "name": get_input_str("Enter name: ", "name"),
        "age": get_input_int("Enter age: "),
        "phone_number": get_input_str("Enter phone num.: ", "phone_number"),
        "email": get_input_str("Enter email: ", "email"),
    }
    phone_book.append(record)


def display_error(message):
    print("ERROR: %s" % message)


@verbose_mode(verbose)
def count_all_entries_in_phonebook(phone_book):
    print("Total number of entries: ", len(phone_book))


@verbose_mode(verbose)
def display_phonebook_sorted_by_age(phone_book):
    sorted_by_age = sorted(phone_book, key=lambda field: field["age"])
    for number, entry in enumerate(sorted_by_age):
        display_record(number + 1, entry)


@verbose_mode(verbose)
def increase_age(phone_book):
    """Allows to increase age by entered value for each record in phone book"""
    number = get_input_int("Enter a number to increase the age: ")
    for record in phone_book:
        record.update((k, v + number) for k, v in record.items() if k == "age")


@verbose_mode(verbose)
def avr_age_of_all_persons(phone_book):
    print(round(sum(user["age"] for user in phone_book) / len(phone_book)))


@verbose_mode(verbose)
def save_to_file(file_name, phone_book):
    """Save current phonebook to file passed in parameter"""
    with open(file_name, "w", encoding="utf8") as f:
        json.dump(phone_book, f, indent=4)


@verbose_mode(verbose)
def load_from_file(file_name):
    """Load phonebook from file passed in parameter"""
    with open(file_name, "r") as f:
        phone_book = json.load(f)
        return phone_book


def prompt_to_save(file_name, phone_book):
    """Display prompt to save current phone book and save it"""
    choice = {"y": True, "n": False}
    print("Do you want to save changes? Press 'y' for saving and 'n' for break")
    user_choice = get_input_choice_menu(choice)
    if user_choice == "y":
        save_to_file(file_name, phone_book)


@verbose_mode(verbose)
def finish_program():
    exit()


def print_prompt():
    """Display available options"""
    options = [
        "~ Welcome to phonebook ~",
        "Select one of actions below:",
        "\t1 - Print phonebook entries",
        "\t2 - Print phonebook entries (by age)",
        "\t3 - Add new entry",
        "\t4 - Find entry by name",
        "\t5 - Find entry by age",
        "\t6 - Find entry by email",
        "\t7 - Delete entry by name",
        "\t8 - The number of entries in the phonebook",
        "\t9 - Avr. age of all persons",
        "\t10 - Increase age by num. of years",
        "-----------------------------",
        "\ts - Save to file",
        "\tl - Load from file",
        "\t0 - Exit",
    ]
    print("\n".join(options))


def main():
    parser = argparse.ArgumentParser(description="")

    parser.add_argument("filename", type=str, help="Path to file_name")
    parser.add_argument("verbose", type=bool, help="Display detailed processing info")

    args = parser.parse_args()

    global verbose
    verbose = args.verbose

    phone_book = []

    file_name = args.filename
    if not os.path.exists(file_name):
        raise FileExistsError(f"'{file_name}' not found. Check the file name and path.")

    while True:
        try:
            menu = {
                "1": display_phonebook,
                "2": display_phonebook_sorted_by_age,
                "3": add_record_to_phonebook,
                "4": find_record_by_name,
                "5": find_record_by_age,
                "6": find_record_by_email,
                "7": delete_record_by_name,
                "8": count_all_entries_in_phonebook,
                "9": avr_age_of_all_persons,
                "10": increase_age,
                "0": finish_program,
                "s": save_to_file,
                "l": load_from_file,
            }

            print_prompt()
            user_input = get_input_choice_menu(menu)

            match user_input:
                case "0":
                    prompt_to_save(file_name, phone_book)
                    menu[user_input]()
                case "l":
                    prompt_to_save(file_name, phone_book)
                    phone_book = load_from_file(file_name)
                    menu[user_input](file_name)
                case "s":
                    menu[user_input](file_name, phone_book)
                case _:
                    menu[user_input](phone_book)

        except Exception as ex:
            display_error("Something went wrong. Try again...")


if __name__ == "__main__":
    main()
