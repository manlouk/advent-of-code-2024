from solutions.day4 import xmas_occurences


def test_xmas_occurences():

    puzzle = [
        ["X", "M", "A", "S"],
        ["S", "M", "A", "X"],
        ["X", "M", "A", "S"],
        ["S", "A", "M", "S"],
    ]

    assert xmas_occurences(puzzle, 0, 0) == 2
