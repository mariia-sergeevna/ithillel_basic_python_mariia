def can_knight_move(cage1, cage2) -> bool:
    unicode_diff = ord(cage2[0]) - ord(cage1[0])
    num_diff = int(cage2[1]) - int(cage1[1])

    return abs(unicode_diff) * abs(num_diff) == 2


def main() -> None:
    start, finish = input("Enter start and finish knight's coordinates: ").split()
    result = can_knight_move(start, finish)
    print("Yes, it could" if result else f"No, it couldn't move to cage {finish}")


def test():
    true_case = can_knight_move("d4", "c6")
    assert true_case is True, "Knight could move from 'd4' to 'c6'"

    false_case = can_knight_move("c4", "b5")
    assert false_case is False, "Knight couldn't move from 'c4' to 'b5'"


if __name__ == "__main__":
    main()
    test()
