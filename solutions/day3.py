from typing import List
import re


def clean_noise(instruction: str) -> List[str]:
    return re.findall(r"mul\(\d+,\d+\)", instruction)


def extract_enriched_instruction_set(instruction: str) -> List[str]:
    return re.findall(r"mul\(\d{1,3},\d{1,3}\)|don\'t\(\)|do\(\)", instruction)


def find_active_instructions(instructions: List[str]) -> List[str]:
    active_instructions = []
    active = True
    for instruction in instructions:
        if instruction == "do()":
            active = True
        if instruction == "don't()":
            active = False
        if active:
            if "mul" in instruction:
                active_instructions.append(instruction)
    return active_instructions


def calculate_sum(instructions: List[str]) -> int:
    total = 0
    for instruction in instructions:
        x, y = instruction.replace("mul(", "").replace(")", "").split(",")
        total += int(x) * int(y)
    return total


def part1(filename: str) -> int:
    clean_instructions = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            clean_instructions += clean_noise(line)

    return calculate_sum(clean_instructions)


def part2(filename: str) -> int:
    clean_instructions = []
    with open(filename, "r") as f:
        clean_instructions = []
        for line in f:
            clean_instructions += extract_enriched_instruction_set(line)
        active_instructions = find_active_instructions(clean_instructions)

        return calculate_sum(active_instructions)


if __name__ == "__main__":
    print(f"Solution for part 1: {part1(filename='data/input3.txt')}")
    print(f"Solution for part 2: {part2(filename='data/input3.txt')}")
