"""
This module provides classes for performing linear coordinate system transformations.

Classes:
    CoordinateSystem: A data class representing a coordinate system.
    LinearCoordinateSystemTransform: A class for performing linear transformations between two coordinate systems.
"""

from dataclasses import dataclass
from typing import Tuple


@dataclass
class CoordinateSystem:
    """
    A data class representing a coordinate system.

    Attributes:
        x_range (Tuple[float, float]): A tuple representing the range of x values in the coordinate system.
        y_range (Tuple[float, float]): A tuple representing the range of y values in the coordinate system.
    """

    x_range: Tuple[float, float] = (-1, 1)
    y_range: Tuple[float, float] = (1, -1)


class LinearCoordinateSystemTransform:
    """
    A class for performing linear transformations between two coordinate systems.

    Attributes:
        _source (CoordinateSystem): The source coordinate system for the transformation.
        _target (CoordinateSystem): The target coordinate system for the transformation.

    Methods:
        get_transformed_coordinates(source_coordinates: Tuple[float, float]) -> Tuple[float, float]:
            Returns a tuple representing the transformed coordinates in the target coordinate system, given a
            tuple representing the coordinates in the source coordinate system.
    """

    def __init__(self, source: CoordinateSystem, target: CoordinateSystem):
        self._source = source
        self._target = target

    def get_transformed_coordinates(self, source_coordinates: Tuple[float, float]) -> Tuple[float, float]:
        """
        Returns a tuple representing the transformed coordinates in the target coordinate system, given a tuple
        representing the coordinates in the source coordinate system.

        Args:
            source_coordinates (Tuple[float, float]): A tuple representing the coordinates in the
            source coordinate system.

        Returns:
            Tuple[float, float]: A tuple representing the transformed coordinates in the target coordinate system.

        Raises:
            ValueError: If the source coordinates are outside the bounds of the source coordinate system.
        """

        def transform_coordinate(coordinate, source_coordinate_range, target_coordinate_range):
            source_min, source_max = source_coordinate_range
            target_min, target_max = target_coordinate_range
            return ((coordinate - source_min) / (source_max - source_min)) * (target_max - target_min) + target_min

        def ensure_range(src_coordinates: Tuple[float, float]) -> None:
            _x, _y = src_coordinates
            if _x < self._source.x_range[0] or _x > self._source.x_range[1]:
                raise ValueError(
                    f"x coordinate {_x} is outside of the source coordinate system range {self._source.x_range}")
            if _y < self._source.y_range[1] or _y > self._source.y_range[0]:
                raise ValueError(
                    f"y coordinate {_y} is outside of the source coordinate system range {self._source.y_range}")

        ensure_range(source_coordinates)
        x, y = source_coordinates
        new_x = transform_coordinate(x, self._source.x_range, self._target.x_range)
        new_y = transform_coordinate(y, self._source.y_range, self._target.y_range)
        return new_x, new_y
