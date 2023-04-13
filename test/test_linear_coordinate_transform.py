import pytest

from star_catalog.transformations import CoordinateSystem, LinearCoordinateSystemTransform


@pytest.mark.parametrize("source_x_range,source_y_range,target_x_range,target_y_range,source_coords,expected_result", [
    ((-1, 1), (1, -1), (0, 1000), (0, 1000), (0, 0), (500, 500)),
    ((-1, 1), (1, -1), (0, 1000), (0, 1000), (0.5, 0.5), (750, 250)),
    ((-1, 1), (1, -1), (0, 500), (0, 500), (0, 0), (250, 250)),
    ((-1, 1), (1, -1), (0, 500), (0, 500), (0.5, 0.5), (375, 125)),
])
def test_can_transform_between_coordinate_systems(source_x_range, source_y_range, target_x_range, target_y_range,
                                                  source_coords, expected_result):
    source = CoordinateSystem(x_range=source_x_range, y_range=source_y_range)
    target = CoordinateSystem(x_range=target_x_range, y_range=target_y_range)
    transform = LinearCoordinateSystemTransform(source, target)

    transformed_coordinates = transform.get_transformed_coordinates(source_coords)

    assert transformed_coordinates == expected_result


@pytest.mark.parametrize("source_x", [
    1.0967,
    (-1.0967),
])
def test_when_x_coordinate_is_outside_bounds_raise_error(source_x):
    source = CoordinateSystem(x_range=(-1, 1), y_range=(-1, 1))
    target = CoordinateSystem(x_range=(0, 1000), y_range=(0, 1000))
    transform = LinearCoordinateSystemTransform(source, target)

    with pytest.raises(ValueError) as error:
        transform.get_transformed_coordinates((source_x, 0))

    assert str(error.value) == f"x coordinate {source_x} is outside of the source coordinate system range (-1, 1)"


@pytest.mark.parametrize("source_y", [
    1.0967,
    (-1.0967),
])
def test_when_y_coordinate_is_outside_bounds_raise_error(source_y):
    source = CoordinateSystem(x_range=(-1, 1), y_range=(-1, 1))
    target = CoordinateSystem(x_range=(0, 1000), y_range=(0, 1000))
    transform = LinearCoordinateSystemTransform(source, target)

    with pytest.raises(ValueError) as error:
        transform.get_transformed_coordinates((1, source_y))

    assert str(error.value) == f"y coordinate {source_y} is outside of the source coordinate system range (-1, 1)"
