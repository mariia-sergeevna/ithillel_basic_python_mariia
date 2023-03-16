from transport import Plane


def test_plane_attributes():
    plane = Plane("Boeing 727", 100000000, 800, "JT9D", 13700, 73)
    assert plane.brand == "Boeing 727", "Result must be 'Boeing'"
    assert plane.weight == 100_000_000, "Result must be '100_000_000'"
    assert plane.max_speed == 800, "Result must be '800_000_000'"
    assert plane.engine == "JT9D", "Result must be 'JT9D'"
    assert plane.flight_altitude == 13_700, "Result must be '13_700'"
    assert plane.length_wing == 37, "Result must be '37'"


def test_plane_clean_turbine():
    plane = Plane("Boeing 747", 120_000_000, 700, "PW2000", 12_000, 50)
    expected_res = "Result must be 'Turbine of Boeing 747 is clean'"
    assert plane.clean_turbine() == "Turbine of Boeing 747 is clean", expected_res


def test_plane_start_to_move():
    plane = Plane("Boeing 757", 112_000_000, 750, "JT8D", 14_000, 60)
    expected_res = "Boeing 757 start the engine and takes off!"
    assert plane.clean_turbine() == "Boeing 757 start the engine and takes off!", expected_res


if __name__ == "__main__":
    test_plane_attributes()
    test_plane_clean_turbine()
