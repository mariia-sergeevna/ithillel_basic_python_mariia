from typing import Union


class Godzilla:
    """
    A class to represent a godzilla, that can eat humans.

    Attributes:
    - stomach_capacity: The maximum volume of humans that Godzilla can eat.
    - stomach_content: The current volume of humans in the stomach.
    """

    def __init__(self, stomach_volume: Union[int, float]) -> None:
        self.stomach_volume = stomach_volume
        self.stomach_contents = 0

    def eat(self, human_volume: Union[int, float]) -> None:
        """Try to eat the humans with given volume."""
        if self.stomach_contents + human_volume > self.stomach_volume:
            print("It's too much for my stomach")
        elif self.stomach_contents + human_volume > self.stomach_volume * 0.9:
            print("I'm full and can't eat more people")
        else:
            self.stomach_contents += human_volume
            print(f"I ate human {human_volume} size")


def test_godzilla_eat():
    godzilla = Godzilla(10.7)
    godzilla.eat(2.8)
    godzilla.eat(6)
    assert godzilla.stomach_contents == 8.8, "Result must be 8."


def test_godzilla_is_full():
    godzilla = Godzilla(100)
    godzilla.eat(50)
    godzilla.eat(45)
    assert (
        godzilla.stomach_contents == 50
    ), "Result must be 50, because godzilla is full"


def test_godzilla_too_much():
    godzilla = Godzilla(55)
    godzilla.eat(56)
    assert (
        godzilla.stomach_contents == 0
    ), "Result must be 0, because it's too much for godzilla"


if __name__ == "__main__":
    test_godzilla_eat()
    test_godzilla_is_full()
    test_godzilla_too_much()
