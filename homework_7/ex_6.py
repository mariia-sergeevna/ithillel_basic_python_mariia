def calculate_fibonacci(index: int) -> int:
    if index == 1:
        return 0
    if index == 2:
        return 1
    previous_value, current_value = 0, 1
    current_index = 2
    while current_index <= index:
        current_value += previous_value
        previous_value = current_value - previous_value
        current_index += 1
    return previous_value


def main() -> None:
    user_input = int(input("Enter desired value: "))
    result = calculate_fibonacci(user_input)
    print(f"{user_input} element in fibonacci" f" is {result}")


if __name__ == "__main__":
    main()
