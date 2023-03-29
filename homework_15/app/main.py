import json
import os
import argparse
from copy import copy
from functools import wraps

from utilities.input import validate_age, validate_str, get_input_choice_menu


class Record:
    def __init__(self, surname, name, age, phone_number, email):
        self._surname = surname
        self._name = name
        self._age = age
        self._phone_number = phone_number
        self._email = email

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, user_input):
        self._surname = validate_str("surname", user_input)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, user_input):
        self._name = validate_str("name", user_input)

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, user_input):
        self._age = validate_age(user_input)

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, user_input):
        self._phone_number = validate_str("phone_number", user_input)

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, user_input):
        self._email = validate_str("email", user_input)

    def display_record(self, number):
        print("--[ %s ]--------------------------" % number)
        print("| Surname: %20s |" % self.surname)
        print("| Name:    %20s |" % self.name)
        print("| Age:     %20s |" % self.age)
        print("| Phone:   %20s |" % self.phone_number)
        print("| Email:   %20s |" % self.email)

    def serialize(self):
        return {
            "surname": self._surname,
            "name": self._name,
            "age": self._age,
            "phone_number": self._phone_number,
            "email": self._email
        }


class PhoneBook:

    def __init__(self, records=None, verbose=False):
        self.records = [] if not records else records
        self.verbose = verbose

    @staticmethod
    def verbose_mode():
        def wrapper(func):
            @wraps(func)
            def display_status(*args, **kwargs):
                self = args[0]
                if self.verbose:
                    print("Starting handle your request...")
                func_result = func(*args, **kwargs)
                if self.verbose:
                    print("Request handled is finished.")
                return func_result
            return display_status
        return wrapper

    @verbose_mode()
    def add_record_to_phonebook(self):
        """Add 1 record to phone book"""
        record = Record(
            surname=validate_str("Enter surname: ", "surname"),
            name=validate_str("Enter name: ", "name"),
            age=validate_age("Enter age: "),
            phone_number=validate_str("Enter phone num.: ", "phone_number"),
            email=validate_str("Enter email: ", "email")
        )
        self.records.append(record)

    # @staticmethod
    @verbose_mode()
    def display_phonebook(self, sorted_records=None):
        """Print all records from phone book"""
        print("#########  Phone book  ##########")
        records = sorted_records if sorted_records else self.records

        for number, record in enumerate(records):
            record.display_record(number + 1)

    @verbose_mode()
    def display_phonebook_sorted_by_age(self):
        sorted_records = sorted(self.records, key=lambda entry: entry.age)
        for number, record in enumerate(sorted_records):
            record.display_record(number + 1)

    @staticmethod
    def display_error(message):
        print("ERROR: %s" % message)

    def find_by_field(self, field, field_value):
        """Allows to search by field name and value"""
        for idx, record in enumerate(self.records):
            if getattr(record, field) == field_value:
                record.display_record(idx)
                return
        self.display_error(f"Records with {field} '{field_value}' not found")

    @verbose_mode()
    def find_record_by_name(self):
        user_input = validate_str("Enter name: ", "name")
        self.find_by_field("name", user_input)

    @verbose_mode()
    def find_record_by_age(self):
        user_input = validate_age("Enter desired age: ")
        self.find_by_field("age", user_input)

    @verbose_mode()
    def find_record_by_email(self):
        user_input = validate_str("Enter email: ", "email")
        self.find_by_field("email", user_input)

    @verbose_mode()
    def increase_age(self):
        """Allows to increase age by entered value for each record in phone book"""
        number = validate_age("Enter a number to increase the age: ")
        for record in self.records:
            record.age += number

    @verbose_mode()
    def delete_by_field(self, field, field_value):
        """Allows to delete record by field name and value"""
        found = False
        for record in copy(self.records):
            if getattr(record, field) == field_value:
                self.records.remove(record)
                found = True
        if not found:
            print(f"Records with {field} '{field_value}' not found")

    @verbose_mode()
    def delete_record_by_name(self):
        input_name = validate_str("Enter name: ", "name")
        self.delete_by_field("name", input_name)

    @verbose_mode()
    def delete_record_by_surname(self):
        input_surname = validate_str("Enter surname: ", "surname")
        self.delete_by_field("surname", input_surname)

    @verbose_mode()
    def count_all_entries_in_phonebook(self):
        print("Total number of entries: ", len(self.records))

    @verbose_mode()
    def avr_age_of_all_persons(self):
        print(round(sum(record.age for record in self.records) / len(self.records)))

    @verbose_mode()
    def save_to_file(self, filename):
        """Save current phonebook to file passed in parameter"""
        serialized_phonebook = [record.serialize() for record in self.records]
        with open(filename, "w", encoding="utf8") as f:
            json.dump(serialized_phonebook, f, indent=4)

    @verbose_mode()
    def load_from_file(self, filename):
        """Load phonebook from file passed in parameter"""
        with open(filename, "r") as f:
            load_data = json.load(f)
            records = [Record(**record_data) for record_data in load_data]
            self.records = records


