def sum_symbol_codes(first: str, last: str) -> float:
    unicode_diff = ord(last) - ord(first)
    triangle_num = unicode_diff * (unicode_diff + 1) / 2

    return ord(first) * (unicode_diff + 1) + triangle_num


def main() -> None:
    char_1, char_2 = input("Enter symbols to find unicode sum between them: ").split()
    sum_codes = sum_symbol_codes(char_1, char_2)
    print(f"Unicode sum between '{char_1}' and '{char_2}' - {sum_codes}")


def test():
    result = sum_symbol_codes("a", "d")
    assert result == 394, f"For symbols 'a' and 'b' result must be 394.0"


if __name__ == "__main__":
    main()
    test()
