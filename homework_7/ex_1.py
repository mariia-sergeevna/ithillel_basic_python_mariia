def is_knight_move(coord_1, coord_2) -> bool:
    start_cage, finish_cage = list(coord_1), list(coord_2)

    unicode_difference = ord(finish_cage[0]) - ord(start_cage[0])
    num_cage_difference = int(finish_cage[1]) - int(start_cage[1])

    if unicode_difference in [-1, 1]:
        if num_cage_difference in [-2, 2]:
            return True
        return False
    elif unicode_difference in [-2, 2]:
        if num_cage_difference in [-1, 1]:
            return True
        return False
    else:
        return False


def main() -> None:
    start, finish = input("Enter start and finish knight's coordinates: ").split()
    result = is_knight_move(start, finish)
    print("Yes, it could" if result else f"No, it couldn't move to cage {finish}")


def test():
    true_case = is_knight_move("d4", "c6")
    assert true_case is True, "Knight could move from 'd4' to 'c6'"

    false_case = is_knight_move("c4", "b5")
    assert false_case is False, "Knight couldn't move from 'c4' to 'b5'"


if __name__ == "__main__":
    main()
    test()
