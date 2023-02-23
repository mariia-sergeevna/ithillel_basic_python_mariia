def lchain(*iterables) -> list:
    result = []
    for el in iterables:
        result.extend([*el])
    return result


def test():
    assert lchain([1, 2, 3], {'5': 5}, tuple(), (6, 7), range(8, 10)) == [
         1, 2, 3, '5', 6, 7, 8, 9
    ], "Result must be '[1, 2, 3, '5', 6, 7, 8, 9]'"


if __name__ == "__main__":
    test()
