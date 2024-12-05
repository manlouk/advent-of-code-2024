from solutions.day3 import (
    clean_noise,
    calculate_sum,
    part1,
    extract_enriched_instruction_set,
    find_active_instructions,
    part2,
)

# def test_part1():
#     assert part1('tests/data/test_input3.txt') == 161


def test_clean_noise():
    assert clean_noise("mul(2,3)") == ["mul(2,3)"]
    assert clean_noise("mul(2,3]") == []
    assert clean_noise("add(2,3)mul(2,3)") == ["mul(2,3)"]
    assert clean_noise("add(2,3)mul(2,3)mul(123,323)") == ["mul(2,3)", "mul(123,323)"]


def test_calculate_sum():
    assert calculate_sum(["mul(2,3)"]) == 6
    assert calculate_sum(["mul(2,3)", "mul(123,323)"]) == 6 + 123 * 323


def test_extract_enriched_instruction_set():
    assert extract_enriched_instruction_set("do()x34fs?!mul(1,2)") == [
        "do()",
        "mul(1,2)",
    ]
    assert extract_enriched_instruction_set("do()x34fs?!mul(1,2)don't()") == [
        "do()",
        "mul(1,2)",
        "don't()",
    ]
    assert extract_enriched_instruction_set("don't()do()x$^£)@mul(1,2)") == [
        "don't()",
        "do()",
        "mul(1,2)",
    ]
    assert extract_enriched_instruction_set("dox$^£)@mul(1,2)mul(3,5)") == [
        "mul(1,2)",
        "mul(3,5)",
    ]
    assert extract_enriched_instruction_set(
        "xmul(2,4)&mul[3,7]!^dodo()n't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    ) == ["mul(2,4)", "do()", "mul(5,5)", "mul(11,8)", "do()", "mul(8,5)"]


def test_find_active_instructions():
    assert find_active_instructions(["do()", "mul(1,2)", "don't()"]) == ["mul(1,2)"]
    assert find_active_instructions(["do()", "mul(1,2)", "don't()", "mul(3,5)"]) == [
        "mul(1,2)"
    ]
    assert find_active_instructions(
        ["mul(1,2)", "mul(2,4)", "don't()", "mul(3,5)", "do()", "mul(100,1)"]
    ) == ["mul(1,2)", "mul(2,4)", "mul(100,1)"]
    assert find_active_instructions(
        ["mul(1,2)", "don't()", "mul(100,1)", "mul(2,4)", "do()", "mul(3,5)", "do()"]
    ) == ["mul(1,2)", "mul(3,5)"]
    assert find_active_instructions(["don't()", "do()", "mul(100,1)", "mul(2,4)"]) == [
        "mul(100,1)",
        "mul(2,4)",
    ]


def test_part1():
    assert part1("tests/data/test_input31.txt") == 161


def test_part2():
    assert part2("tests/data/test_input32.txt") == 48
