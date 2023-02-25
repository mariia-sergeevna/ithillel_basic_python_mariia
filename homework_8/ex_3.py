def sort_by_value(lst: list) -> list:
    return sorted(lst, key=float)


def sort_by_1digit_of_num(lst: list) -> list:
    return sorted(lst, key=lambda num: str(num)[0])


def main():
    result = sort_by_value([5, "9", 0, "452", 6.5, "6", 1, 2])
    print(result)

    result2 = sort_by_1digit_of_num([472, 326, 1, "1101000", "99", 9, "20", 863, "0"])
    print(result2)


if __name__ == "__main__":
    main()
