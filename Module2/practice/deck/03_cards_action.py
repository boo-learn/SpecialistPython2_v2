
values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
cards = []
for value in values:
    for suit in suits:
        deck_card = Card(value, suit)
        cards.append(deck_card)


print(f" cards {len(cards)}", end = "")
for card in cards:

    print(f" {card.to_str()}", end=", ")
