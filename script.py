import random

suits = ["Spades", "Heerts", "Diamonds", "Clubs"]

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]

deck = [(suit, card) for suit in suits for card in cards]

def card_value(card):
    if card[1] in ["Jack", "Queen", "King"]:
        value = 10
    elif card[1] == "Ace":
        value = 11
    else:
        value = int(card[1])
    
    return value

random.shuffle(deck)

player_hand = [deck.pop(), deck.pop()]

dealer_hand = [deck.pop(), deck.pop()]


while True:
    player_score = sum(card_value(card) for card in player_hand)
    dealer_score = sum(card_value(card) for card in dealer_hand)
    print("Player cards are:", player_hand)
    print("Player score: ", player_score)
    print("\n")
    hit_or_stay = input("Hit me or stay?".lower())
    if hit_or_stay == "hit":
        new_card = deck.pop()
        player_hand.append(new_card)
    elif hit_or_stay == "stay":
        break
    else:
        print("invalid choice")
        continue

    if player_score > 21:
        print("Player cards are:", player_hand)
        print("Player score: ", player_score)
        print("Player cards are:", player_hand)
        print("Player score: ", player_score)
        print("Dealer wins")
        break

while dealer_score < 17:
    new_card = deck.pop()
    dealer_hand.append(new_card)
    dealer_score += card_value(new_card)
    print("Cards Dealer Has:", dealer_hand)
    print("Score Of The Dealer:", dealer_score)
    print("\n")
    
if dealer_score > 21:
    print("Player cards are:", player_hand)
    print("Player score: ", player_score)
    print("Dealeer cards are:", dealer_hand)
    print("Dealer score: ", dealer_score)
    print("Player wins")
elif dealer_score > player_score:
    print("Player cards are:", player_hand)
    print("Player score: ", player_score)
    print("Dealeer cards are:", dealer_hand)
    print("Dealer score: ", dealer_score)
    print("Dealer wins")
elif dealer_score < player_score:
    print("Player cards are:", player_hand)
    print("Player score: ", player_score)
    print("Dealeer cards are:", dealer_hand)
    print("Dealer score: ", dealer_score)
    print("Player wins")
else:
    print("Player cards are:", player_hand)
    print("Player score: ", player_score)
    print("Dealeer cards are:", dealer_hand)
    print("Dealer score: ", dealer_score)
    print("Draw")