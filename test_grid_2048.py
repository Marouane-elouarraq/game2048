from grid_2048 import create_grid
from pytest import *


def test_create_grid():
    assert create_grid() == [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [
        ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]

test_create_grid()
