import json
import os
import argparse
import re

from utilities.input import get_input_str, get_input_int, get_input_choice_menu
from utilities.wrapper import verbose_mode

verbose = False


class Record:
    def __init__(self, surname, name, age, phone_number, email):
        self.surname = surname
        self.name = name
        self.age = age
        self.phone_number = phone_number
        self.email = email

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, user_input):
        self._surname = self._validate_field("surname", user_input)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, user_input):
        self._name = self._validate_field("name", user_input)

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, user_input):
        self._age = self._validate_age(user_input)

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, user_input):
        self._phone_number = self._validate_field("phone_number", user_input)

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, user_input):
        self._email = self._validate_field("email", user_input)

    def _validate_age(self, user_input, lower_bound=1, upper_bound=99):
        """Get and check that user input age is valid."""
        while True:
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

            user_input = input()

    def _validate_field(self, field, user_input):
        if field == "surname" or field == "name":
            regex = r"[A-Za-z]+"
        elif field == "phone_number":
            regex = r"\+1\d{10}$"
        elif field == "email":
            regex = r"[\w.-]+@[A-Za-z]+\.[a-z]{2,}"
        else:
            raise ValueError("Isn't correct field")
        while True:
            if re.fullmatch(regex, user_input):
                return user_input
            else:
                print(f"Invalid input! Please, enter correct {field}.")
                user_input = input()

    def display_record(self, number):
        print("--[ %s ]--------------------------" % number)
        print("| Surname: %20s |" % self._surname)
        print("| Name:    %20s |" % self._name)
        print("| Age:     %20s |" % self._age)
        print("| Phone:   %20s |" % self._phone_number)
        print("| Email:   %20s |" % self._email)




class PhoneBook:
    def __init__(self, records=None):
        self.records = [] if not records else records

    # @verbose_mode(verbose)
    def display_phonebook(self):
        """Print all records from phone book"""
        print("#########  Phone book  ##########")

        for number, record in enumerate(self.records):
            record.display_record(number + 1)

    # @verbose_mode(verbose)
    def add_record_to_phonebook(self, surname, name, age, phone_number, email):
        """Add 1 record to phone book"""
        record = Record(surname, name, age, phone_number, email)
        self.records.append(record)


new_ph_book = PhoneBook()
new_ph_book.add_record_to_phonebook("testSurn", "tName", "10", "+18005550102", "mariia_8@gmail.com")
new_ph_book.display_phonebook()


class Menu:
    pass
