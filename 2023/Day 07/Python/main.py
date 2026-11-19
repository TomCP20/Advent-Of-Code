"""Advent of Code - 2023 - Day 7"""

from collections import Counter


def parse_hand(line: str):
    """Parses a line of input into a hand."""
    hand, bid = line.split()
    return (hand, int(bid))


def score_hand(cards: str, is_part_2: bool) -> int:
    """Calculates the hands score."""
    score = rank_card(cards[4], is_part_2)
    score += rank_card(cards[3], is_part_2) * 15
    score += rank_card(cards[2], is_part_2) * (15**2)
    score += rank_card(cards[1], is_part_2) * (15**3)
    score += rank_card(cards[0], is_part_2) * (15**4)
    score += rank_hand(cards, is_part_2) * (15**5)
    return score


def rank_hand(cards: str, is_part_2: bool) -> int:
    """Calculates the hands rank."""
    counts = Counter(cards)

    if is_part_2 and "J" in counts:
        joker_no = counts["J"]
        if joker_no == 5:
            return 7  # Five of a kind jokers
        del counts["J"]
        max_no = max(counts.values()) + joker_no
    else:
        max_no = max(counts.values())

    match len(counts):
        case 1:  # Five of a kind
            return 7
        case 2:
            if max_no == 4:  # Four of a kind
                return 6
            return 5  # Full house
        case 3:
            if max_no == 3:  # Three of a kind
                return 4
            return 3  # Two pair
        case 4:  # One pair
            return 2
        case 5:
            return 1  # High card
        case _:
            print(f"invalid cards {cards}.")
            return 0


def rank_card(card: str, is_part_2: bool) -> int:
    """Returns the rank of the card."""
    match card:
        case "A":
            return 14
        case "K":
            return 13
        case "Q":
            return 12
        case "J":
            return 1 if is_part_2 else 11
        case "T":
            return 10
        case _:
            if card.isdigit():
                return int(card)
            print(f"invalid card {card}.")
            return 0


def calc_winnings(hands: list[tuple[str, int]]):
    """Calculates the total winnings."""
    return sum(i * bid for i, (_, bid) in enumerate(hands, 1))


def main():
    """Solves Part 1 and 2 of Day 7"""
    with open(0, encoding="utf-8") as f:
        lines = f.read().splitlines()
        hands = [parse_hand(line) for line in lines]
    hands = sorted(hands, key=lambda h: score_hand(h[0], False))
    print(calc_winnings(hands))
    hands = sorted(hands, key=lambda h: score_hand(h[0], True))
    print(calc_winnings(hands))


main()
