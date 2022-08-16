from deck_total import Card, Deck

deck1 = Deck()
deck2 = Deck()

while deck2.cards:
    deck1.cards.append(deck2.draw(1)[0])

deck1.shuffle()

for i in range(52):
    deck1.draw(1)

suits = {"Hearts": 0, "Diamonds": 0, "Spades": 0, "Clubs": 0}
for card in deck1:
    suits[card.suit] += 1

max_count = 0
max_keys = set()
for key in suits:
    if suits[key] > max_count:
        max_count = suits[key]
        max_keys = {key}
    elif suits[key] == max_count:
        max_keys.add(key)

print("Больше всего карт масти - ", ', '.join(max_keys))

# TODO: Создайте две колоды по 52 карты. Перемешайте их вместе - в итоге получится одна колода из 104 карт.
#   Выбросите/вытяните половину карт. Узнайте, какой/каких мастей в колоде осталось больше всего?
