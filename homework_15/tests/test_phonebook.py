import unittest
from unittest.mock import patch

from main import Record, PhoneBook


class PropertiesTestCase(unittest.TestCase):
    """Test case for testing the properties of the Record class."""

    def test_properties(self):
        """Test that the properties of the Record class are correctly set."""
        record = Record("Testov", "Test", 20, "+18005550102", "nik@gmail.com")
        self.assertEqual(record.surname, "Testov")
        self.assertEqual(record.name, "Test")
        self.assertEqual(record.age, 20)
        self.assertEqual(record.phone_number, "+18005550102")
        self.assertEqual(record.email, "nik@gmail.com")


class SerializeTestCase(unittest.TestCase):
    """Test case for testing the serialization of the Record class."""

    def test_ok(self):
        """Test that the serialization of a Record object returns a dict with class attributes."""
        record = Record("Petrov", "Nik", 25, "+18005550102", "nik@gmail.com")
        expected_result = {
            "surname": "Petrov",
            "name": "Nik",
            "age": 25,
            "phone_number": "+18005550102",
            "email": "nik@gmail.com"
        }
        text_error = "Result after serialize must be dict with class attributes"
        self.assertEqual(record.serialize(), expected_result, text_error)


class DeleteTestCase(unittest.TestCase):
    """Test case for testing the deletion of records in the PhoneBook class."""

    def test_delete_one_record(self):
        """Test that deleting a record from a PhoneBook object removes it from the list of records."""
        records = [
            Record("Ivanov", "Ivan", 30, "+18005550112", "van@test.com"),
            Record("Petrov", "Petr", 25, "+18005550105", "petr@test.com")
        ]
        with patch('builtins.input', return_value="Ivan"):
            phone_book = PhoneBook(records=records)
            phone_book.delete_record_by_name()
            self.assertEqual(len(phone_book.records), 1)
            self.assertEqual(phone_book.records[0].surname, "Petrov")
