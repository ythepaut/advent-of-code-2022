"""
Advent of code 2022 - https://adventofcode.com/2022
Yohann THEPAUT (ythepaut) <contact@ythepaut.com>
"""

SectionRange = tuple[int, int]


def preprocess_inputs(inputs: list[str]) -> list[tuple[SectionRange, SectionRange]]:
    pairs = []
    for input_ in inputs:
        pair = input_[:-1].split(",")
        pairs.append((
            tuple(map(int, pair[0].split("-"))),
            tuple(map(int, pair[1].split("-")))
        ))
    return pairs


def range_from_section_range(section_range: SectionRange) -> range:
    return range(section_range[0], section_range[1] + 1)


def range_a_fully_overlaps_b(range_a: SectionRange, range_b: SectionRange) -> bool:
    section_range_a = range_from_section_range(range_a)
    section_range_b = range_from_section_range(range_b)
    for section_b in section_range_b:
        if section_b not in section_range_a:
            return False
    return True


def part1(pairs: list[tuple[SectionRange, SectionRange]]) -> int:
    count = 0
    for pair in pairs:
        if range_a_fully_overlaps_b(pair[0], pair[1]) or range_a_fully_overlaps_b(pair[1], pair[0]):
            count += 1
    return count


def range_a_partially_overlaps_b(range_a: SectionRange, range_b: SectionRange) -> bool:
    section_range_a = range_from_section_range(range_a)
    section_range_b = range_from_section_range(range_b)
    for section_b in section_range_b:
        if section_b in section_range_a:
            return True
    return False


def part2(pairs: list[tuple[SectionRange, SectionRange]]) -> int:
    count = 0
    for pair in pairs:
        if range_a_partially_overlaps_b(pair[0], pair[1]) or range_a_partially_overlaps_b(pair[1], pair[0]):
            count += 1
    return count


def solve(inputs: list[str]) -> tuple[int, int]:
    pairs = preprocess_inputs(inputs)
    return part1(pairs), part2(pairs)
