from dataclasses import dataclass
from typing import Tuple


@dataclass
class CoordinateSystem:
    x_range: Tuple[float, float] = (-1, 1)
    y_range: Tuple[float, float] = (1, -1)


class LinearCoordinateSystemTransform:
    def __init__(self, source: CoordinateSystem, target: CoordinateSystem):
        self._source = source
        self._target = target

    def get_transformed_coordinates(self, source_coordinates: Tuple[float, float]) -> Tuple[float, float]:
        x, y = source_coordinates

        source_x_min, source_x_max = self._source.x_range
        target_x_min, target_x_max = self._target.x_range
        new_x = ((x - source_x_min) / (source_x_max - source_x_min)) * (target_x_max - target_x_min) + target_x_min

        source_y_min, source_y_max = self._source.y_range
        target_y_min, target_y_max = self._target.y_range
        new_y = ((y - source_y_min) / (source_y_max - source_y_min)) * (target_y_max - target_y_min) + target_y_min

        return new_x, new_y
