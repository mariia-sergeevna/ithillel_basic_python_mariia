from enum import Enum


class Field(str, Enum):
    SURNAME = "surname"
    NAME = "name"
    AGE = "age"
    EMAIL = "email"
    PHONE_NUMBER = "phone_number"
