from __future__ import annotations


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

    SUITS = ["❤", "♠", "◆", "♣"]

    def __init__(self, id: str):
        self.id = id
        (
            self.value,
            self.suit,
        ) = (
            self.id[:-1],
            self.id[-1],
        )

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

    def __init__(self, cards: list[Card], cat: str, cat_rank: str | tuple):
        self.cards = cards
        self.cat = cat
        self.cat_rank = cat_rank

    def __contains__(self, card):
        return card in self.hand

    def sorted_cards(self):
        return sorted(self.cards, key=lambda card: Card.SORTED_VALUES[card.value])

    def get_highest_card(self):
        return self.sorted_cards()[-1]

    def high_card(self):
        self.cat = Hand.HIGH_CARD
        return self.cat, self.get_highest_card

    def one_pair(self):
        card_values = []
        for card in self.cards:
            card_values.append(card.value)
        for value in Card.SORTED_VALUES.keys():
            if card_values.count(value) == 2:
                self.cat = Hand.ONE_PAIR
                return self.cat, value

        return None

    def two_pair(self):
        _, first_pair = self.one_pair()
        if first_pair:
            aux_cards = self.cards.copy()
            self.cards.remove(first_pair)
            var2 = self.one_pair()
            self.cards = aux_cards
            # nos guardamos un copy, para manipular las cartas dandonos igual
            # luego cogemos, manipulamos los datos finalmente cuando encontremos la 2a pareja dejamos todo como estaba
            if var2:
                return Hand.TWO_PAIR, [first_pair, var2]
        return None

    def three_of_a_kind(self):
        card_values = []
        for card in self.cards:
            card_values.append(card.value)
        for value in Card.SORTED_VALUES.keys():
            if card_values.count(value) == 3:
                self.cat = Hand.THREE_OF_A_KIND
                return self.cat, value

        return None

    def straight(self):
        first_card = self.sorted_cards()[0]
        all_cards = self.sorted_cards()
        for card in all_cards[1:]:
            if Card.SORTED_VALUES[card.value] != Card.SORTED_VALUES[first_card.value] + 1: 
                return None
            first_card += 1
        self.cat = Hand.STRAIGHT
        return self.cat, self.get_highest_card()

    def flush(self):
        first_suit = self.sorted_cards()[0].value
        if all(card.value == first_suit for card in self.sorted_cards()):
            self.cat = Hand.FLUSH
            
            return self.cat, self.get_highest_card()
        return None

    def full_house(self):
        if self.one_pair() and self.three_of_a_kind():
            self.cat = Hand.FULL_HOUSE
            return self.cat, tuple(self.three_of_a_kind()[1], self.one_pair())

    def four_of_a_kind(self):
        card_values = []
        for card in self.cards:
            card_values.append(card.value)
        for value in Card.SORTED_VALUES.keys():
            if card_values.count(value) == 4:
                self.cat = Hand.FOUR_OF_A_KIND
                return self.cat, value

        return None

    def straight_flush(self):
        if self.flush() and self.straight():
            self.cat = Hand.STRAIGHT_FLUSH
            return self.cat, self.highest_card()
        return None

    def winner_category(self) -> tuple[int, str | tuple[str, str]]:
        checkers = [
            self.straight_flush,
            self.four_of_a_kind,
            self.full_house,
            self.flush,
            self.straight,
            self.three_of_a_kind,
            self.two_pair,
            self.one_pair,
        ]

        for check in checkers:
            result = check()
            if result:
                return result
        return self.get_highest_card()

    def __iter__(self):
        for card in self.hand:
            yield card

    def __lt__(self, other: Hand) -> bool:
        return self.winner_category()[0] < other.winner_category()[0]

    def __eq__(self, other: Hand) -> bool:
        return self.winner_category()[0] == other.winner_category()[0]

    def __gt__(self, other: Hand) -> bool:
        return self.winner_category()[0] > other.winner_category()[0]
