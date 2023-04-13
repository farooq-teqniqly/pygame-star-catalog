from io import BytesIO, TextIOWrapper

from star_catalog.star import StarReader, Star


def test_can_create_star():
    line = "0.994772 0.023164 -0.099456 28 4.61 3"
    stream = TextIOWrapper(BytesIO(line.encode("utf-8")))
    reader = StarReader(stream)
    stars = list(reader.read())

    assert len(stars) == 1
    assert stars[0] == Star((0.994772, 0.023164, -0.099456), 4.61)
