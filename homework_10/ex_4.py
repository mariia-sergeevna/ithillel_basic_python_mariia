from random import randint


def user_pick():
    """Guess the number picked by user."""
    possible_nums = [i for i in range(1, 11)]
    lowest_idx = 0
    highest_idx = len(possible_nums) - 1
    answers = {
        "1": "Guessed number is greater",
        "2": "Guessed number is smaller",
        "3": "You guessed it! :)",
    }

    while lowest_idx <= highest_idx:
        middle_el = (lowest_idx + highest_idx) // 2
        guess_num = possible_nums[middle_el]
        print(f"Is your number {guess_num}?")
        result = get_str(answers)
        if result == "3":
            return middle_el
        if result == "2":
            highest_idx = middle_el - 1
        else:
            lowest_idx = middle_el + 1
    return None


def program_pick():
    """Guess the number picked by computer."""
    number = randint(1, 10)

    while True:
        number_input = get_integer()
        if number_input < number:
            print(f"Guessed number greater than {number_input}")
        elif number_input > number:
            print(f"Guessed number smaller than {number_input}")
        elif number_input == number:
            print(f"You guessed it! :) it's {number_input} ")
            break


def get_integer():
    """Get user input to guess the number."""
    while True:
        user_input = input("Your number: ")
        try:
            input_num = int(user_input)
            return input_num
        except ValueError:
            print("Invalid input! Please enter a numeric value")


def get_str(option: dict):
    """Get user input to select menu option"""
    while True:
        for k, v in option.items():
            print(f"{k} - {v}")

        user_input = input("Choose one of the options: ")

        if user_input not in option:
            print(
                f"Invalid input! Only {' and '.join(map(str, list(option.keys())))} options are available"
            )
        if user_input in option:
            return user_input


def main():
    while True:
        main_menu = {
            "1": "User picks the number for computer",
            "2": "Computer picks the number for user",
        }
        command = get_str(main_menu)
        match command:
            case "1":
                user_pick()

            case "2":
                program_pick()

        finish_menu = {
            "1": "Play again",
            "2": "Exit",
        }
        command = get_str(finish_menu)

        match command:
            case "1":
                continue

            case "2":
                exit()


if __name__ == "__main__":
    main()
