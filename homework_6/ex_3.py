from cmath import sqrt
import math


def solve_2equation_in_complex(a: float, b: float, c: float) -> tuple:
    discriminant = pow(b, 2) - (4 * a * c)
    if a != 0:
        if discriminant < 0:
            x1 = (-b + sqrt(discriminant)) / (2 * a)
            x2 = (-b - sqrt(discriminant)) / (2 * a)
            return x1, x2
        elif discriminant == 0:
            return (-b) / 2 * a, None
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return x1, x2
    return None, None


def main() -> None:
    param_1, param_2, param_3 = map(float, input("Enter equation parameters: ").split())
    x_1, x_2 = solve_2equation_in_complex(param_1, param_2, param_3)
    if x_1 is None and x_2 is None:
        print("This is not quadratic equation!")
    elif x_2 is None:
        print(f"Equation has one real root: {x_1}")
    else:
        print(f"Roots of equation: {x_1} and {x_2}")


def test() -> None:
    result = solve_2equation_in_complex(1, 2, 5)
    print("Result: ", result)
    assert result == (
        (-1 + 2j),
        (-1 - 2j),
    ), "For parameters 1, 2, 5 the result should be (-1+2j) and (-1-2j)"

    result = solve_2equation_in_complex(0, 3, 7)
    print("Result: ", result)
    assert result == (
        None,
        None,
    ), "For parameters 0, 3, 7 the result should be 'This is not quadratic equation!'"


if __name__ == "__main__":
    test()
    main()
