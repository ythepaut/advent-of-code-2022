"""
Advent of code 2022 - https://adventofcode.com/2022
Yohann THEPAUT (ythepaut) <contact@ythepaut.com>
"""
import re
from dataclasses import dataclass
import copy

Stack = list[str]


@dataclass
class Instruction:
    amount: int
    stack_from: int
    stack_to: int


def preprocess_inputs(inputs: list[str]) -> tuple[list[Stack], list[Instruction]]:
    # Get stacks
    i = 0
    groups = []
    while "[" in inputs[i]:
        raw_groups = re.findall(r"(\[[A-Z]]\s|\s{4})", inputs[i])
        groups.append(list(map(lambda group: re.sub(r"[\[\]\s\n]", "", group), raw_groups)))
        i += 1
    # Transpose groups to get stacks
    stacks = [[] for _ in range(len(groups[0]))]
    for group in groups:
        for j, letter in enumerate(group):
            letter = group[j]
            if letter != "":
                stacks[j].insert(0, letter)

    # Get instructions
    instructions = []
    for instruction in inputs[i + 2:]:
        amount, stack_from, stack_to = re.findall(r"move (\d+) from (\d+) to (\d+)", instruction)[0]
        instructions.append(Instruction(int(amount), int(stack_from) - 1, int(stack_to) - 1))
    return stacks, instructions


def move_crate_stack(stacks: list[Stack], instruction: Instruction) -> None:
    for _ in range(instruction.amount):
        crate = stacks[instruction.stack_from][-1]
        stacks[instruction.stack_from].pop()
        stacks[instruction.stack_to].append(crate)


def read_message(stacks: list[Stack]) -> str:
    return "".join([stack[-1] for stack in stacks])


def part1(stacks: list[Stack], instructions: list[Instruction]) -> str:
    for instruction in instructions:
        move_crate_stack(stacks, instruction)
    return read_message(stacks)


def move_crate_queue(stacks: list[Stack], instruction: Instruction) -> None:
    stack_from = stacks[instruction.stack_from]
    crates = stack_from[len(stack_from) - instruction.amount:]
    for _ in range(instruction.amount):
        stack_from.pop()
    stacks[instruction.stack_to] += crates


def part2(stacks: list[Stack], instructions: list[Instruction]) -> str:
    for instruction in instructions:
        move_crate_queue(stacks, instruction)
    return read_message(stacks)


def solve(inputs: list[str]) -> tuple[str, str]:
    stacks, instructions = preprocess_inputs(inputs)
    return part1(copy.deepcopy(stacks), instructions), part2(copy.deepcopy(stacks), instructions)
