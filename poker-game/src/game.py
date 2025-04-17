from cards import Card

def get_winner(players: list[Player], common_cards: list[Card], private_cards: list[list[Card]])-> tuple[Player | None, Hand]:
    player1 = players[0]
    player2 = players[1]
    player1_cards = private_cards[0]
    player2_cards = private_cards[1]
    pass

def get_common_cards(common_cards: list[Card]):
    return common_cards


    
