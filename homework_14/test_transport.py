from transport import Transport, ElectricTransport, AirTransport, Train, AirBalloon, Plane


def test_transport():
    tr = Transport("t_transport", 100_000_000, 800)
    assert tr.brand == "t_transport", "Result must be 't_transport'"
    assert tr.weight == 100_000_000, "Result must be '100_000_000'"
    assert tr.max_speed == 800, "Result must be '800_000_000'"
    assert tr.start_to_move() == "t_transport starts to move...", "Result must be 't_transport starts to move...'"
    assert tr.sound() == "...sound when moving...", "Result must be '...sound when moving...'"


def test_electric_transport():
    el_tr = ElectricTransport("t_el_transport", 120_000_000, 1000, engine="Gas")
    assert el_tr.brand == "t_el_transport", "Result must be 't_el_transport'"
    assert el_tr.weight == 120_000_000, "Result must be '120_000_000'"
    assert el_tr.max_speed == 1000, "Result must be '1000'"
    assert el_tr.engine == "Gas", "Result must be 'Gas'"

    assert el_tr.start_to_move() == "t_el_transport start the engine and go!",\
        "Result must be 't_el_transport start the engine and go!'"
    assert el_tr.sound() == "...sound when moving...", "Result must be '...sound when moving...'"
    assert el_tr.stop_transport() == "Transport stopped", "Result must be 'Transport stopped'"


def test_air_transport():
    air_tr = AirTransport("air_transport", 107_000_000, 900, flight_altitude=10_000)
    assert air_tr.brand == "air_transport", "Result must be 'air_transport'"
    assert air_tr.weight == 107_000_000, "Result must be '107_000_000'"
    assert air_tr.max_speed == 900, "Result must be '900'"
    assert air_tr.flight_altitude == 10_000, "Result must be '10_000'"

    assert air_tr.start_to_move() == "air_transport takes off!",\
        "Result must be 'air_transport takes off!'"
    assert air_tr.sound() == "...sound when moving...", "Result must be '...sound when moving...'"


def test_train():
    train = Train("t_train", 200_000_000, 400, engine="555M", count_wagons=75)
    assert train.brand == "t_train", "Result must be 't_train'"
    assert train.weight == 200_000_000, "Result must be '200_000_000'"
    assert train.max_speed == 400, "Result must be '400'"
    assert train.engine == "555M", "Result must be '555M'"
    assert train.count_wagons == 75, "Result must be '75'"

    assert train.start_to_move() == "t_train start the engine and go!",\
        "Result must be 't_train start the engine and go!'"
    assert train.sound() == "Sound when moving chuh-chux tu-tu", "Result must be 'Sound when moving chuh-chux tu-tu'"
    train.add_wagons(5)
    assert train.count_wagons == 80, "Result must be '80'"
    assert train.stop_transport() == "Transport stopped", "Result must be 'Transport stopped'"


def test_air_balloon():
    air_balloon = AirBalloon("air_balloon", 1_000_000, 200, flight_altitude=5_000, temperature_inside=70)
    assert air_balloon.brand == "air_balloon", "Result must be 'air_balloon'"
    assert air_balloon.weight == 1_000_000, "Result must be '1_000_000'"
    assert air_balloon.max_speed == 200, "Result must be '900'"
    assert air_balloon.flight_altitude == 5_000, "Result must be '10_000'"
    assert air_balloon.temperature_inside == 70, "Result must be '70'"

    assert air_balloon.start_to_move() == "air_balloon takes off!",\
        "Result must be 'air_balloon takes off!'"
    assert air_balloon.sound() == "Sound when moving 'phhh-phhh' *sound of air heat burner*",\
        "Result must be 'Sound when moving 'phhh-phhh' *sound of air heat burner*'"


def test_plane():
    plane = Plane("Boeing 727", 100000000, 800, engine="JT9D", flight_attitude=13700, length_wing=73)
    # assert plane.brand == "Boeing 727", "Result must be 'Boeing 727'"
    # assert plane.weight == 100_000_000, "Result must be '100_000_000'"
    # assert plane.max_speed == 800, "Result must be '800_000_000'"
    # assert plane.engine == "JT9D", "Result must be 'JT9D'"
    # assert plane.flight_altitude == 13_700, "Result must be '13_700'"
    # assert plane.length_wing == 37, "Result must be '37'"


# def test_plane_clean_turbine():
#     plane = Plane("Boeing 747", 120_000_000, 700, "PW2000", 12_000, 50)
#     expected_res = "Result must be 'Turbine of Boeing 747 is clean'"
#     assert plane.clean_turbine() == "Turbine of Boeing 747 is clean", expected_res
#
#
# def test_plane_start_to_move():
#     plane = Plane("Boeing 757", 112_000_000, 750, "JT8D", 14_000, 60)
#     expected_res = "Boeing 757 start the engine and takes off!"
#     assert plane.clean_turbine() == "Boeing 757 start the engine and takes off!", expected_res


if __name__ == "__main__":
    test_transport()
    test_electric_transport()
    test_air_transport()
    test_train()
    test_air_balloon()
    test_plane()
