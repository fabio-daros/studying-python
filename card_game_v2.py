"""
Type Hints to a game using more types.

"""

# Example Card Games v1 with type hints --------------------------------------------------------------

import random

from typing import List, Tuple

suits = '♠ ♡ ♢ ♣'.split()  # To copy the icons: https://www.alt-codes.net/suit-cards.php
cards = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

CARD = Tuple[str, str]
DECK = List[CARD]


def create_deck(random_1: bool = False) -> DECK:
    """Create a deck with 52 cards to play"""
    deck = [(s, c) for c in cards for s in suits]
    if random_1:
        random.shuffle(deck)
    return deck


# print(create_deck())  #  list of tuples


def distribute_cards(deck: DECK) -> Tuple[DECK, DECK, DECK, DECK]:
    """Distribute the cards in the deck"""
    return deck[0::4], deck[1::4], deck[2::4], deck[3::4]


deck = create_deck()


# print(distribute_cards(deck))

def play() -> None:
    """start playing cards to four players"""
    cards_1 = create_deck(random_1=True)
    players = 'P1 P2 P3 P4'.split()
    hands = {p: h for p, h in zip(players, distribute_cards(cards_1))}

    for player, cards_1 in hands.items():
        cards_1 = ' '.join(f'{p}{c}' for (p, c) in cards_1)
        print(f'{player}: {cards_1}')


if __name__ == "__main__":
    play()
