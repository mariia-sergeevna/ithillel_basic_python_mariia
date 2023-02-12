from math import sqrt


def solve_quadratic_equation(a: float, b: float, c: float) -> tuple:
    discriminant = pow(b, 2) - (4 * a * c)
    if discriminant < 0:
        return None, None
    elif discriminant == 0:
        return (-b) / 2 * a, None
    return (-b + sqrt(discriminant)) / (2 * a), (-b - sqrt(discriminant)) / (2 * a)


def main() -> None:
    user_input = input("Enter equation parameters: ")
    param_1, param_2, param_3 = map(float, user_input.split())

    x_1, x_2 = solve_quadratic_equation(param_1, param_2, param_3)
    if x_1 is None and x_2 is None:
        print("Equation has no roots")
    elif x_2 is None:
        print(f"Equation has one root: {x_1}")
    else:
        print(f"Roots of equation: {x_1} and {x_2}")


def test() -> None:
    result = solve_quadratic_equation(1, -2, -3)
    print("Result: ", result)
    assert result == (
        3.0,
        -1.0,
    ), "For parameters 1, -2, -3 the result should be 3 and -1"

    result = solve_quadratic_equation(1, 12, 36)
    print("Result: ", result)
    assert result == (-6.0, None), "For parameters 1, 12, 36 the result should be -6"

    result = solve_quadratic_equation(5, 3, 7)
    print("Result: ", result)
    assert result == (
        None,
        None,
    ), "For parameters 5, 3, 7 the result should be 'Equation has no roots'"


if __name__ == "__main__":
    test()
    main()
