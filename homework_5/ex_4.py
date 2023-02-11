from typing import Union


def my_sum(*numbers: float, start: Union[int, float] = 0) -> float:
    return sum(numbers) + float(start)


print(f"Sum of numbers: {my_sum(1, 2, 3, 4, start=8)}")
