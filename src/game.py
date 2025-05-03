from __future__ import annotations
from src.cards import Card, Hand
from src.roles import Player
import src.helpers

def get_best_hand(cards: list[Card]) -> Hand:
    best = None
    for combination in src.helpers.combinations(cards, n=5):
        hand = Hand(list(combination), '0', '')
        cat, cat_rank = hand.winner_category()
        hand.cat = str(cat)
        hand.cat_rank = cat_rank
        if best is None or hand > best:
            best = hand
    return best


def get_winner(players: list[Player], common_cards: list[Card], private_cards: list[list[Card]]) -> tuple[Player | None, Hand]:
    def get_best_hand(cards: list[Card]) -> Hand: # POR VER, HECHO CON DEEP
        best = None
        for combo in src.helpers.combinations(cards, n=5):
            hand = Hand(list(combo), '', '')
            cat, cat_rank = hand.winner_category()
            hand.cat = cat
            hand.cat_rank = cat_rank
            if best is None or hand > best:
                best = hand
        return best
    
    # Asumimos que los inputs son correctos (según PDF)
    hand1 = get_best_hand(private_cards[0] + common_cards)
    hand2 = get_best_hand(private_cards[1] + common_cards)
    
    if hand1 > hand2:
        return players[0], hand1
    elif hand2 > hand1:
        return players[1], hand2
    return None, hand1  # Empate
