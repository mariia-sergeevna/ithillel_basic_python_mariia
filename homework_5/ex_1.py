from math import pi, cos


def display_result(degrees: float) -> str:
    return f"{degrees} in radians {degrees2radians(degrees)}"


def degrees2radians(degrees: float) -> float:
    return (degrees * pi) / 180


print(
    display_result(cos(60)), display_result(cos(45)), display_result(cos(40)), sep="\n"
)
