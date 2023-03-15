from typing import Union
from math import sqrt


class Point:
    """
    A class to represent a point in two-dimensional space.

    Attributes:
    - x: The x-coordinate of the point.
    - y: The y-coordinate of the point.
    """

    def __init__(self, x: Union[int, float], y: Union[int, float]):
        self.x = x
        self.y = y


class Circle:
    """
    A class to represent a circle in two-dimensional space.

    Attributes:
    - center: The center of the circle.
    - radius: The radius of the circle.
    """

    def __init__(self, center: Point, radius: Union[int, float]):
        self.center = center
        self.radius = radius

    def is_inside_point(self, point: Point) -> bool:
        """Check if the point inside of circle"""
        distance = sqrt((self.center.x - point.x) ** 2 + (self.center.y - point.y) ** 2)
        return distance <= self.radius


def test_point_outside_circle():
    center_circle = Point(3, 3)
    circle = Circle(center_circle, 2)
    point = Point(6, 5)
    assert circle.is_inside_point(point) is False, "Result must be False"


def test_point_inside_circle():
    center_circle = Point(0, 0)
    circle = Circle(center_circle, 1.5)
    point = Point(-0.2, 1)
    assert circle.is_inside_point(point) is True, "Result must be True"


if __name__ == "__main__":
    test_point_outside_circle()
    test_point_inside_circle()
