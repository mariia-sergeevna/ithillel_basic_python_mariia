import json
import argparse
from copy import copy
from typing import Union

from utilities.wrapper import verbose_mode
from utilities.input import validate_age, validate_str, get_input_choice_menu, input_value, validate_filename
from utilities.field import Field


class Record:
    """
    A class representing a record in a phone book.

    Attributes:
        surname: The surname of the person in the record.
        name: The name of the person in the record.
        age: The age of the person in the record.
        phone_number: The phone number of the person in the record.
        email: The email address of the person in the record.
    """

    def __init__(
        self, surname: str, name: str, age: int, phone_number: str, email: str
    ) -> None:
        self.surname = surname
        self.name = name
        self.age = age
        self.phone_number = phone_number
        self.email = email

    def display_record(self, number: int) -> None:
        """
        Displays the record information in a formatted way.

        Args:
            number: The number of the record in the phone book.
        """
        print(f"--[ {number} ]----------------------------")
        print(f"|  Surname: {self.surname:>20}  |")
        print(f"|  Name:    {self.name:>20}  |")
        print(f"|  Age:     {self.age:>20}  |")
        print(f"|  Phone:   {self.phone_number:>20}  |")
        print(f"|  Email:   {self.email:>20}  |")

    def to_dict(self) -> dict:
        """Returns the record information in a dict form"""
        return {
            Field.SURNAME: self.surname,
            Field.NAME: self.name,
            Field.AGE: self.age,
            Field.PHONE_NUMBER: self.phone_number,
            Field.EMAIL: self.email,
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
        self.modified = False

    @verbose_mode
    def add_record_to_phonebook(self) -> None:
        """Add 1 record to phone book"""
        record = Record(
            surname=input_value("Enter surname: ", validate_str, Field.SURNAME),
            name=input_value("Enter name: ", validate_str, Field.NAME),
            age=input_value("Enter age: ", validate_age),
            phone_number=input_value("Enter phone num.: ", validate_str, Field.PHONE_NUMBER),
            email=input_value("Enter email: ", validate_str, Field.EMAIL),
        )
        self.records.append(record)
        self.modified = True

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
        user_input = input_value("Enter name: ", validate_str, Field.NAME)
        self.find_by_field(Field.NAME, user_input)

    @verbose_mode
    def find_record_by_age(self) -> None:
        user_input = input_value("Enter desired age: ", validate_age)
        self.find_by_field(Field.AGE, user_input)

    @verbose_mode
    def find_record_by_email(self) -> None:
        user_input = input_value("Enter email: ", validate_str, Field.EMAIL)
        self.find_by_field(Field.EMAIL, user_input)

    @verbose_mode
    def increase_age(self) -> None:
        """Allows to increase age by entered value for each record in phone book"""
        number = input_value("Enter a number to increase the age: ", validate_age)
        for record in self.records:
            record.age += number

        self.modified = True

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

        self.modified = True

    @verbose_mode
    def delete_record_by_name(self) -> None:
        input_name = input_value("Enter name: ", validate_str, Field.NAME)
        self.delete_by_field(Field.NAME, input_name)

    @verbose_mode
    def delete_record_by_surname(self) -> None:
        input_surname = input_value("Enter surname: ", validate_str, Field.SURNAME)
        self.delete_by_field(Field.SURNAME, input_surname)

    @verbose_mode
    def count_all_entries_in_phonebook(self) -> None:
        """Counts the number of entries in the phone book."""
        print("Total number of entries: ", len(self.records))

    @verbose_mode
    def avr_age_of_all_persons(self) -> None:
        """Calculates the average age of all the persons in the phone book."""
        print(round(sum(record.age for record in self.records) / len(self.records)))

    @verbose_mode
    def save_to_new_file(self, filename: str) -> None:
        """Saves the phone book to a file with the given filename."""
        filename = Menu.get_filename("save to", filename)
        self.save_to_file(filename)

    @verbose_mode
    def save_to_file(self, filename: str) -> None:
        """Saves the phone book to a file with the given filename."""
        serialized_phonebook = [record.to_dict() for record in self.records]
        with open(filename, "w", encoding="utf8") as f:
            json.dump(serialized_phonebook, f, indent=4)
        self.modified = False

    @verbose_mode
    def load_from_file(self, filename: str) -> None:
        """Loads the phone book from a file with the given filename."""
        filename = Menu.get_filename("load from", filename)
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

    @staticmethod
    def get_filename(action: str, filename: str) -> str:
        """Prompts the user for a filename for saving or loading."""
        if not filename:
            filename = input_value(f"Enter filename to {action}: ", validate_filename)
        else:
            choice = {"y": True, "n": False}
            print(f"Do you want to {action} current file or other? "
                  "Press 'y' for current file and 'n' for new file")
            user_choice = get_input_choice_menu(choice)
            if user_choice == "n":
                filename = input_value(f"Enter filename to {action}: ", validate_filename)

        return filename

    def prompt_to_save(self, phonebook) -> None:
        """Display prompt to save current phone book and save it"""
        choice = {"y": True, "n": False}
        print("Do you want to save changes? Press 'y' for saving and 'n' for break")
        user_choice = get_input_choice_menu(choice)
        if user_choice == "y":
            filename = self.get_filename("save to", self.filename)
            phonebook.save_to_file(filename)

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
                        if phonebook.modified:
                            self.prompt_to_save(phonebook)
                        menu[user_input]()
                    case "l":
                        if phonebook.modified:
                            self.prompt_to_save(phonebook)
                        phonebook.load_from_file(self.filename)
                    case "s":
                        phonebook.save_to_new_file(self.filename)
                    case _:
                        menu[user_input]()

            except Exception as ex:
                PhoneBook.display_error("Something went wrong. Try again...")


def main():
    parser = argparse.ArgumentParser(description="")

    parser.add_argument("filename", type=str, nargs="?", default=None, help="Path to file_name")
    parser.add_argument(
        "--verbose", action="store_true", help="Display detailed processing info"
    )

    args = parser.parse_args()

    if args.filename:
        validate_filename(args.filename)

    menu = Menu(args.filename, args.verbose)
    menu.run()


if __name__ == "__main__":
    main()
