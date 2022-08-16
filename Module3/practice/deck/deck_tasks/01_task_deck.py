from deck_total import Card, Deck

deck = Deck()
# print(deck)
deck.shuffle()

card1, card2 = deck.draw(2)
if card1 > card2:
    print(f"карта {card1} больше {card2}")
else:
    print(f"карта {card1} меньше {card2}")
