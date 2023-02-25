from typing import Union, Any


def index(lst: list, elem: Any) -> Union[int, None]:
    """Find index of element in list"""
    for idx, item in enumerate(lst):
        if item == elem:
            return idx


def main() -> None:
    input_lst = [el for el in input("Enter list of elements: ").split()]
    input_elem = input("Enter element to search in list: ")
    result = index(input_lst, input_elem)
    print(f"'{input_elem}' has index {result}" if result else "Element didn't find")


def test() -> None:
    result = index(["a", 1, 2.0, ["b"]], 1)
    assert result == 1, "With parameters (['a', 1, 2.0, ['b']], 1) result must be '1'"

    result = index(["a", 1, 2.0, ["b"]], 8)
    assert result is None, "This element doesn't exist in list"


if __name__ == "__main__":
    test()
    main()
