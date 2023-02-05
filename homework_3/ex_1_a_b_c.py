from typing import Any, Tuple


def swap_with_temporary_variable(a: Any, b: Any) -> Tuple[Any, Any]:
    """Swap the values of variables a and b with temporary variable c"""
    c = a
    a = b
    b = c
    return a, b


def swap_values_without_extra_variable(a: Any, b: Any) -> Tuple[Any, Any]:
    """Swap the values of variables a and b without additional variable"""
    a, b = b, a
    return a, b


def swap_int_values_of_variables(a: int, b: int) -> Tuple[int, int]:
    """Swap the values of variables a and b without additional variables"""
    a += b
    b = a - b
    a -= b
    return a, b


a = input("Enter, please, variable a: ")
b = input("Enter, please, variable b: ")

print(swap_with_temporary_variable(a, b))
print(swap_values_without_extra_variable(a, b))
print(swap_int_values_of_variables(int(a), int(b)))
