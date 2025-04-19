from __future__ import annotations
import helpers


class Card:
    SORTED_VALUES = {
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

    SUITS = ['❤', '♠', '◆', '♣']

    def __init__(self, id: str):
        self.id = id
        self.value, self.suit, = self.id[:-1], self.id[-1]

    def __lt__(self, other: Card) -> bool:
        return Card.SORTED_VALUES[self.value] < Card.SORTED_VALUES[other.value]
    
    def __gt__(self, other: Card) -> bool:
        return Card.SORTED_VALUES[self.value] > Card.SORTED_VALUES[other.value]
    
    def __eq__(self, other) -> bool:
        return Card.SORTED_VALUES[self.value] == Card.SORTED_VALUES[other.value]


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
        self.cards = cards
        self.cat = cat
        self.cat_rank = cat_rank

    def __contains__(self, card: Card):
        return card in hand
    
    def sorted_cards(self, cards):
        sorted_cards = sorted(cards, key=lambda card: Card.SORTED_VALUES[card[0]])
        return sorted_cards
    
    def get_highest_card(self):
        return self.sorted_cards(self)[-1]
    
    def high_card(self):
        self.cat = Hand.HIGH_CARD
        return self.cat, self.get_highest_card
    
    def one_pair(self):
        for card in self.sorted_cards[::-1]:
            if self.count(card) == 2:
                self.cat = Hand.ONE_PAIR
                return self.cat, card
        return None
    
    def two_pair(self):
        num_of_pairs = 0
        highest_pairs = []
        for card in self.sorted_cards:
            if self.one_pair(self.sorted_cards):
                num_of_pairs += 1
                highest_pairs.append(Card.value)
            if num_of_pairs == 2:
                self.cat = Hand.TWO_PAIR
                return self.cat, tuple(highest_pairs)
        return None
    
    def three_of_a_kind(self):
        values = [value for value in Card.SORTED_VALUES.keys()]
        for value in values:
            if Card.values.count(value) == 3:
                self.cat = Hand.THREE_OF_A_KIND
                return self.cat, value
        return None
    
    def straight(self):
       return # por hacer

    def flush(self):
        first_suit = self.sorted_cards[0][1]
        if all(card[1] == first_suit for card in self.sorted_cards):
            self.cat = Hand.FLUSH
            return self.cat, self.get_highest_card
    
    def full_house(self):
        if self.one_pair and self.three_of_a_kind:
            self.cat = Hand.FULL_HOUSE
            return self.cat, tuple()

    def four_of_a_kind(self):
        values = [value for value in Card.SORTED_VALUES.keys()]
        for value in values:
            if Card.values.count(value) == 4:
                self.cat = Hand.THREE_OF_A_KIND
                return self.cat, value
        return None

    