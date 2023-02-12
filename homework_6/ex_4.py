from math import sqrt


def circles_intersect(
    x1: float, y1: float, r1: float, x2: float, y2: float, r2: float
) -> bool:
    distance = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
    return distance <= r1 + r2


def main() -> None:
    user_input1 = input("Enter coordinates x, y, and r for the first circle: ")
    x_1, y_1, r_1 = map(float, user_input1.split())

    user_input2 = input("Enter coordinates x, y, and r for the second circle: ")
    x_2, y_2, r_2 = map(float, user_input2.split())
    if circles_intersect(x_1, y_1, r_1, x_2, y_2, r_2):
        print("These circles intersect")
    else:
        print("These circles don't intersect")


if __name__ == "__main__":
    main()
