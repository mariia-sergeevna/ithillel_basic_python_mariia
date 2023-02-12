def sign(number: float) -> int:
    if number == 0:
        return 0
    if number < 1:
        return -1
    return 1


def main() -> None:
    input_number = float(input("Enter number: "))
    result = sign(input_number)
    print(f"For number {input_number} sign is {result}")


if __name__ == "__main__":
    main()