class Menu:
    def __init__(self, filename, verbose):
        self.filename = filename
        self.verbose = verbose

    @staticmethod
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
            "\t8 - Delete entry by surname",
            "\t9 - The number of entries in the phonebook",
            "\t10 - Avr. age of all persons",
            "\t11 - Increase age by num. of years",
            "-----------------------------",
            "\ts - Save to file",
            "\tl - Load from file",
            "\t0 - Exit",
        ]
        print("\n".join(options))

    def prompt_to_save(self, phonebook):
        """Display prompt to save current phone book and save it"""
        choice = {"y": True, "n": False}
        print("Do you want to save changes? Press 'y' for saving and 'n' for break")
        user_choice = get_input_choice_menu(choice)
        if user_choice == "y":
            phonebook.save_to_file(self.filename)

    @staticmethod
    def finish_program():
        exit()

    def run(self):
        phonebook = PhoneBook(verbose=self.verbose)
        # phonebook.add_record_to_phonebook("testSurn", "tName", "10", "+18005550102", "mariia_8@gmail.com")

        # while True:
        #     try:
        #         menu = {
        #             "1": PhoneBook.display_phonebook,
        #             "2": PhoneBook.display_phonebook_sorted_by_age,
        #             "3": PhoneBook.add_record_to_phonebook,
        #             "4": PhoneBook.find_record_by_name,
        #             "5": PhoneBook.find_record_by_age,
        #             "6": PhoneBook.find_record_by_email,
        #             "7": PhoneBook.delete_record_by_name,
        #             "8": PhoneBook.count_all_entries_in_phonebook,
        #             "9": PhoneBook.avr_age_of_all_persons,
        #             "10": PhoneBook.increase_age,
        #             "0": self.finish_program,
        #             "s": self.save_to_file,
        #             "l": self.load_from_file,
        #         }
        #
        #         self.print_prompt()
        #         user_input = get_input_choice_menu(menu)
        #         # user_input = input("choice menu: ")
        #
        #         match user_input:
        #             case "0":
        #                 self.prompt_to_save(phonebook)
        #                 menu[user_input]()
        #             case "l":
        #                 self.prompt_to_save(phonebook)
        #                 phonebook = self.load_from_file(self.filename)
        #                 menu[user_input](self.filename)
        #             case "s":
        #                 menu[user_input]()
        #             case _:
        #                 # print("i'm here")
        #                 menu[user_input](phonebook)
        #
        #     except Exception as ex:
        #         PhoneBook.display_error("Something went wrong. Try again...")
        while True:
            menu = {
                "1": phonebook.display_phonebook,
                "2": phonebook.display_phonebook_sorted_by_age,
                "3": phonebook.add_record_to_phonebook,
                "4": phonebook.find_record_by_name,
                "5": phonebook.find_record_by_age,
                "6": phonebook.find_record_by_email,
                "7": phonebook.delete_record_by_name,
                "8": phonebook.delete_record_by_surname,
                "9": phonebook.count_all_entries_in_phonebook,
                "10": phonebook.avr_age_of_all_persons,
                "11": phonebook.increase_age,
                "0": self.finish_program,
                "s": phonebook.save_to_file,
                "l": phonebook.load_from_file,
            }

            self.print_prompt()
            user_input = get_input_choice_menu(menu)

            match user_input:
                case "1":
                    menu[user_input](phonebook.records)
                case "0":
                    self.prompt_to_save(phonebook)
                    menu[user_input]()
                case "l":
                    self.prompt_to_save(phonebook)
                    phonebook.load_from_file(self.filename)
                case "s":
                    phonebook.save_to_file(self.filename)
                case _:
                    menu[user_input]()


def main():
    parser = argparse.ArgumentParser(description="")

    parser.add_argument("filename", type=str, help="Path to file_name")
    parser.add_argument("verbose", type=bool, help="Display detailed processing info")

    args = parser.parse_args()
    if not os.path.exists(args.filename):
        raise FileExistsError(f"'{args.filename}' not found. Check the file name and path.")

    menu = Menu(args.filename, args.verbose)
    menu.run()


if __name__ == "__main__":
    main()
