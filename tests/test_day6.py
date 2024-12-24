import pytest

from solutions.day6 import part1, part2, read_maze


@pytest.fixture
def example_input():
    return "tests/data/test_input6.txt"


@pytest.fixture
def maze_list():
    maze = read_maze("tests/data/test_input6.txt").split("\n")
    maze = [[c for c in row] for row in maze]

    return maze


def test_is_valid_move(maze_list):
    assert is_valid_move(maze_list, 0, 0) == True
    assert is_valid_move(maze_list, 0, 4) == False


def test_part1(example_input):
    assert part1(example_input) == 41


def test_part2(example_input):
    assert part2(example_input) == 6
