from __future__ import annotations
from helpers import combinations
import card
import game

class Player:
    def __init__(self, name: str):
        self.name = name
        self.private_cards = []

    def obtain_best_hand(self):
        available_cards = self.private_cards + game.get_common_cards
        all_posible_combinations = list(combinations(available_cards, n=5))
        first_combination = all_posible_combinations[0]
        for combination in all_posible_combinations:
            if combination > first_combination:
                first_combination = combination
            elif combination == first_combination
        



