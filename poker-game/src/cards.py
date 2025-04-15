from __future__ import annotations


class Card:
    VALUES = {
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 14,
    }
    SUITS = ('❤', '◆', '♣', '♠')

    def __init__(self, id: str):
        self.id = id
        self.rank = id[:1]
        self.suit = id[1:]
        self.value = Card.VALUES[self.rank]

    def __lt__(self, other: Card):
        return self.value < other.value


class Hand:
    cat_values = {
        'HIGH_CARD': 1,
        'ONE_PAIR': 2,
        'TWO_PAIR': 3,
        'THREE_OF_A_KIND': 4,
        'STRAIGHT': 5,
        'FLUSH': 6,
        'FULL_HOUSE': 7,
        'FOUR_OF_A_KIND': 8,
        'STRAIGHT_FLUSH': 9,
    }

    def __init__(self, cards: list[Card], cat: str, cat_rank: str | tuple):
        self.cards = sorted(cards, reverse=True)
        self.cat = cat
        self.cat_rank = cat_rank

    def __contains__(self, card: Card):
        return card in self.cards
