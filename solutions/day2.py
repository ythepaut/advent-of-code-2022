"""
Advent of code 2022 - https://adventofcode.com/2022
Yohann THEPAUT (ythepaut) <contact@ythepaut.com>
"""

OPPONENT_TO_HAND = {"A": "ROCK", "B": "PAPER", "C": "SCISSORS"}
PLAY_TO_HAND = {"X": "ROCK", "Y": "PAPER", "Z": "SCISSORS"}
HAND_TO_PLAY = {"ROCK": "X", "PAPER": "Y", "SCISSORS": "Z"}

SCORES_FROM_HAND = {"ROCK": 1, "PAPER": 2, "SCISSORS": 3}

HAND_BEATS = {"ROCK": "SCISSORS", "PAPER": "ROCK", "SCISSORS": "PAPER"}
HAND_LOSES = {"ROCK": "PAPER", "PAPER": "SCISSORS", "SCISSORS": "ROCK"}


def preprocess_inputs(inputs: list[str]) -> list[tuple[str, str]]:
    rounds = []
    for input_ in inputs:
        opponent, response = input_[:-1].split(" ")
        rounds.append((OPPONENT_TO_HAND[opponent], PLAY_TO_HAND[response]))
    return rounds


def part1(rounds: list[tuple[str, str]]) -> int:
    score = 0
    for round_ in rounds:
        opponent, hand = round_
        score += SCORES_FROM_HAND[round_[1]]
        if hand == opponent:
            score += 3
        elif HAND_BEATS[hand] == opponent:
            score += 6
    return score


def part2(rounds: list[tuple[str, str]]) -> int:
    score = 0
    for round_ in rounds:
        opponent, result = round_[0], HAND_TO_PLAY[round_[1]]
        if result == "X":
            score += SCORES_FROM_HAND[HAND_BEATS[opponent]]
        elif result == "Y":
            score += SCORES_FROM_HAND[opponent] + 3
        elif result == "Z":
            score += SCORES_FROM_HAND[HAND_LOSES[opponent]] + 6
    return score


def solve(inputs: list[str]) -> tuple[int, int]:
    rounds = preprocess_inputs(inputs)
    return part1(rounds), part2(rounds)
