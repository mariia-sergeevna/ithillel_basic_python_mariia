from secrets import choice
from string import ascii_letters, digits


def generate_password(amount_characters: int) -> str:
    valid_characters = ascii_letters + digits + "_"
    while True:
        password = "".join(choice(valid_characters) for _ in range(amount_characters))

        if (
            any(character.islower() for character in password)
            and any(character.isupper() for character in password)
            and any(character.isdigit() for character in password)
            and all(
                password[idx - 1] != password[idx] for idx in range(1, len(password))
            )
        ):
            break
    return password


def get_user_input():
    while True:
        user_input = input("Enter length of password: ")
        try:
            input_amount = int(user_input)

            if input_amount >= 8:
                return input_amount
            else:
                print("Length of password must be minimum 8")

        except ValueError:
            print("Invalid input! Please enter a numeric value")


def main() -> None:
    user_input = get_user_input()

    gen_password = generate_password(user_input)
    print(f"Your generate password:\n{gen_password}")


if __name__ == "__main__":
    main()
