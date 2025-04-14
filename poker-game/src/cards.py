class Card:
    SUITS = ('❤', '◆', '♣', '♠')
    VALUES = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')

    def __init__(self, id: str):
        self.id = id


class Hand:
    def __init__(self, cards: list[str], cat: str, cat_rank: str | tuple):
        self.cards = []
        self.cat = cat
        self.cat_rank = cat_rank

    def __contains__(self, card: Card):
        return card in hand
