import os
from star_plot_app import process_file

test_data_root = os.path.join(os.getcwd(), "data")


def test_can_process_file():
    stars = process_file(os.path.join(test_data_root, "test_stardata.csv"))
    assert len(stars) == 1

    star = stars[0]

    assert star.coordinates == (997.386, 488.418, 0)
    assert star.magnitude == 4.61
