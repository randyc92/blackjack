import random

suits = ["Spades", "Heerts", "Diamonds", "Clubs"]

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]

deck = [(suit, card) for suit in suits for card in cards]

def card_values(card):
    if card[0] == ["Jack", "Queen", "King"]:
        value = 10
    elif card[0] == "Ace":
        value = 11
    else:
        value = int(card[0])
    
    return value