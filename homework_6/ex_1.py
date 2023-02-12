def is_even(number: float) -> bool:
    if number % 2:
        return False
    return True


def test():
    result = is_even(4)
    print("Result: ", result)
    assert result is True, "With number 4 the result should be True"


if __name__ == "__main__":
    test()
