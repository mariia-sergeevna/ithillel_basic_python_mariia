# from __future__ import absolute_import
import unittest

# from .. .app.main import Record
from main import Record


class SerializeTestCase(unittest.TestCase):

    def test_ok(self):
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

    # def test_with_negative_age(self):
    #     record = Record(surname="Doe", name="John", age=-20, phone_number="123456789", email="johndoe@example.com")
    #     expected_dict = {
    #         "surname": "Doe",
    #         "name": "John",
    #         "age": -20,
    #         "phone_number": "123456789",
    #         "email": "johndoe@example.com"
    #     }
    #     self.assertEqual(record.serialize(), expected_dict)


# class PhoneBookTestCase(unittest.TestCase):
#     pass


# class TestRecord(unittest.TestCase):
#     def test_properties(self):
#         record = Record("test", "Test", 18, "+18005550102", "nik@gmail.com")
#         self.assertEqual(record.surname, "Testov")
#         self.assertEqual(record.name, "Test")
#         self.assertEqual(record.age, 18)
#         self.assertEqual(record.phone_number, "+18005550102")
#         self.assertEqual(record.email, "nik@gmail.com")


# if __name__ == "__main__":
#     unittest.main()
