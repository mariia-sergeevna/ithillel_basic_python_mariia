from math import pi, sqrt


def cone_square_and_volume(radius: float, height: float) -> tuple[float, float]:
    local_square = pi * (radius**2) + pi * radius * (sqrt(radius**2 + height**2))
    local_volume = 1 / 3 * pi * pow(radius, 2) * height
    return local_square, local_volume


input_radius, input_height = input("Enter radius and height of cone: ").split()

square, volume = cone_square_and_volume(float(input_radius), float(input_height))

print(f"Square of cone - {round(square, 2)}, volume - {round(volume, 2)}")
