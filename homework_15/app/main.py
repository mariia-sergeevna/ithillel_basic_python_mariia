import json
import os
import argparse
import re
from copy import copy

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
        self._surname = self.validate_field("surname", user_input)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, user_input):
        self._name = self.validate_field("name", user_input)

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, user_input):
        self._age = self.validate_age(user_input)

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, user_input):
        self._phone_number = self.validate_field("phone_number", user_input)

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, user_input):
        self._email = self.validate_field("email", user_input)

    @staticmethod
    def validate_age(user_input, lower_bound=1, upper_bound=99):
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

    @staticmethod
    def validate_field(field, user_input):
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
    def add_record_to_phonebook(self, surname, name, age, phone_number, email):
        """Add 1 record to phone book"""
        record = Record(surname, name, age, phone_number, email)
        self.records.append(record)

    # @verbose_mode(verbose)
    def display_phonebook(self):
        """Print all records from phone book"""
        print("#########  Phone book  ##########")

        for number, record in enumerate(self.records):
            record.display_record(number + 1)

    # @verbose_mode(verbose)
    def display_phonebook_sorted_by_age(self):
        self.records = sorted(self.records, key=lambda record: record.age)
        self.display_phonebook()

    @staticmethod
    def display_error(message):
        print("ERROR: %s" % message)

    def find_by_field(self, field, field_value):
        """Allows to search by field name and value"""
        found = False
        for idx, record in enumerate(self.records):
            if getattr(record, field) == field_value:
                record.display_record(idx)
                found = True
        if not found:
            self.display_error(f"Records with {field} '{field_value}' not found")

    # @verbose_mode(verbose)
    def find_record_by_name(self, value):
        user_input = Record.validate_field("name", value)
        self.find_by_field("name", user_input)

    # @verbose_mode(verbose)
    def find_record_by_age(self, value):
        user_input = Record.validate_age(value)
        self.find_by_field("age", user_input)

    def find_record_by_email(self, value):
        user_input = Record.validate_field("email", value)
        self.find_by_field("email", user_input)

    # @verbose_mode(verbose)
    def increase_age(self):
        """Allows to increase age by entered value for each record in phone book"""
        number = Record.validate_age(input("enter value: "))
        for record in self.records:
            record.age += number

    def delete_by_field(self, field, field_value):
        """Allows to delete record by field name and value"""
        # copy_phonebook = copy(self.records)
        found = False
        for record in copy(self.records):
            if getattr(record, field) == field_value:
                self.records.remove(record)
                found = True
        if not found:
            print(f"Records with {field} '{field_value}' not found")


    # @verbose_mode(verbose)
    def delete_record_by_name(self, value):
        input_name = Record.validate_field("name", value)
        self.delete_by_field("name", input_name)


    # @verbose_mode(verbose)
    def delete_record_by_surname(self, value):
        input_surname = Record.validate_field("surname", value)
        self.delete_by_field("surname", input_surname)

    # @verbose_mode(verbose)
    def count_all_entries_in_phonebook(self):
        print("Total number of entries: ", len(self.records))


    # @verbose_mode(verbose)
    def avr_age_of_all_persons(self):
        print(round(sum(record.age for record in self.records) / len(self.records)))


class Menu:
    def __init__(self, filename, verbose):
        self.filename = filename
        self.verbose = verbose

    def run(self):
        phonebook = PhoneBook()
        phonebook.add_record_to_phonebook("testSurn", "tName", "10", "+18005550102", "mariia_8@gmail.com")
        while True:
            try:
                menu = {
                    "1": PhoneBook.display_phonebook,
                    "2": PhoneBook.display_phonebook_sorted_by_age,
                    "3": PhoneBook.add_record_to_phonebook,
                    "4": PhoneBook.find_record_by_name,
                    "5": PhoneBook.find_record_by_age,
                    "6": PhoneBook.find_record_by_email,
                    "7": PhoneBook.delete_record_by_name,
                    "8": PhoneBook.count_all_entries_in_phonebook,
                    "9": PhoneBook.avr_age_of_all_persons,
                    "10": PhoneBook.increase_age,
                    # "0": finish_program,
                    # "s": save_to_file,
                    # "l": load_from_file,
                }

                # print_prompt()
                # user_input = get_input_choice_menu(menu)
                user_input = input("choice menu: ")

                match user_input:
                    # case "0":
                    #     prompt_to_save(file_name, phone_book)
                    #     menu[user_input]()
                    # case "l":
                    #     prompt_to_save(file_name, phone_book)
                    #     phone_book = load_from_file(file_name)
                    #     menu[user_input](file_name)
                    case "s":
                        menu[user_input]()
                    case _:
                        print("i'm here")
                        menu[user_input](phonebook)

            except Exception as ex:
                PhoneBook.display_error("Something went wrong. Try again...")


def main():
    parser = argparse.ArgumentParser(description="")

    parser.add_argument("filename", type=str, help="Path to file_name")
    parser.add_argument("verbose", type=bool, help="Display detailed processing info")

    args = parser.parse_args()
    if not os.path.exists(args.filename):
        raise FileExistsError(f"'{args.filename}' not found. Check the file name and path.")

    menu = Menu(args.filename, args.verbose)
    menu.run()

new_ph_book = PhoneBook()
new_ph_book.add_record_to_phonebook("testSurn", "tName", "10", "+18005550102", "mariia_8@gmail.com")
new_ph_book.add_record_to_phonebook("NewTest", "newName", "20", "+18005550103", "pavlo9@gmail.com")
# new_ph_book.display_phonebook()
print("________")
# new_ph_book.find_record_by_name("newName")
# new_ph_book.find_record_by_age("10")
# new_ph_book.find_record_by_email("mariia_8@gmail.com")
# new_ph_book.increase_age(10)
# new_ph_book.delete_record_by_name("tName")
# new_ph_book.delete_record_by_surname("NewTest")
# new_ph_book.display_phonebook()
new_ph_book.display_phonebook_sorted_by_age()
new_ph_book.count_all_entries_in_phonebook()
new_ph_book.avr_age_of_all_persons()


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
if __name__ == "__main__":
    main()
