"""
Advent of code 2022 - https://adventofcode.com/2022
Yohann THEPAUT (ythepaut) <contact@ythepaut.com>
"""
from dataclasses import dataclass
from typing import Any

DIRECTORY_COUNT_THRESHOLD = 100_000
TOTAL_SPACE = 70_000_000
NEEDED_SPACE = 30_000_000


@dataclass
class File:
    name: str
    size: int


@dataclass
class Directory:
    name: str
    parent: Any
    children: list


Node = Directory | File


def preprocess_inputs(inputs: list[str]) -> list[str]:
    return list(map(lambda input_: input_[:-1], inputs))


def list_directory(commands: list[str], current_directory: Directory) -> list[Node]:
    nodes: list[Node] = []
    i = 0
    while i < len(commands) and not commands[i].startswith("$"):
        args = commands[i].split(" ")
        if commands[i].startswith("dir"):
            nodes.append(Directory(args[1], current_directory, []))
        else:
            nodes.append(File(args[1], int(args[0])))
        i += 1
    return nodes


def construct_tree(commands: list[str]) -> Directory:
    assert commands[0] == "$ cd /"
    root_directory = Directory("/", None, [])
    current_directory = root_directory
    i = 1
    while i < len(commands):
        command = commands[i]
        if command == "$ ls":
            # Retrieve nodes in directory
            nodes = list_directory(commands[i+1:], current_directory)
            current_directory.children.extend(nodes)
            i += len(nodes) + 1
        else:
            # Change directory
            directory_name = command.split(" ")[2]
            if directory_name == "..":
                current_directory = current_directory.parent
            else:
                current_directory = list(filter(
                    lambda node: node.name == directory_name, current_directory.children
                ))[0]
            i += 1
    return root_directory


def print_tree(node: Node, indentation: str = "") -> None:
    print(f"""{indentation}{node.name}\t({'dir' if isinstance(node, Directory) else 'file'}, {get_node_size(node)})""")
    if isinstance(node, Directory):
        for child in node.children:
            print_tree(child, indentation + "  ")


def get_node_size(node: Node) -> int:
    if isinstance(node, File):
        return node.size
    total = 0
    for child in node.children:
        total += get_node_size(child)
    return total


def part1(node: Node) -> int:
    if isinstance(node, File):
        return 0
    node_size: int = get_node_size(node)
    current_size = node_size if node_size < DIRECTORY_COUNT_THRESHOLD else 0
    return current_size + sum(map(part1, node.children))


def get_directory_sizes(node: Node) -> list[int]:
    if isinstance(node, File):
        return []
    sizes = [get_node_size(node)]
    for child in node.children:
        sizes.extend(get_directory_sizes(child))
    return sizes


def part2(tree: Directory) -> int:
    directory_sizes = get_directory_sizes(tree)
    space_to_free = (TOTAL_SPACE - get_node_size(tree) - NEEDED_SPACE) * -1
    return min(list(filter(lambda size: size >= space_to_free, directory_sizes)))


def solve(inputs: list[str]) -> tuple[int, int]:
    commands = preprocess_inputs(inputs)
    tree = construct_tree(commands)
    return part1(tree), part2(tree)
