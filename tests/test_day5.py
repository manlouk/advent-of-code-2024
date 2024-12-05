import pytest
from solutions.day5 import (
    create_graph,
    correctly_ordered_update,
    print_queue,
    find_middle_number,
    order_updates,
)


@pytest.fixture
def correct_update():
    return [97, 53, 13, 20]


@pytest.fixture
def incorrect_update():
    return [97, 13, 17, 20]


def test_create_graph(ordering_rules):
    ordering_rules = ordering_rules.split("\n")
    assert create_graph(ordering_rules) == {53: [13], 97: [13, 53], 13: [20], 20:[]}


def test_correctly_ordered_update(correct_update, incorrect_update, ordering_rules):
    ordering_rules = ordering_rules.split("\n")
    graph = create_graph(ordering_rules)
    assert correctly_ordered_update(correct_update, graph) == True
    assert correctly_ordered_update(incorrect_update, graph) == False


def test_find_middle_number():
    assert find_middle_number([75, 47, 61, 53, 29]) == 61
    assert find_middle_number([97, 61, 53, 29, 13]) == 53
    assert find_middle_number([75, 29, 13]) == 29


def test_order_updates(ordering_rules):
    ordering_rules = ordering_rules.split("\n")
    graph = create_graph(ordering_rules)
    assert order_updates([75,97,61,47, 47], graph) == [97,75,47,61,53]


def test_print_queue():

    assert print_queue("tests/data/test_input5.txt") == (143, 123)
