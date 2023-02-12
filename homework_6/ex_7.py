def calculate_fibonacci(index: int) -> int:
    if index == 1:
        return 0
    if index == 2:
        return 1
    return calculate_fibonacci(index - 1) + calculate_fibonacci(index - 2)


def main() -> None:
    input_index = int(input("Enter desired value: "))
    print(
        f"{input_index} element in fibonacci" f" is {calculate_fibonacci(input_index)}"
    )


if __name__ == "__main__":
    main()
