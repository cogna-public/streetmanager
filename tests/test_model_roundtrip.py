from streetmanager.lookup.swagger_client.models.coordinates import Coordinates


def test_coordinates_roundtrip():
    c = Coordinates(easting=123.45, northing=678.9)
    d = c.to_dict()
    assert d == {"easting": 123.45, "northing": 678.9}

