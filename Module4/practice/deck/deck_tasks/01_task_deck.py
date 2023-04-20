
from deck_total import Card, Deck

# TODO: Создайте колоду из 52 карт. Перемешайте ее. Вытяните две карты сверху.
#   Сравните эти карты и выведите сообщение формата: “карта A♦ больше J♣”

new_deck = Deck()
new_deck.shuffle()

card1 = new_deck[0]
card2 = new_deck[1]

# Тестируем методы .less() и .more()
if card1 > card2:
    print(f"карта {card1} больше {card2}")
if card1 < card2:
    print(f"карта {card1} меньше {card2}")
