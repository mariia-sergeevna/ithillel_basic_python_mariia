from typing import Union


class Transport:
    """
    Represents a basic transport object.
    Attributes:
    - brand: the brand of the transport.
    - weight: the weight of the transport.
    - max_speed: the maximum speed that a transport can reach.
    """

    def __init__(
        self, brand: str, weight: Union[int, float], max_speed: Union[int, float]
    ):
        self.brand = brand
        self.weight = weight
        self.max_speed = max_speed

    def start_to_move(self) -> str:
        """Returns a string indicating the transport starts to move."""
        return f"{self.brand} starts to move..."

    @staticmethod
    def sound() -> str:
        """Returns a string indicating the sound the transport makes"""
        return "...sound when moving..."


class BrakesMixin:
    """Represents a mixin class that provides a method to stop the transport."""

    @staticmethod
    def stop_transport() -> str:
        """Returns a string indicating the transport is stopped."""
        return "Transport stopped"


class ElectricTransport(Transport, BrakesMixin):
    """
    A class representing electric transport that inherits from Transport and BrakesMixin.

    Attributes:
    - brand: str : the brand of the electric transport.
    - weight: Union[int, float] : the weight of the electric transport in kilograms.
    - max_speed: Union[int, float] : the maximum speed of the electric transport in kilometers per hour.
    - engine: str : the type of engine of the electric transport.
    """

    def __init__(self, *args, engine: str, **kwargs):
        super().__init__(*args, **kwargs)
        self.engine = engine

    def start_to_move(self):
        return f"{self.brand} start the engine and go!"


class AirTransport(Transport):
    """
    A class representing air transport that inherits from Transport.

    Attributes:
    - brand: str : the brand of the electric transport.
    - weight: Union[int, float] : the weight of the electric transport in kilograms.
    - max_speed: Union[int, float] : the maximum speed of the electric transport in kilometers per hour.
    - flight_altitude: Union[int, float] : the maximum altitude the air transport can reach in meters.
    """

    def __init__(
        self,
        *args,
        flight_altitude: Union[int, float],
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.flight_altitude = flight_altitude

    def start_to_move(self):
        return f"{self.brand} takes off!"


class Train(ElectricTransport):
    """
    A class representing a train that inherits from ElectricTransport.

    Attributes:
    - brand: str : the brand name of the train.
    - weight: Union[int, float] : the weight of the train in kilograms.
    - max_speed: Union[int, float] : the maximum speed of the train in km/h.
    - engine: str : the type of engine the train uses.
    - count_wagons: int : the number of wagons that the train has.
    """

    def __init__(
        self,
        *args,
        count_wagons: int,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.count_wagons = count_wagons

    @staticmethod
    def sound():
        return "Sound when moving chuh-chux tu-tu"

    def add_wagons(self, input_wagons: int):
        """A method that increases the number of wagons by input_wagons"""
        self.count_wagons += input_wagons


class AirBalloon(AirTransport):
    """
    A class representing air balloon that inherits from AirTransport.

    Attributes:
    - brand: str : the brand name of the air balloon.
    - weight: Union[int, float] : the weight of the air balloon in kilograms.
    - max_speed: Union[int, float] : the maximum speed of the air balloon in km/h.
    - flight_altitude: Union[int, float] : the maximum altitude the air balloon can reach in meters.
    - temperature_inside: Union[int, float] : the temperature inside the air balloon in Celsius.
    """

    def __init__(
        self,
        *args,
        temperature_inside: Union[int, float],
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.temperature_inside = temperature_inside

    @staticmethod
    def sound():
        return "Sound when moving 'phhh-phhh' *sound of air heat burner*"


class Plane(ElectricTransport, AirTransport):
    """
    A class representing a plane that inherits from ElectricTransport and AirTransport.

    Attributes:
    - brand: str : the brand of the plane.
    - weight: Union[int, float] : the weight of the plane in kilograms.
    - max_speed: Union[int, float] : the maximum speed of the plane in kilometers per hour.
    - engine: str : the type of engine used by the plane.
    - flight_altitude: Union[int, float] : the maximum altitude at which the plane can fly in meters.
    - length_wing: Union[int, float] : the length of the wings of the plane in meters.
    """

    def __init__(
        self,
        *args,
        length_wing: Union[int, float],
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.length_wing = length_wing

    def start_to_move(self):
        return f"{self.brand} start the engine and takes off!"

    @staticmethod
    def sound():
        return "Sound when moving 'Gggggggg'"

    def clean_turbine(self):
        """A method that cleans the turbine of the plane."""
        return f"Turbine of {self.brand} is clean"
