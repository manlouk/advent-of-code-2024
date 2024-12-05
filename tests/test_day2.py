from solutions.day2 import part1, check_difference, check_monotonicity_v2


def test_part1():

    part1_result = part1("tests/data/test_input2.txt")

    assert part1_result == 2


def test_check_difference():

    assert check_difference([7, 6, 4, 2, 1]) is True
    assert check_difference([9, 7, 6, 2, 1]) is False
    assert check_difference([1, 2, 4]) is True
    assert check_difference([1]) is True


def test_check_monotonicity():

    assert check_monotonicity_v2([7, 6, 4, 2, 1]) is True
    assert check_monotonicity_v2([1, 2, 3]) is True
    assert check_monotonicity_v2([1]) is True
    assert check_monotonicity_v2([3, 2, 1]) is True
    assert check_monotonicity_v2([1, 3, 2]) is False
    assert check_monotonicity_v2([[32, 30, 27, 26, 23, 21, 18, 15]]) == True
