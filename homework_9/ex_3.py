from typing import Union


def copydeep(
    obj: Union[str, int, float, bool, list, tuple, dict]
) -> Union[str, int, float, bool, list, tuple, dict]:
    if isinstance(obj, (int, float, str, bool)):
        return obj

    if isinstance(obj, tuple):
        return tuple(copydeep(x) for x in obj)

    if isinstance(obj, list):
        return [copydeep(x) for x in obj]

    if isinstance(obj, dict):
        return {copydeep(key): copydeep(value) for key, value in obj.items()}


def test_deep_copy_with_dict():
    dict_1 = {1: "a", 2: 1, 3: 2.0, 4: ["b"]}
    dict_2 = copydeep(dict_1)
    dict_1[1] = 33
    error_msg = "Result must be '{1: 'a', 2: 1, 3: 2.0, 4: ['b']}'"
    assert dict_2 == {1: "a", 2: 1, 3: 2.0, 4: ["b"]}, error_msg


if __name__ == "__main__":
    test_deep_copy_with_dict()
