import argparse
import urllib.request
import defaults

from star_catalog.star import StarReader
from star_catalog.transformations import CoordinateSystem, LinearCoordinateSystemTransform


def main(input_url: str, output_path: str):
    def transform_coordinates(data: tuple) -> tuple:
        x, y, z, magnitude = data
        transformed_x, transformed_y = transform.get_transformed_coordinates((x, y))
        return transformed_x, transformed_y, z, magnitude

    source = CoordinateSystem(x_range=(-1, 1), y_range=(-1, 1))
    target = CoordinateSystem(x_range=(0, 1000), y_range=(0, 1000))
    transform = LinearCoordinateSystemTransform(source, target)
    reader = StarReader(urllib.request.urlopen(input_url))
    stars = list(reader.read(transform_coordinates))

    with open(output_path, "w", encoding=defaults.encoding) as output_file:
        output_file.writelines([f"{star.coordinates[0]},{star.coordinates[1]},{star.magnitude}\n" for star in stars])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download star data from a URL, transform, and write to an output "
                                                 "file.")
    parser.add_argument("input_url", help="The URL to download from")
    parser.add_argument("output_file", help="The name of the output file")

    # Parse the arguments
    args = parser.parse_args()
    main(args.input_url, args.output_file)
