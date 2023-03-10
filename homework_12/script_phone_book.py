import json
import os
import argparse


verbose = False


def display_status(func):
    def wrapper(*args, **kwargs):
        if verbose:
            print("Starting handle your request...")
        func(*args, **kwargs)
        if verbose:
            print("Request handled is finished.")
        return func

    return wrapper


def display_record(number, entry):
    print("--[ %s ]--------------------------" % number)
    print("| Surname: %20s |" % entry["surname"])
    print("| Name:    %20s |" % entry["name"])
    print("| Age:     %20s |" % entry["age"])
    print("| Phone:   %20s |" % entry["phone_number"])
    print("| Email:   %20s |" % entry["email"])


@display_status
def display_phonebook(phone_book):
    print("#########  Phone book  ##########")

    print(phone_book)
    for number, record in enumerate(phone_book):
        display_record(number + 1, record)


def get_input_int(lower_bound=18, upper_bound=105):
    """Get and check user input age."""
    while True:
        user_input = input("Enter age: ")
        try:
            input_age = int(user_input)

            if input_age < lower_bound:
                print(f"Entered age should be greater than or equal to {lower_bound}")
            elif input_age > upper_bound:
                print(f"Entered age should be smaller than or equal to {upper_bound}")
            else:
                return input_age

        except ValueError:
            print(f"Invalid input! '{user_input}' is not a integer value!")


def get_input_str(option):
    """Get and check user input"""
    while True:
        user_input = input("Choose one of the options: ")

        if user_input in option:
            return user_input

        elif not user_input:
            print("Invalid input! Input can't be empty")

        else:
            print(
                f"Invalid input! Only {', '.join(map(str, option))} options are available"
            )


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
    user_input = input("Enter name: ")
    find_by_field(phone_book, "name", user_input)


@display_status
def find_record_by_age(phone_book):
    user_input = get_input_int()
    find_by_field(phone_book, "age", user_input)


def delete_by_field(phone_book, field, field_value):
    copy_phonebook = phone_book[:]
    for idx, el in enumerate(copy_phonebook):
        if el[field] == field_value:
            del phone_book[idx]


@display_status
def delete_record_by_name(phone_book):
    input_name = input("Enter name: ")
    delete_by_field(phone_book, "name", input_name)


@display_status
def delete_record_by_surname(phone_book):
    input_surname = input("Enter surname: ")
    delete_by_field(phone_book, "surname", input_surname)


@display_status
def add_record_to_phonebook(phone_book):
    surname = input("Enter surname: ")
    name = input("Enter name: ")
    # age = int(input("Enter age: "))
    phone_number = input("Enter phone num.: ")
    email = input("Enter email: ")

    entry = {
        "surname": surname,
        "name": name,
        "age": get_input_int(),
        "phone_number": phone_number,
        "email": email,
    }
    phone_book.append(entry)


def display_error(message):
    print("ERROR: %s" % message)

# def display_info(message):
#     print("INFO: %s" % message)


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
    number = int(input("Enter number to increase age: "))
    for record in phone_book:
        record.update((k, v + number) for k, v in record.items() if k == "age")


@display_status
def avr_age_of_all_persons(phone_book):
    print(sum(user["age"] for user in phone_book) / len(phone_book))


@display_status
def save_to_file(file_name, phone_book):
    with open(file_name, "w", encoding="utf8") as f:
        json.dump(phone_book, f, indent=4)


@display_status
def load_from_file(file_name):
    with open(file_name, "r") as f:
        phone_book = json.load(f)
        print(phone_book)
        return phone_book


def prompt_to_save(file_name, phone_book):
    choice = {"Y": True, "N": False}
    print("Do you want to save changes? Press 'Y' for saving and 'N' for break")
    user_choice = get_input_str(choice)
    if user_choice == "Y":
        save_to_file(file_name, phone_book)


@display_status
def finish_program():
    exit()


def print_prompt():
    print("\n~ Welcome to phonebook ~")
    print("Select one of actions below:")
    print("\t1 - Print phonebook entries")
    print("\t2 - Print phonebook entries (by age)")
    print("\t3 - Add new entry")
    print("\t4 - Find entry by name")
    print("\t5 - Find entry by age")
    print("\t6 - Delete entry by name")
    print("\t7 - The number of entries in the phonebook")
    print("\t8 - Avr. age of all persons")
    print("\t9 - Increase age by num. of years")
    print("-----------------------------")
    print("\ts - Save to file")
    print("\tl - Load from file")
    print("\t0 - Exit")


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
        raise FileExistsError(f"{file_name} not exist!")

    # while True:
    #     try:
    #         menu = {
    #             "1": display_phonebook,
    #             "2": display_phonebook_sorted_by_age,
    #             "3": add_record_to_phonebook,
    #             "4": find_record_by_name,
    #             "5": find_record_by_age,
    #             "6": delete_record_by_name,
    #             "7": count_all_entries_in_phonebook,
    #             "8": avr_age_of_all_persons,
    #             "9": increase_age,
    #             "0": finish_program,
    #             "s": save_to_file,
    #             "l": load_from_file,
    #         }
    #
    #         print_prompt()
    #         user_input = get_input_str(menu)
    #
    #         match user_input:
    #             case "0", "l":
    #                 prompt_to_save(file_name, phone_book)
    #                 menu[user_input]()
    #             case "l":
    #                 phone_book = load_from_file()
    #             case _:
    #                 menu[user_input](phone_book)
    #
    #     except Exception as ex:
    #         display_error("Something went wrong. Try again...")
    while True:
        menu = {
            "1": display_phonebook,
            "2": display_phonebook_sorted_by_age,
            "3": add_record_to_phonebook,
            "4": find_record_by_name,
            "5": find_record_by_age,
            "6": delete_record_by_name,
            "7": count_all_entries_in_phonebook,
            "8": avr_age_of_all_persons,
            "9": increase_age,
            "0": finish_program,
            "s": save_to_file,
            "l": load_from_file,
        }

        print_prompt()
        user_input = get_input_str(menu)

        match user_input:
            case "0", "l":
                prompt_to_save(file_name, phone_book)
                menu[user_input]()
            case "l":
                phone_book = load_from_file(file_name)
                print(phone_book, "switch c")
            case "s":
                menu[user_input](file_name, phone_book)
            case _:
                menu[user_input](phone_book)


if __name__ == "__main__":
    main()
