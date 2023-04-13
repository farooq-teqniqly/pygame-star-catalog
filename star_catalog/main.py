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
        """

        x, y = source_coordinates

        source_x_min, source_x_max = self._source.x_range
        target_x_min, target_x_max = self._target.x_range
        new_x = ((x - source_x_min) / (source_x_max - source_x_min)) * (target_x_max - target_x_min) + target_x_min

        source_y_min, source_y_max = self._source.y_range
        target_y_min, target_y_max = self._target.y_range
        new_y = ((y - source_y_min) / (source_y_max - source_y_min)) * (target_y_max - target_y_min) + target_y_min

        return new_x, new_y
