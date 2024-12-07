import pytest
from solutions.day7 import eval_expression, valid_test_value, bridge_repair


def test_eval_expression():

    assert eval_expression( [1,2,4],['+','*'])==12
    assert eval_expression([1,2,4],['*','+']) == 6
    assert eval_expression([1,2],['*']) == 2
    assert eval_expression([1,2],["||"]) == 12
    assert eval_expression([15,5],["||"]) == 155

def test_valid_test_value():

    assert valid_test_value(190,[10,19],['*','+']) == True
    assert valid_test_value(3267,[81,40,27],['*','+']) == True
    assert valid_test_value(83,[17,5],['*','+']) == False
    assert valid_test_value(156,[15,6],['*','+']) == False
    assert valid_test_value(292,[11, 6, 16, 20],['*','+'])==True
    assert valid_test_value(21037,[9, 7, 18, 13],['*','+']) == False

def test_part1():
    assert bridge_repair('tests/data/test_input7.txt')==11387