#
#
# def display_record(number, record):
#     print("--[ %s ]--------------------------" % number)
#     print("| Surname: %20s |" % record["surname"])
#     print("| Name:    %20s |" % record["name"])
#     print("| Age:     %20s |" % record["age"])
#     print("| Phone:   %20s |" % record["phone_number"])
#     print("| Email:   %20s |" % record["email"])
#
#
# @verbose_mode(verbose)
# def display_phonebook(phone_book):
#     """Print all records from phone book"""
#     print("#########  Phone book  ##########")
#
#     for number, record in enumerate(phone_book):
#         display_record(number + 1, record)
#
#
# def find_by_field(phone_book, field, field_value):
#     """Allows to search by field name and value"""
#     found = False
#     for idx, el in enumerate(phone_book):
#         if el[field] == field_value:
#             display_record(idx, el)
#             found = True
#     if not found:
#         display_error(f"Records with {field} '{field_value}' not found")
#
#
# @verbose_mode(verbose)
# def find_record_by_name(phone_book):
#     user_input = get_input_str("Enter name: ", "name")
#     find_by_field(phone_book, "name", user_input)
#
#
# @verbose_mode(verbose)
# def find_record_by_age(phone_book):
#     user_input = get_input_int("Enter desired age: ")
#     find_by_field(phone_book, "age", user_input)
#
#
# @verbose_mode(verbose)
# def find_record_by_email(phone_book):
#     user_input = get_input_str("Enter email: ", "email")
#     find_by_field(phone_book, "email", user_input)
#
#
# def delete_by_field(phone_book, field, field_value):
#     """Allows to delete record by field name and value"""
#     copy_phonebook = phone_book[:]
#     found = False
#     for idx, el in enumerate(copy_phonebook):
#         if el[field] == field_value:
#             del phone_book[idx]
#             found = True
#     if not found:
#         print(f"Records with {field} '{field_value}' not found")
#
#
# @verbose_mode(verbose)
# def delete_record_by_name(phone_book):
#     input_name = get_input_str("Enter name: ", "name")
#     delete_by_field(phone_book, "name", input_name)
#
#
# @verbose_mode(verbose)
# def delete_record_by_surname(phone_book):
#     input_surname = get_input_str("Enter surname: ", "surname")
#     delete_by_field(phone_book, "surname", input_surname)
#
#
# @verbose_mode(verbose)
# def add_record_to_phonebook(phone_book):
#     """Add 1 record to phone book"""
#     record = {
#         "surname": get_input_str("Enter surname: ", "surname"),
#         "name": get_input_str("Enter name: ", "name"),
#         "age": get_input_int("Enter age: "),
#         "phone_number": get_input_str("Enter phone num.: ", "phone_number"),
#         "email": get_input_str("Enter email: ", "email"),
#     }
#     phone_book.append(record)
#
#
# def display_error(message):
#     print("ERROR: %s" % message)
#
#
# @verbose_mode(verbose)
# def count_all_entries_in_phonebook(phone_book):
#     print("Total number of entries: ", len(phone_book))
#
#
# @verbose_mode(verbose)
# def display_phonebook_sorted_by_age(phone_book):
#     sorted_by_age = sorted(phone_book, key=lambda field: field["age"])
#     for number, entry in enumerate(sorted_by_age):
#         display_record(number + 1, entry)
#
#
# @verbose_mode(verbose)
# def increase_age(phone_book):
#     """Allows to increase age by entered value for each record in phone book"""
#     number = get_input_int("Enter a number to increase the age: ")
#     for record in phone_book:
#         record.update((k, v + number) for k, v in record.items() if k == "age")
#
#
# @verbose_mode(verbose)
# def avr_age_of_all_persons(phone_book):
#     print(round(sum(user["age"] for user in phone_book) / len(phone_book)))
#
#
# @verbose_mode(verbose)
# def save_to_file(file_name, phone_book):
#     """Save current phonebook to file passed in parameter"""
#     with open(file_name, "w", encoding="utf8") as f:
#         json.dump(phone_book, f, indent=4)
#
#
# @verbose_mode(verbose)
# def load_from_file(file_name):
#     """Load phonebook from file passed in parameter"""
#     with open(file_name, "r") as f:
#         phone_book = json.load(f)
#         return phone_book
#
#
# def prompt_to_save(file_name, phone_book):
#     """Display prompt to save current phone book and save it"""
#     choice = {"y": True, "n": False}
#     print("Do you want to save changes? Press 'y' for saving and 'n' for break")
#     user_choice = get_input_choice_menu(choice)
#     if user_choice == "y":
#         save_to_file(file_name, phone_book)
#
#
# @verbose_mode(verbose)
# def finish_program():
#     exit()
#
#
# def print_prompt():
#     """Display available options"""
#     options = [
#         "~ Welcome to phonebook ~",
#         "Select one of actions below:",
#         "\t1 - Print phonebook entries",
#         "\t2 - Print phonebook entries (by age)",
#         "\t3 - Add new entry",
#         "\t4 - Find entry by name",
#         "\t5 - Find entry by age",
#         "\t6 - Find entry by email",
#         "\t7 - Delete entry by name",
#         "\t8 - The number of entries in the phonebook",
#         "\t9 - Avr. age of all persons",
#         "\t10 - Increase age by num. of years",
#         "-----------------------------",
#         "\ts - Save to file",
#         "\tl - Load from file",
#         "\t0 - Exit",
#     ]
#     print("\n".join(options))
#
#
# def main():
#     parser = argparse.ArgumentParser(description="")
#
#     parser.add_argument("filename", type=str, help="Path to file_name")
#     parser.add_argument("verbose", type=bool, help="Display detailed processing info")
#
#     args = parser.parse_args()
#
#     global verbose
#     verbose = args.verbose
#
#     phone_book = []
#
#     file_name = args.filename
#     if not os.path.exists(file_name):
#         raise FileExistsError(f"'{file_name}' not found. Check the file name and path.")
#
#     while True:
#         try:
#             menu = {
#                 "1": display_phonebook,
#                 "2": display_phonebook_sorted_by_age,
#                 "3": add_record_to_phonebook,
#                 "4": find_record_by_name,
#                 "5": find_record_by_age,
#                 "6": find_record_by_email,
#                 "7": delete_record_by_name,
#                 "8": count_all_entries_in_phonebook,
#                 "9": avr_age_of_all_persons,
#                 "10": increase_age,
#                 "0": finish_program,
#                 "s": save_to_file,
#                 "l": load_from_file,
#             }
#
#             print_prompt()
#             user_input = get_input_choice_menu(menu)
#
#             match user_input:
#                 case "0":
#                     prompt_to_save(file_name, phone_book)
#                     menu[user_input]()
#                 case "l":
#                     prompt_to_save(file_name, phone_book)
#                     phone_book = load_from_file(file_name)
#                     menu[user_input](file_name)
#                 case "s":
#                     menu[user_input](file_name, phone_book)
#                 case _:
#                     menu[user_input](phone_book)
#
#         except Exception as ex:
#             display_error("Something went wrong. Try again...")
#
#
# if __name__ == "__main__":
#     main()