from math import pi, sqrt


def cone_square_and_volume(
        radius: float,
        height: float
) -> tuple[float, float]:
    local_square = pi * pow(radius, 2) + pi * radius *\
             (sqrt(pow(radius, 2) + pow(height, 2)))
    local_volume = 1/3 * pi * pow(radius, 2) * height
    return round(local_square, 2), round(local_volume, 2)


input_radius, input_height = input("Enter radius and height of cone: ").split()

square, volume = cone_square_and_volume(float(input_radius), float(input_height))

print(f"Square of cone - {square}, volume - {volume}")
