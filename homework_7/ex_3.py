from math import log2


def calculate_wheat_chess_position(kilograms: float) -> str:
    grams = (kilograms * pow(10, 6)) / 35
    cage = int(log2(grams) + 1)
    letters = "abcdefgh"

    return letters[cage // 8] + str(cage % 8)


def main() -> None:
    input_kilograms = float(input("Enter desired value of seed in kg: "))
    chess_position = calculate_wheat_chess_position(input_kilograms)
    print(f"Chess position of wheat - {chess_position}")


def test():
    result = calculate_wheat_chess_position(0.03584)
    assert result == "b3", "With parameters '0.03584' result must be 'b3'"


if __name__ == "__main__":
    main()
    test()
