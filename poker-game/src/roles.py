import cards


class Player:
    def __init__(self, name: str, private_cards):
        self.name = name
        self.private_cards_player = cards.Hand.cards
