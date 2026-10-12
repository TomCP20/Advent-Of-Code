"""Advent of Code - 2023 - Day 2"""

import re

RED = 12
GREEN = 13
BLUE = 14


def get_game_id(game: str) -> int:
    """Finds the game id"""
    match = re.prefixmatch(r"Game (\d+)", game)
    if match:
        return int(match.group(1))
    print("Could not find id")
    return 0


def is_game_possible(game: str) -> bool:
    """Checks if a game is possible"""
    match = re.prefixmatch(r"^Game \d+: (.+)$", game)
    if match:
        rounds = match.group(1).split("; ")
        result = all(is_round_possible(round) for round in rounds)

        return result
    print("Could not find game")
    return False


def is_round_possible(game_round: str) -> bool:
    """Checks if a round is possible"""
    return (
        is_color_possible(game_round, "red", RED)
        and is_color_possible(game_round, "green", GREEN)
        and is_color_possible(game_round, "blue", BLUE)
    )


def is_color_possible(game_round: str, color: str, max_cube_num: int) -> bool:
    """Checks if a color is possible"""
    search = re.search(r"(\d+) " + color, game_round)
    cube_num = int(search.group(1)) if search else 0
    return cube_num <= max_cube_num


def get_game_power(game: str) -> int:
    """Gets the power of a game"""
    return (
        get_game_min_color(game, "red")
        * get_game_min_color(game, "green")
        * get_game_min_color(game, "blue")
    )


def get_game_min_color(game: str, color: str) -> int:
    """gets the minimum color for a game"""
    match = re.prefixmatch(r"^Game \d+: (.+)$", game)
    if match:
        rounds = match.group(1).split("; ")
        return max(get_round_color_num(round, color) for round in rounds)
    print("couldn't find rounds")
    return 0


def get_round_color_num(game_round: str, color: str) -> int:
    """gets the number of a colour for a round"""
    search = re.search(r"(\d+) " + color, game_round)
    return int(search.group(1)) if search else 0


def main():
    """Solves Part 1 and 2 of Day 2"""
    with open(0, encoding="utf-8") as f:
        games = f.read().splitlines()
    print(sum(get_game_id(game) for game in games if is_game_possible(game)))
    print(sum(get_game_power(game) for game in games))


main()
