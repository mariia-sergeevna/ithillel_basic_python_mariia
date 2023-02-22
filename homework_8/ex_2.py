from typing import Union


def copydeep(
    obj: Union[int, float, str, tuple, list]
) -> Union[int, float, str, tuple, list]:
    if isinstance(obj, (int, float, str)):
        return obj

    if isinstance(obj, tuple):
        return tuple(copydeep(x) for x in obj)

    if isinstance(obj, list):
        return [copydeep(x) for x in obj]


def main():
    lst1 = ["a", 1, 2.0, ["b"]]
    lst2 = copydeep(lst1)
    lst1[3].append(0)
    print(f"Original list:\n{lst1}\nCopy:\n{lst2}")


if __name__ == "__main__":
    main()
