from deck_total import Card, Deck

# TODO: Создайте колоду из 52 карт. Перемешайте ее. Вытяните 10 карт сверху
#   и посчитайте карт какой/каких мастей среди вытянутых карт оказалось больше всего?

deck = Deck()
deck.shuffle()
hand = deck.draw(10)

for card in hand:
    print(card, end=" ")

suits_count = {"Hearts": 0, "Diamonds": 0, "Spades": 0, "Clubs": 0}

for card in hand:
    suits_count[card.suit] += 1
print()
max_cards = max(suits_count.values())
for key, value in suits_count.items():
    if value == max_cards:
        print(f"{key} - {value}")
