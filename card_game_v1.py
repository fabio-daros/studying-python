"""
Type Hints to a game using more types.


names: list = ['[Game Name 1]', '[Game Name 2]', '[Game Name 3]']

version: tuple = (3, 4, 5)

options: dict = {'module_1': True, 'module_2': True}

values: set = {3, 4, 5, 7}

print(names)

print(version)

print(options)

print(values)

print(__annotations__)

"""

# Example_1 --------------------------------------------------------------

"""
from typing import Dict, List, Tuple, Set

names: List[str] = ['Game Name 1', 'Game Name 2']

version: Tuple[int, int, int] = (3, 4, 5)

options: Dict[str, bool] = {'module_1': True, 'module_2': True}

values: Set[int] = {3, 4, 5, 7}

print(names)

print(version)

print(options)

print(values)

print(__annotations__)
"""

# Example_2 Card Games v1 without type hints --------------------------------------------------------------

import random

suits = '♠ ♡ ♢ ♣'.split()  # To copy the icons: https://www.alt-codes.net/suit-cards.php
cards = '2 3 4 5 6 7 8 9 10 J Q K A'.split()


def create_deck(random_1=False):
    """Create a deck with 52 cards to play"""
    deck = [(s, c) for c in cards for s in suits]
    if random_1:
        random.shuffle(deck)
    return deck


# print(create_deck())  #  list of tuples


def distribute_cards(deck):
    """Distribute the cards in the deck"""
    return deck[0::4], deck[1::4], deck[2::4], deck[3::4]


deck = create_deck()


# print(distribute_cards(deck))

def play():
    """start playing cards to four players"""
    cards = create_deck(random_1=True)
    players = 'P1 P2 P3 P4'.split()
    hands = {p: h for p, h in zip(players, distribute_cards(cards))}

    for player, cards in hands.items():
        cards = ' '.join(f'{p}{c}' for (p, c) in cards)
        print(f'{player}: {cards}')


if __name__ == "__main__":
    play()
