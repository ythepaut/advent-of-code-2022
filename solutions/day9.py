"""
Advent of code 2022 - https://adventofcode.com/2022
Yohann THEPAUT (ythepaut) <contact@ythepaut.com>
"""
from dataclasses import dataclass
from itertools import product

KNOTS_COUNT = 10


@dataclass
class Instruction:
    dx: int
    dy: int


@dataclass(frozen=False)
class Position:
    x: int
    y: int


def preprocess_inputs(inputs: list[str]) -> list[Instruction]:
    instructions: list[Instruction] = []
    for input_ in inputs:
        direction, delta = input_[:-1].split(" ")
        match direction:
            case "U":
                instructions.extend([Instruction(0, -1) for _ in range(int(delta))])
            case "D":
                instructions.extend([Instruction(0, 1) for _ in range(int(delta))])
            case "L":
                instructions.extend([Instruction(-1, 0) for _ in range(int(delta))])
            case "R":
                instructions.extend([Instruction(1, 0) for _ in range(int(delta))])
    return instructions


def get_position_neighbours(position: Position):
    for dx, dy in product([-1, 0, 1], repeat=2):
        neighbor = Position(position.x + dx, position.y + dy)
        yield neighbor


def get_delta(head: Position, tail: Position) -> tuple[int, int]:
    dx, dy = 0, 0

    # if head and tail are neighbours, skip
    if any(head == p for p in get_position_neighbours(tail)):
        return dx, dy

    if tail.y > head.y:
        dy -= 1
    elif tail.y < head.y:
        dy += 1
    if tail.x > head.x:
        dx -= 1
    elif tail.x < head.x:
        dx += 1

    return dx, dy


def part1(instructions: list[Instruction]) -> int:
    head = Position(0, 0)
    tail = Position(0, 0)
    visited_positions: list[tuple[int, int]] = []
    for instruction in instructions:
        head.x += instruction.dx
        head.y += instruction.dy

        dx, dy = get_delta(head, tail)
        tail.x += dx
        tail.y += dy

        visited_positions.append((tail.x, tail.y))
    return len(set(visited_positions))


def part2(instructions: list[Instruction]) -> int:
    nodes = [Position(0, 0) for _ in range(KNOTS_COUNT)]
    visited_positions: list[tuple[int, int]] = []
    for instruction in instructions:
        head = nodes[0]
        head.x += instruction.dx
        head.y += instruction.dy

        for i, current_tail in enumerate(nodes[1:]):
            dx, dy = get_delta(head, current_tail)
            current_tail.x += dx
            current_tail.y += dy
            head = current_tail
            if i == KNOTS_COUNT - 2:
                visited_positions.append((nodes[-1].x, nodes[-1].y))
    return len(set(visited_positions))


def solve(inputs: list[str]) -> tuple[int, int]:
    instructions = preprocess_inputs(inputs)
    return part1(instructions), part2(instructions)
