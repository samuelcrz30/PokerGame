class Card:
    def __init__(self, id: str):
        self.id = id

    def cards_suits(self):
        self.suits = ("♥", "♠", "♦", "♣")
    
    def cards_values(self):
        self.values = {
        "1": 1, 
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
        "A": 14
        }


class Hand:
    def __init__(self, cards: list[str], cat: str, cat_rank: str | tuple):
        self.cards = []
        self.cat = cat
        self.cat_rank = cat_rank

    def __contains__(self, card: Card):
        return card in hand
