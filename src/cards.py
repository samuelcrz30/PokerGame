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

    def __eq__(self, other: Card) -> bool:
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
        return card in self.cards

    def sorted_cards(self):
        return sorted(self.cards, key=lambda card: Card.SORTED_VALUES[card.value])

    def get_highest_card(self):
        return self.sorted_cards()[-1]

    def high_card(self):
        self.cat = Hand.HIGH_CARD
        return self.cat, self.get_highest_card().value

    def one_pair(self):
        card_values = [card.value for card in self.cards]
        for card in reversed(Card.SORTED_VALUES):
            if card_values.count(card) == 2:
                self.cat = Hand.ONE_PAIR
                return self.cat, card
        return None

    def two_pair(self):
        card_values = [card.value for card in self.cards]
        pairs = []
        for card in reversed(Card.SORTED_VALUES):
            if card_values.count(card) == 2:
                pairs.append(card)
            if len(pairs) == 2:
                self.cat = Hand.TWO_PAIR
                return self.cat, tuple(pairs)
        return None

    def three_of_a_kind(self):
        card_values = [card.value for card in self.cards]
        for card in reversed(Card.SORTED_VALUES):
            if card_values.count(card) == 3:
                self.cat = Hand.THREE_OF_A_KIND
                return self.cat, card
        return None

    def straight(self):
        values = sorted(set(Card.SORTED_VALUES[card.value] for card in self.cards))

        if len(values) < 5:
            return None

        counter = 1
        for i in range(1, len(values)):
            if values[i] == values[i - 1] + 1:
                counter += 1
                if counter == 5:
                    self.cat = Hand.STRAIGHT
                    high_value = values[i]
                    for char, num in Card.SORTED_VALUES.items():
                        if num == high_value:
                            return self.cat, char
            else:
                counter = 1

        return None

    def flush(self):
        for suit in Card.SUITS:
            same_cards = [card for card in self.cards if card.suit == suit]
            if len(same_cards) >= 5:
                best_cards = sorted(same_cards)[-5:]
                self.cat = Hand.FLUSH
                return self.cat, best_cards[-1].value
        return None

    def full_house(self):
        three = self.three_of_a_kind()
        pair = self.one_pair()
    
        if three and pair and three[1] != pair[1]:
            self.cat = Hand.FULL_HOUSE
            return self.cat, (three[1], pair[1])
        return None

    def four_of_a_kind(self):
        card_values = [card.value for card in self.cards]
        for card in reversed(Card.SORTED_VALUES):
            if card_values.count(card) == 4:
                self.cat = Hand.THREE_OF_A_KIND
                return self.cat, card
        return None

    def straight_flush(self):
            for s in Card.SUITS:
                suited = [c for c in self.cards if c.suit == s]
                if len(suited) >= 5:
                    values = sorted(set(Card.SORTED_VALUES[c.value] for c in suited))
                    for i in range(len(values) - 4):
                        if values[i + 4] - values[i] == 4:
                            for k, v in Card.SORTED_VALUES.items():
                                if v == values[i + 4]:
                                    self.cat = Hand.STRAIGHT_FLUSH
                                    return self.cat, k
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
        return self.high_card()

    def __iter__(self):
        for card in self.hand:
            yield card

    def __lt__(self, other: Hand) -> bool:
        return self.winner_category() < other.winner_category()

    def __eq__(self, other: Hand) -> bool:
        return self.winner_category() == other.winner_category()

    def __gt__(self, other: Hand) -> bool:
        return self.winner_category() > other.winner_category()


    
