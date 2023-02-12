def calculate_fibonacci(index: int) -> int:
    if index == 1:
        return 0
    if index == 2:
        return 1
    return calculate_fibonacci(index - 1) + calculate_fibonacci(index - 2)


def main() -> None:
    user_input = int(input("Enter desired value: "))
    result = calculate_fibonacci(user_input)
    print(f"{user_input} element in fibonacci" f" is {result}")


if __name__ == "__main__":
    main()
