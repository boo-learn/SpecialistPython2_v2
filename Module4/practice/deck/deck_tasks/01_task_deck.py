from deck_total import Card, Deck


desk1 = Deck()

desk1.shuffle()

card1, card2 = desk1.draw(2)

if card1 > card2:
    print(f"{card1} больше {card2}")
if card1< card2:
    print(f"{card1} меньше {card2}")
