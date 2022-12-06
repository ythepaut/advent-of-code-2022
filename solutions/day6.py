"""
Advent of code 2022 - https://adventofcode.com/2022
Yohann THEPAUT (ythepaut) <contact@ythepaut.com>
"""

SectionRange = tuple[int, int]


def preprocess_inputs(inputs: list[str]) -> str:
    return inputs[0][:-1]


def find_marker_index(datastream: str, length: int) -> int:
    for i in range(len(datastream) - length):
        if len(set(datastream[i:i + length])) == length:
            return i + length
    return -1


def part1(datastream: str) -> int:
    return find_marker_index(datastream, 4)


def part2(datastream: str) -> int:
    return find_marker_index(datastream, 14)


def solve(inputs: list[str]) -> tuple[int, int]:
    datastream = preprocess_inputs(inputs)
    return part1(datastream), part2(datastream)
