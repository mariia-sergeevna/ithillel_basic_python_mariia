import json
import os
import argparse

from utilities.input import get_input_str, get_input_int, get_input_choice_menu
from utilities.wrapper import display_status

verbose = False


# def display_status(func):
#     def wrapper(*args, **kwargs):
#         if verbose:
#             print("Starting handle your request...")
#         result = func(*args, **kwargs)
#         if verbose:
#             print("Request handled is finished.")
#         return result
#
#     return wrapper


def display_record(number, record):
    print("--[ %s ]--------------------------" % number)
    print("| Surname: %20s |" % record["surname"])
    print("| Name:    %20s |" % record["name"])
    print("| Age:     %20s |" % record["age"])
    print("| Phone:   %20s |" % record["phone_number"])
    print("| Email:   %20s |" % record["email"])


@display_status
def display_phonebook(phone_book):
    print("#########  Phone book  ##########")

    for number, record in enumerate(phone_book):
        display_record(number + 1, record)


# def get_input_int(prompt, lower_bound=1, upper_bound=99):
#     """Get and check user input age."""
#     while True:
#         user_input = input(prompt)
#         try:
#             input_age = int(user_input)
#
#             if input_age < lower_bound:
#                 print(f"Entered age should be greater than or equal to {lower_bound}")
#             elif input_age > upper_bound:
#                 print(f"Entered age should be smaller than or equal to {upper_bound}")
#             else:
#                 return input_age
#
#         except ValueError:
#             print(f"Invalid input! '{user_input}' is not an integer value!")
#
#
# def get_input_choice_menu(option):
#     """Get and check user input"""
#     while True:
#         user_input = input("Choose one of the options: ")
#
#         if user_input.lower() in option:
#             return user_input
#
#         elif not user_input:
#             print("Invalid input! Input can't be empty")
#
#         else:
#             print(
#                 f"Invalid input! Only {', '.join(map(str, option))} options are available"
#             )
#
#
# def get_input_str(prompt, field):
#     if field == "surname" or field == "name":
#         regex = r'[A-Za-z]+'
#     elif field == "phone_number":
#         regex = r'\+1\d{10}$'
#     else:
#         regex = r'[\w.-]+@[A-Za-z]+\.[a-z]{2,}'
#     while True:
#         user_input = input(prompt)
#         if re.fullmatch(regex, user_input):
#             return user_input
#         print(f"Invalid input! Please, enter correct {field}.")


def find_by_field(phone_book, field, field_value):
    found = False
    for idx, el in enumerate(phone_book):
        if el[field] == field_value:
            display_record(idx, el)
            found = True
    if not found:
        display_error(f"Records with {field} '{field_value}' not found")


@display_status
def find_record_by_name(phone_book):
    user_input = get_input_str("Enter name: ", "name")
    find_by_field(phone_book, "name", user_input)


@display_status
def find_record_by_age(phone_book):
    user_input = get_input_int("Enter desired age: ")
    find_by_field(phone_book, "age", user_input)


@display_status
def find_record_by_email(phone_book):
    user_input = get_input_str("Enter email: ", "email")
    find_by_field(phone_book, "email", user_input)


def delete_by_field(phone_book, field, field_value):
    copy_phonebook = phone_book[:]
    found = False
    for idx, el in enumerate(copy_phonebook):
        if el[field] == field_value:
            del phone_book[idx]
            found = True
    if not found:
        print(f"Records with {field} '{field_value}' not found")


@display_status
def delete_record_by_name(phone_book):
    input_name = get_input_str("Enter name: ", "name")
    delete_by_field(phone_book, "name", input_name)


@display_status
def delete_record_by_surname(phone_book):
    input_surname = get_input_str("Enter surname: ", "surname")
    delete_by_field(phone_book, "surname", input_surname)


@display_status
def add_record_to_phonebook(phone_book):
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


@display_status
def count_all_entries_in_phonebook(phone_book):
    print("Total number of entries: ", len(phone_book))


@display_status
def display_phonebook_sorted_by_age(phone_book):
    sorted_by_age = sorted(phone_book, key=lambda field: field["age"])
    for number, entry in enumerate(sorted_by_age):
        display_record(number + 1, entry)


@display_status
def increase_age(phone_book):
    number = get_input_int("Enter a number to increase the age: ")
    for record in phone_book:
        record.update((k, v + number) for k, v in record.items() if k == "age")


@display_status
def avr_age_of_all_persons(phone_book):
    print(round(sum(user["age"] for user in phone_book) / len(phone_book)))


@display_status
def save_to_file(file_name, phone_book):
    with open(file_name, "w", encoding="utf8") as f:
        json.dump(phone_book, f, indent=4)


@display_status
def load_from_file(file_name):
    with open(file_name, "r") as f:
        phone_book = json.load(f)
        return phone_book


def prompt_to_save(file_name, phone_book):
    choice = {"y": True, "n": False}
    print("Do you want to save changes? Press 'y' for saving and 'n' for break")
    user_choice = get_input_choice_menu(choice)
    if user_choice == "Y":
        save_to_file(file_name, phone_book)


@display_status
def finish_program():
    exit()


def print_prompt():
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
        "\t0 - Exit"
    ]
    print('\n'.join(options))


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
