def lchain(*iterables) -> list:
    result = []
    for el in iterables:
        result.extend([*el])
    return result


def test_lchain_with_multiple_iterable():
    test_data = [1, 2, 3], {'5': 5}, tuple(), (6, 7), range(8, 10)
    expected_result = [1, 2, 3, '5', 6, 7, 8, 9]
    error_msg = "Result must be '[1, 2, 3, '5', 6, 7, 8, 9]'"
    assert lchain(test_data) == expected_result, error_msg


if __name__ == "__main__":
    test_lchain_with_multiple_iterable()
