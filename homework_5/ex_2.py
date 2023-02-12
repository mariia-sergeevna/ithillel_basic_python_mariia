from math import sqrt


def triangle_square_and_perimeter(
        side_1: float,
        side_2: float
) -> tuple[float, float]:
    hypotenuse = sqrt(pow(side_1, 2) + pow(side_2, 2))
    local_square = (side_1 * side_2) / 2
    local_perimeter = side_1 + side_2 + hypotenuse
    return local_square, local_perimeter


while True:
    leg_1, leg_2 = map(float, input("Enter legs of triangle: ").split())
    square, perimeter = triangle_square_and_perimeter(leg_1, leg_2)
    print(f"Square triangle is {round(square, 2)},"
          f" perimeter is {round(perimeter, 2)}")
