"""Advent of Code - 2023 - Day 4"""

import re


def get_game_count(game: str):
    """Calculates the count of winning numbers in my numbers for a game"""
    match = re.match(r"^Card [ \d]{2}\d: ([ \d]{29}) [|] ([ \d]{74})$", game)
    assert match
    winning_numbers = set(map(int, match.group(1).split()))
    my_numbers = set(map(int, match.group(2).split()))
    count = len(winning_numbers & my_numbers)
    return count


def get_game_score(game: str):
    """Calculates the score of a game"""
    count = get_game_count(game)
    if count == 0:
        return 0
    return 2 ** (count - 1)


def main():
    """Solves Part 1 and 2 of Day 4"""
    with open(0, encoding="utf-8") as f:
        games = f.read().splitlines()

    print(sum(map(get_game_score, games)))

    card_counts = [1] * len(games)
    for i, game in enumerate(games):
        score = get_game_count(game)
        for j in range(1, min(score + 1, len(games))):
            card_counts[i + j] += card_counts[i]
    print(sum(card_counts))


main()
