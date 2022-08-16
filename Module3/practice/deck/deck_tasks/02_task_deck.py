from deck_total import Card, Deck
from collections import Counter

# TODO: Создайте колоду из 52 карт. Перемешайте ее. Вытяните 10 карт сверху
#   и посчитайте карт какой/каких мастей среди вытянутых карт оказалось больше всего?

# Создаем колоду
deck = Deck()
# Тусуем колоду
deck.shuffle()
print(deck)
# Берем две карты из колоды

def suit_count():
    suits = []
    cards = deck.draw(10)
    for card in cards:
        suits.append(card.suit)
    counter = Counter(suits)
    return max(counter, key=counter.get)

print(suit_count())
