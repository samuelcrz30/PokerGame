from __future__ import annotations
from src.cards import Card, Hand
from src.roles import Player


def get_winner(
    players: list[Player], common_cards: list[Card], private_cards: list[list[Card]]
) -> tuple[Player | None, Hand]:

    first_player_hand = Hand(cards=private_cards[0] + common_cards, cat="", cat_rank="")
    second_player_hand = Hand(cards=private_cards[1] + common_cards, cat="", cat_rank="")

    if first_player_hand > second_player_hand:
        return players[0], first_player_hand
    elif first_player_hand < second_player_hand:
        return players[1], second_player_hand
    else:
        return None, first_player_hand
