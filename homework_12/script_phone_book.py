import json

running = True
# global phone_book

# phone_book = [
#     {"name": "Nazar", "surname": "Nazarenko", "age": 50, "phone_number": "+18005550102"},
#     {"name": "Mariia", "surname": "Mariychuk", "age": 15, "phone_number": "+18505550112"},
# ]


def display_record(number, entry):
    print("--[ %s ]--------------------------" % number)
    print("| Surname: %20s |" % entry["surname"])
    print("| Name:    %20s |" % entry["name"])
    print("| Age:     %20s |" % entry["age"])
    print("| Phone:   %20s |" % entry["phone_number"])


def display_phonebook():
    print("#########  Phone book  ##########")

    for number, record in enumerate(phone_book):
        display_record(number + 1, record)


def get_input_str(option):
    """Get and check user input"""
    while True:
        user_input = input("Choose one of the options: ")

        if user_input in option:
            return user_input

        if not user_input:
            print("Invalid input! Input can't be empty")

        elif user_input not in option:
            print(
                f"Invalid input! Only {', '.join(map(str, option))} options are available"
            )


def find_by_field(field, field_value):
    for idx, el in enumerate(phone_book):
        if el[field] == field_value:
            display_record(idx, el)
            break
    else:
        display_error(f"Records with {field} '{field_value}' not found")


def find_record_by_name():
    user_input = input("Enter name: ")
    find_by_field("name", user_input)


def find_record_by_age():
    user_input = input("Enter age: ")
    find_by_field("age", user_input)


def delete_by_field(field, field_value):
    copy_phonebook = phone_book[:]
    for idx, el in enumerate(copy_phonebook):
        if el[field] == field_value:
            del phone_book[idx]


def delete_record_by_name():
    input_name = input("Enter name: ")
    delete_by_field("name", input_name)


def delete_record_by_surname():
    input_surname = input("Enter surname: ")
    delete_by_field("surname", input_surname)


def add_record_to_phonebook():
    surname = input("Enter surname: ")
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    phone_number = input("Enter phone num.: ")

    entry = {"surname": surname, "name": name, "age": age, "phone_number": phone_number}
    phone_book.append(entry)


def display_error(message):
    print("ERROR: %s" % message)


def display_info(message):
    print("INFO: %s" % message)


def count_all_entries_in_phonebook():
    print("Total number of entries: ", len(phone_book))


def display_phonebook_sorted_by_age():
    sorted_by_age = sorted(phone_book, key=lambda field: field["age"])
    for number, entry in enumerate(sorted_by_age):
        display_record(number + 1, entry)


def increase_age():
    # global phone_book
    number = int(input("Enter number for increase: "))
    for record in phone_book:
        record.update((k, v + number) for k, v in record.items() if k == "age")


def avr_age_of_all_persons():
    print(sum(user["age"] for user in phone_book) / len(phone_book))


def save_to_file():
    with open("phone_book.json", "w", encoding="utf8") as f:
        json.dump(phone_book, f, indent=4)


def load_from_file():
    with open("phone_book.json", 'r') as f:
        phone_book = json.load(f)
        return phone_book


def exit():
    global running
    running = False


def print_prompt():
    print("~ Welcome to phonebook ~")
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
    while running:
        try:
            menu = {
                '1': display_phonebook,
                '2': display_phonebook_sorted_by_age,
                '3': add_record_to_phonebook,
                '4': find_record_by_name,
                '5': find_record_by_age,
                '6': delete_record_by_name,
                '7': count_all_entries_in_phonebook,
                '8': avr_age_of_all_persons,
                '9': increase_age,

                '0': exit,
                's': save_to_file,
                'l': load_from_file,
            }

            print_prompt()
            user_input = get_input_str(menu)
            menu[user_input]()

        except Exception as ex:
            display_error("Something went wrong. Try again...")
        # menu = {
        #     '1': display_phonebook,
        #     '2': display_phonebook_sorted_by_age,
        #     '3': add_record_to_phonebook,
        #     '4': find_record_by_name,
        #     '5': find_record_by_age,
        #     '6': delete_record_by_name,
        #     '7': count_all_entries_in_phonebook,
        #     '8': avr_age_of_all_persons,
        #     '9': increase_age,
        #
        #     '0': exit,
        #     's': save_to_file,
        #     'l': load_from_file,
        # }
        #
        # print_prompt()
        # user_input = input("Choose one option: ")
        # menu[user_input]()


if __name__ == '__main__':
    main()
