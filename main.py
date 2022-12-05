#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent of code 2022 - https://adventofcode.com/2022
Yohann THEPAUT (ythepaut) <contact@ythepaut.com>
"""

import argparse
from solutions import day1, day2, day3


def get_inputs(path: str) -> list[str]:
    """Gets inputs from files and return them as a list of strings."""
    file = open(path, "r", encoding="utf8")
    lines = file.readlines()
    file.close()
    return lines


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("day", type=int, help="Day number.")
    parser.add_argument("input", type=str, help="Input file path.")
    args = parser.parse_args()

    inputs = get_inputs(args.input)
    days = [day1, day2, day3]
    assert (0 < args.day <= len(days)), f"Day must be between 1 and {len(days)}"

    solutions = days[args.day - 1].solve(inputs)
    print("Part 1 solution : ", solutions[0])
    print("Part 2 solution : ", solutions[1])
