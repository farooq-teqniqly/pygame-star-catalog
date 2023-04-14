import argparse
from typing import List, Union

import pygame
from pygame import Surface, SurfaceType

import defaults
from star_catalog.star import Star

DEFAULT_MARGIN = 20
DEFAULT_MODE = "plain"
DEFAULT_COLOR = pygame.Color(255, 255, 255)
DEFAULT_SIZE = 1


def process_file(star_data_file: str) -> List[Star]:
    with open(star_data_file, "r", encoding=defaults.encoding) as input_file:
        lines = input_file.readlines()

    stars = []

    for line in lines:
        segments = line.split(",")
        stars.append(Star((float(segments[0]), float(segments[1]), 0.0), float(segments[2])))

    return stars


def get_star_size(star: Star) -> int:
    size = round(10.0 / (star.magnitude + 2))
    return size


def draw_star(mode: str, star: Star, margin: int, color: pygame.Color, screen: Union[Surface, SurfaceType]):
    if mode == "plain":
        size = DEFAULT_SIZE
    else:
        size = get_star_size(star)

    pygame.draw.rect(screen, color, (int(star.coordinates[0] + margin), int(star.coordinates[1] + margin), size, size))


def init_screen(screen_width: int, screen_height: int) -> Union[Surface, SurfaceType]:
    pygame.init()
    return pygame.display.set_mode((screen_width, screen_height))


def main(screen_width: int, screen_height: int, star_data_file: str, margin: int = 20, mode: str = DEFAULT_MODE):
    stars = process_file(star_data_file)
    screen = init_screen(screen_width, screen_height)

    done = False
    already_plotted = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if not already_plotted:
                for star in stars:
                    draw_star(mode, star, margin, DEFAULT_COLOR, screen)
                    pygame.display.update()

                already_plotted = True

    pygame.quit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Star plot app")

    # Add required arguments for screen width and height
    parser.add_argument("screen_width", type=int, help="Screen width in pixels")
    parser.add_argument("screen_height", type=int, help="Screen height in pixels")
    parser.add_argument("star_data_file", help="The star data input file")
    parser.add_argument('--margin', type=int, default=DEFAULT_MARGIN, help='Margin in pixels')

    parser.add_argument("--mode", choices=[DEFAULT_MODE, "magnitude"], default=DEFAULT_MODE,
                        help="The mode for drawing the star plot")

    # Parse the arguments
    args = parser.parse_args()
    main(args.screen_width, args.screen_height, args.star_data_file, args.margin, args.mode)
