"""
Advent of code 2022 - https://adventofcode.com/2022
Yohann THEPAUT (ythepaut) <contact@ythepaut.com>
"""


def preprocess_inputs(inputs: list[str]) -> list[list[int]]:
    elves: list[list[int]] = []
    current_elf: list[int] = []
    for input_ in inputs:
        if input_ == "\n":
            elves.append(current_elf)
            current_elf = []
        else:
            current_elf.append(int(input_[:-1]))
    if len(current_elf) > 0:
        elves.append(current_elf)
    return elves


def elf_with_max_calories(elves: list[list[int]]) -> int:
    """Returns the index of the elf carrying the most snacks"""
    assert len(elves) > 0
    max_calories: int = sum(elves[0])
    best_elf_index: int = 0
    for index, elf in enumerate(elves[1:]):
        calories: int = sum(elf)
        if calories > max_calories:
            max_calories = calories
            best_elf_index = index + 1
    return best_elf_index


def part1(elves: list[list[int]]) -> int:
    return sum(elves[elf_with_max_calories(elves)])


def part2(elves: list[list[int]]) -> int:
    total_calories: int = 0
    for i in range(3):
        best_elf: int = elf_with_max_calories(elves)
        total_calories += sum(elves[best_elf])
        elves.pop(best_elf)
    return total_calories


def solve(inputs: list[str]) -> tuple[int, int]:
    elves = preprocess_inputs(inputs)
    return part1(elves), part2(elves)
