import pytest

from star_catalog.main import CoordinateSystem, LinearCoordinateSystemTransform


@pytest.mark.parametrize("source_x_range,source_y_range,target_x_range,target_y_range,source_coords,expected_result", [
    ((-1, 1), (1, -1), (0, 1000), (0, 1000), (0, 0), (500, 500)),
    ((-1, 1), (1, -1), (0, 1000), (0, 1000), (0.5, 0.5), (750, 250)),
    ((-1, 1), (1, -1), (0, 500), (0, 500), (0, 0), (250, 250)),
    ((-1, 1), (1, -1), (0, 500), (0, 500), (0.5, 0.5), (375, 125)),
    # Add more test cases here as needed
])
def test_can_transform_between_coordinate_systems(source_x_range, source_y_range, target_x_range, target_y_range,
                                                  source_coords, expected_result):
    source = CoordinateSystem(x_range=source_x_range, y_range=source_y_range)
    target = CoordinateSystem(x_range=target_x_range, y_range=target_y_range)
    transform = LinearCoordinateSystemTransform(source, target)

    transformed_coordinates = transform.get_transformed_coordinates(source_coords)

    assert transformed_coordinates == expected_result
