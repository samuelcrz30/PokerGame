from __future__ import annotations

import cards
import roles

player = roles.Player
card = cards.Card
hand = cards.Hand


def get_winner(
    players: list[player], common_cards: list[card], private_cards: list[list[card]]
) -> tuple[player | None, hand]:
    player1 = players[0]
    player2 = players[1]
    cards_player1 = private_cards[0]
    cards_player2 = private_cards[1]
    player1_hand = player1.private_cards_player
    player2_hand = player2.private_cards_player

    # ejemploo
    return None, player1_hand


def get_best_hand(p1_hand, p2_hand):
    p1_hand.cards
    p2_hand.cards
