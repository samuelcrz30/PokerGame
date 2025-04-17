from __future__ import annotations
import helpers


class Card:
    VALUES = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
        "A": 14,
    }

    def __init__(self, id: str):
        self.id = id
        self.suit, self.value = self.id[-1], self.id[:-1]

    def __lt__(self, other: Card) -> bool:
        return Card.VALUES[self.value] < Card.VALUES[other.value]
    
    def __gt__(self, other: Card) -> bool:
        return Card.VALUES[self.value] > Card.VALUES[other.value]
    
    def __eq__(self, other) -> bool:
        return Card.VALUES[self.value] == Card.VALUES[other.value]


class Hand:
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    STRAIGHT = 5
    FLUSH = 6
    FULL_HOUSE = 7
    FOUR_OF_A_KIND = 8
    STRAIGHT_FLUSH = 9

    def __init__(self, cards: list[str], cat: str, cat_rank: str | tuple):
        self.cards = []
        self.cat = cat
        self.cat_rank = cat_rank

    def __contains__(self, card: Card):
        return card in hand
