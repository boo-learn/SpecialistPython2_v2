from deck_total import Card, Deck

deck = Deck()
deck.shuffle()

hand = deck.draw(10)
suits = {"Hearts": 0, "Diamonds": 0, "Spades": 0, "Clubs": 0}
for card in hand:
    suits[card.suit] += 1

max_count = 0
max_keys = set()
for key in suits:
    if suits[key] > max_count:
        max_count = suits[key]
        max_keys = {key}
    elif suits[key] == max_count:
        max_keys.add(key)

print("Больше всего карт масти - ", ', '.join(list(max_keys)))

# TODO: Создайте колоду из 52 карт. Перемешайте ее. Вытяните 10 карт сверху
#   и посчитайте карт какой/каких мастей среди вытянутых карт оказалось больше всего?
