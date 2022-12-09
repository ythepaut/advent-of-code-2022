"""
Advent of code 2022 - https://adventofcode.com/2022
Yohann THEPAUT (ythepaut) <contact@ythepaut.com>
"""
from dataclasses import dataclass


@dataclass
class Grid:
    trees: list[str]
    height: int
    width: int


def preprocess_inputs(inputs: list[str]) -> Grid:
    trees: list[str] = list(map(lambda input_: input_[:-1], inputs))
    return Grid(trees, len(trees), len(trees[0]))


def is_tree_visible(grid: Grid, row: int, col: int) -> bool:
    tree_height = int(grid.trees[row][col])
    return any([
        all([int(grid.trees[row - delta][col]) < tree_height for delta in range(1, row + 1)]),
        all([int(grid.trees[row + delta][col]) < tree_height for delta in range(1, grid.height - row)]),
        all([int(grid.trees[row][col - delta]) < tree_height for delta in range(1, col + 1)]),
        all([int(grid.trees[row][col + delta]) < tree_height for delta in range(1, grid.width - col)]),
    ])


def part1(grid: Grid) -> int:
    visible_tree_count = 0
    for row in range(grid.height):
        for col in range(grid.width):
            if is_tree_visible(grid, row, col):
                visible_tree_count += 1
    return visible_tree_count


def part2(grid: Grid) -> int:
    best_score = 0
    for row in range(1, grid.height - 1):
        for col in range(1, grid.width - 1):
            scenic_score = 1
            for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
                i, j = row + dx, col + dy
                distance = 0

                while 0 <= i < grid.height and 0 <= j < grid.width:
                    distance += 1
                    if grid.trees[row][col] <= grid.trees[i][j]:
                        break
                    i += dx
                    j += dy

                scenic_score *= distance
            best_score = max(best_score, scenic_score)
    return best_score


def solve(inputs: list[str]) -> tuple[int, int]:
    grid = preprocess_inputs(inputs)
    return part1(grid), part2(grid)
