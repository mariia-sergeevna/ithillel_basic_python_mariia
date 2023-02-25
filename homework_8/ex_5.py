def get_max_digit_with_str(number: int) -> int:
    return max(str(number))


def get_max_digit_without_str(number: int) -> int:
    num = 0
    while number >= 1:
        if number % 10 > num:
            num = number % 10
        number = number // 10
    return num


def main() -> None:
    user_input = int(input("Enter number for find biggest digit: "))
    res_1 = get_max_digit_with_str(user_input)
    print(f"Find with using str: {res_1}")

    res_2 = get_max_digit_without_str(user_input)
    print(f"Find without using str: {res_2}")


if __name__ == "__main__":
    main()
