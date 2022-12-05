"""
Advent of code 2022 - https://adventofcode.com/2022
Yohann THEPAUT (ythepaut) <contact@ythepaut.com>
"""

ITEMS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def preprocess_inputs(inputs: list[str]) -> list[str]:
    rucksacks = []
    for input_ in inputs:
        rucksacks.append(input_[:-1])
    return rucksacks


def get_compartments(rucksack: str) -> list[str]:
    i = len(rucksack) // 2
    return [rucksack[0:i], rucksack[i:len(rucksack)]]


def get_common_item(strings: list[str]) -> str | None:
    for item in strings[0]:
        if all(item in string for string in strings):
            return item
    return None


def get_item_priority(item: str) -> int:
    return ITEMS.index(item) + 1


def part1(rucksacks: list[str]) -> int:
    total = 0
    for rucksack in rucksacks:
        compartments = get_compartments(rucksack)
        common_item = get_common_item(compartments)
        total += get_item_priority(common_item)
    return total


def part2(rucksacks: list[str]) -> int:
    total = 0
    for i in range(0, len(rucksacks) // 3):
        common_item = get_common_item(rucksacks[3 * i:3 * i + 3])
        total += get_item_priority(common_item)
    return total


def solve(inputs: list[str]) -> tuple[int, int]:
    rucksacks = preprocess_inputs(inputs)
    return part1(rucksacks), part2(rucksacks)
