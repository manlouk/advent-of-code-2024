import sys
from solutions.day1 import part1, part2, read_input


def test_read_data():

    list1, list2 = read_input("tests/data/test_input1.txt")
    assert list1 == [3, 4, 2, 1, 3, 3]
    assert list2 == [4, 3, 5, 3, 9, 3]


def test_part1():
    part1_result = part1("tests/data/test_input1.txt")

    assert part1_result == 11


def test_part2():
    part2_result = part2("tests/data/test_input1.txt")

    assert part2_result == 31
