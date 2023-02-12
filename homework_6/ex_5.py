def check_year(year: int) -> bool:
    if (not year % 4 and year % 100) or not year % 400:
        return True
    return False


def main() -> None:
    input_year = int(input("Enter year: "))
    result = check_year(input_year)
    print("YES" if result else "NO")


if __name__ == "__main__":
    main()
