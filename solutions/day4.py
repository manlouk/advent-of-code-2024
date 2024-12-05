import sys


def xmas_occurrences(puzzle: list, x: int, y: int) -> bool:
    rows = len(puzzle)
    cols = len(puzzle[0])

    total = 0

    # Vertical (downwards)
    if x + 3 < rows:
        vertical_down = [
            puzzle[x][y],
            puzzle[x + 1][y],
            puzzle[x + 2][y],
            puzzle[x + 3][y],
        ]
        if vertical_down in (["X", "M", "A", "S"], ["S", "A", "M", "X"]):
            total += 1

    # Horizontal (rightwards)
    if y + 3 < cols:
        horizontal_right = [
            puzzle[x][y],
            puzzle[x][y + 1],
            puzzle[x][y + 2],
            puzzle[x][y + 3],
        ]
        if horizontal_right in (["X", "M", "A", "S"], ["S", "A", "M", "X"]):
            total += 1

    # Diagonal (down-right)
    if x + 3 < rows and y + 3 < cols:
        diagonal_down_right = [
            puzzle[x][y],
            puzzle[x + 1][y + 1],
            puzzle[x + 2][y + 2],
            puzzle[x + 3][y + 3],
        ]
        if diagonal_down_right in (["X", "M", "A", "S"], ["S", "A", "M", "X"]):
            total += 1

    # Diagonal (down-left)
    if x + 3 < rows and y - 3 >= 0:
        diagonal_down_left = [
            puzzle[x][y],
            puzzle[x + 1][y - 1],
            puzzle[x + 2][y - 2],
            puzzle[x + 3][y - 3],
        ]
        if diagonal_down_left in (["X", "M", "A", "S"], ["S", "A", "M", "X"]):
            total += 1

    # If no matches were found
    return total


def x_mas_occurrences(puzzle: list, x: int, y: int) -> bool:

    rows = len(puzzle)
    cols = len(puzzle[0])

    if x + 1 < rows and y + 1 < cols and x - 1 >= 0 and y - 1 >= 0:

        return [puzzle[x - 1][y - 1], puzzle[x][y], puzzle[x + 1][y + 1]] in (
            ["M", "A", "S"],
            ["S", "A", "M"],
        ) and [puzzle[x + 1][y - 1], puzzle[x][y], puzzle[x - 1][y + 1]] in (
            ["M", "A", "S"],
            ["S", "A", "M"],
        )


def part_1():
    with open("tests/data/test_input4.txt", "r") as f:
        puzzle = []
        for line in f:
            puzzle.append([c for c in line.strip()])
        total_occurences = 0
        for i in range(len(puzzle)):
            for j in range(len(puzzle[i])):
                total_occurences += xmas_occurrences(puzzle, i, j)
        return total_occurences


def part_2():
    with open("data/input4.txt", "r") as f:
        puzzle = []
        for line in f:
            puzzle.append([c for c in line.strip()])
        total_occurences = 0
        for i in range(1, len(puzzle) - 1):
            for j in range(1, len(puzzle[i]) - 1):
                total_occurences += x_mas_occurrences(puzzle, i, j)
        return total_occurences


if __name__ == "__main__":
    print(f"Solution for part 1: {part_1()}")
    print(f"Solution for part 2: {part_2()}")
