from typing import Union


def copydeep(
    obj: Union[str, int, float, bool, list, dict], memory=None
) -> Union[str, int, float, bool, list, dict]:
    if memory is None:
        memory = {}

    if id(obj) in memory:
        return memory[id(obj)]

    elif isinstance(obj, (int, float, str, bool)):
        memory[id(obj)] = obj
        return obj

    elif isinstance(obj, list):
        copy_list = []
        memory[id(obj)] = copy_list
        for el in obj:
            copy_list.append(copydeep(el, memory))
        return copy_list

    elif isinstance(obj, dict):
        copy_dict = {}
        memory[id(obj)] = copy_dict
        for key, value in obj.items():
            copy_dict[copydeep(key, memory)] = copydeep(value, memory)
        return copy_dict


def test_deep_copy():
    test_data = [1, 2, [4, 5, 6], {"A": "B", "c": [3658]}, 2.0, {"e": 0}]
    test_data[3]["d"] = test_data
    copy = copydeep(test_data)

    assert (copy[3]["d"] is not test_data[3]["d"]), "Result must be true"


if __name__ == "__main__":
    test_deep_copy()
