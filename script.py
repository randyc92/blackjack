import random

suits = ["Spades", "Heerts", "Diamonds", "Clubs"]

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]

deck = [(suit, card) for suit in suits for card in cards]

print(deck)
