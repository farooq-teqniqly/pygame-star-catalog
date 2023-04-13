"""
The star module contains classes and functions for working with stars.

Classes:
    Star: Represents a star in three-dimensional space.
    StarReader: A class for reading star data from a stream.

"""

from io import TextIOWrapper
from dataclasses import dataclass
from typing import Tuple, Generator


@dataclass
class Star:
    """
        Represents a star in three-dimensional space.

        Attributes:
            coordinates (Tuple[float, float, float]): The (x, y, z) coordinates of the star.
            magnitude (float): The magnitude (brightness) of the star.
    """
    coordinates: Tuple[float, float, float]
    magnitude: float


class StarReader:
    """
        A class for reading star data from a stream.

        Attributes:
            _stream (TextIOWrapper): A text stream object to read star data from.

        Methods:
            read(): A generator method that reads star data from the stream and yields
            Star objects.

        Example usage:
            with open('stars.txt', 'r') as file:
            reader = StarReader(file)
            for star in reader.read():
            print(star)
    """
    def __init__(self, stream: TextIOWrapper):
        self._stream = stream

    def read(self) -> Generator[Star, None, None]:
        for line in self._stream:
            line = line.strip()
            fields = line.split(" ")
            x, y, z, _, magnitude = map(float, fields[:5])
            yield Star(coordinates=(x, y, z), magnitude=magnitude)
