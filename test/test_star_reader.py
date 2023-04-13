from io import BytesIO, TextIOWrapper
from typing import Callable

from star_catalog.star import StarReader, Star

DEFAULT_ENCODING = "utf-8"


def test_can_create_star_from_string():
    line = "0.994772 0.023164 -0.099456 28 4.61 3"
    stream = TextIOWrapper(BytesIO(line.encode(DEFAULT_ENCODING)))
    reader = StarReader(stream)
    stars = list(reader.read())

    assert len(stars) == 1
    assert stars[0] == Star((0.994772, 0.023164, -0.099456), 4.61)


def test_can_create_star_from_byte_string():
    lines = [
        b"1 2 3 4 5\n",
        b"11 12 13 14 15\n",
    ]
    stream = TextIOWrapper(BytesIO(b"".join(lines)))

    # Process the stream
    reader = StarReader(stream)
    stars = list(reader.read())

    # Verify the result
    expected = [
        Star((1, 2, 3), 5),
        Star((11, 12, 13), 15),
    ]
    assert stars == expected


def test_can_transform_star_data():
    line = "0 0 0 1 3 5"
    stream = TextIOWrapper(BytesIO(line.encode(DEFAULT_ENCODING)))
    reader = StarReader(stream)
    transform: Callable[[tuple], tuple] = lambda data: tuple(x + 1 for x in data)
    stars = list(reader.read(transform))

    assert len(stars) == 1
    assert stars[0] == Star((1, 1, 1), 4)
