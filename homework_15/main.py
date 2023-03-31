import json
import os
import argparse
from copy import copy
from typing import Union, Callable, Any

from utilities.wrapper import verbose_mode
from utilities.input import validate_age, validate_str, get_input_choice_menu
from utilities.field import Field


class Record:
    """
    A class representing a record in a phone book.

    Attributes:
        _surname: The surname of the person in the record.
        _name: The name of the person in the record.
        _age: The age of the person in the record.
        _phone_number: The phone number of the person in the record.
        _email: The email address of the person in the record.
    """

    def __init__(
        self, surname: str, name: str, age: int, phone_number: str, email: str
    ) -> None:
        self._surname = surname
        self._name = name
        self._age = age
        self._phone_number = phone_number
        self._email = email

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, user_input: str):
        self._surname = validate_str(Field.SURNAME, user_input)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, user_input: str):
        self._name = validate_str(Field.NAME, user_input)

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, user_input: int):
        self._age = validate_age(user_input)

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, user_input: str):
        self._phone_number = validate_str(Field.PHONE_NUMBER, user_input)

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, user_input: str):
        self._email = validate_str(Field.EMAIL, user_input)

    def display_record(self, number: int) -> None:
        """
        Displays the record information in a formatted way.

        Args:
            number: The number of the record in the phone book.
        """
        print(f"--[ {number} ]----------------------------")
        print(f"|  Surname: {self._surname:>20}  |")
        print(f"|  Name:    {self._name:>20}  |")
        print(f"|  Age:     {self._age:>20}  |")
        print(f"|  Phone:   {self._phone_number:>20}  |")
        print(f"|  Email:   {self._email:>20}  |")

    def to_dict(self) -> dict:
        """Returns the record information in a dict form"""
        return {
            "surname": self.surname,
            "name": self.name,
            "age": self.age,
            "phone_number": self.phone_number,
            "email": self.email,
        }


class PhoneBook:
    """
    A class that represents a phone book.

    Attributes:
        records: A list of records in the phone book. Defaults to an empty list if not provided.
        verbose: A flag that controls the verbose mode. When set to True, the class prints the status
                    of the function execution. Defaults to False if not provided.
    """

    def __init__(
        self, records: Union[list, None] = None, verbose: bool = False
    ) -> None:
        self.records = [] if not records else records
        self.verbose = verbose

    @verbose_mode
    def add_record_to_phonebook(self) -> None:
        """Add 1 record to phone book"""
        record = Record(
            surname=validate_str("Enter surname: ", "surname"),
            name=validate_str("Enter name: ", "name"),
            age=validate_age("Enter age: "),
            phone_number=validate_str("Enter phone num.: ", "phone_number"),
            email=validate_str("Enter email: ", "email"),
        )
        self.records.append(record)

    @verbose_mode
    def display_phonebook(self, sorted_records=None) -> None:
        """Print all records from phone book"""
        print("#########  Phone book  ##########")
        records = sorted_records if sorted_records else self.records

        for number, record in enumerate(records):
            record.display_record(number + 1)

    @verbose_mode
    def display_phonebook_sorted_by_age(self) -> None:
        """
        Displays all the records in the phone book sorted by age in ascending order.
        """
        sorted_records = sorted(self.records, key=lambda entry: entry.age)
        self.display_phonebook(sorted_records=sorted_records)

    @staticmethod
    def display_error(message):
        print("ERROR: %s" % message)

    def find_by_field(self, field: str, field_value: str) -> None:
        """Allows to search by field name and value"""
        for idx, record in enumerate(self.records):
            if getattr(record, field) == field_value:
                record.display_record(idx)
                return
        self.display_error(f"Records with {field} '{field_value}' not found")

    @verbose_mode
    def find_record_by_name(self) -> None:
        user_input = validate_str("Enter name: ", "name")
        self.find_by_field("name", user_input)

    @verbose_mode
    def find_record_by_age(self) -> None:
        user_input = validate_age("Enter desired age: ")
        self.find_by_field("age", user_input)

    @verbose_mode
    def find_record_by_email(self) -> None:
        user_input = validate_str("Enter email: ", "email")
        self.find_by_field("email", user_input)

    @verbose_mode
    def increase_age(self) -> None:
        """Allows to increase age by entered value for each record in phone book"""
        number = validate_age("Enter a number to increase the age: ")
        for record in self.records:
            record._age += number

    @verbose_mode
    def delete_by_field(self, field, field_value) -> None:
        """Allows to delete record by field name and value"""
        found = False
        for record in copy(self.records):
            if getattr(record, field) == field_value:
                self.records.remove(record)
                found = True
        if not found:
            print(f"Records with {field} '{field_value}' not found")

    @verbose_mode
    def delete_record_by_name(self) -> None:
        input_name = validate_str("Enter name: ", "name")
        self.delete_by_field("name", input_name)

    @verbose_mode
    def delete_record_by_surname(self) -> None:
        input_surname = validate_str("Enter surname: ", "surname")
        self.delete_by_field("surname", input_surname)

    @verbose_mode
    def count_all_entries_in_phonebook(self) -> None:
        """Counts the number of entries in the phone book."""
        print("Total number of entries: ", len(self.records))

    @verbose_mode
    def avr_age_of_all_persons(self) -> None:
        """Calculates the average age of all the persons in the phone book."""
        print(round(sum(record.age for record in self.records) / len(self.records)))

    @verbose_mode
    def save_to_file(self, filename: str) -> None:
        """Saves the phone book to a file with the given filename."""
        serialized_phonebook = [record.to_dict() for record in self.records]
        with open(filename, "w", encoding="utf8") as f:
            json.dump(serialized_phonebook, f, indent=4)

    @verbose_mode
    def load_from_file(self, filename: str) -> None:
        """Loads the phone book from a file with the given filename."""
        with open(filename, "r") as f:
            load_data = json.load(f)
            records = [Record(**record_data) for record_data in load_data]
            self.records = records


class Menu:
    """
    A class that represents the main menu of the phone book application.

    Attributes:
        filename: The name of the file to save/load the phone book data.
        verbose: A flag to indicate if the application should display additional information.
    """

    def __init__(self, filename: str, verbose: bool) -> None:
        self.filename = filename
        self.verbose = verbose

    @staticmethod
    def print_prompt():
        """Display the available options in the main menu."""
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

    def prompt_to_save(self, phonebook) -> None:
        """Display prompt to save current phone book and save it"""
        choice = {"y": True, "n": False}
        print("Do you want to save changes? Press 'y' for saving and 'n' for break")
        user_choice = get_input_choice_menu(choice)
        if user_choice == "y":
            phonebook.save_to_file(self.filename)

    @staticmethod
    def finish_program() -> None:
        """Exit the application"""
        exit()

    def run(self) -> None:
        """Run the phone book application menu"""
        phonebook = PhoneBook(verbose=self.verbose)

        while True:
            try:
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

            except Exception as ex:
                PhoneBook.display_error("Something went wrong. Try again...")


def main():
    parser = argparse.ArgumentParser(description="")

    parser.add_argument("filename", type=str, help="Path to file_name")
    parser.add_argument(
        "--verbose", action="store_true", help="Display detailed processing info"
    )

    args = parser.parse_args()
    if not os.path.exists(args.filename):
        raise FileExistsError(
            f"'{args.filename}' not found. Check the file name and path."
        )

    menu = Menu(args.filename, args.verbose)
    menu.run()


if __name__ == "__main__":
    main()
