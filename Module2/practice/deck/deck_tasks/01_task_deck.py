# Создайте колоду из 52 карт. Перемешайте ее. Вытяните две карты сверху.
# Сравните эти карты и выведите сообщение формата: “карта A♦ больше J♣”
from deck_total import Deck

deck = Deck()
deck.shuffle()
card1, card2 = deck.draw(2)
if card2 > card1:
    print(f"Карта {card2} больше {card1}")
elif card2 < card1:
    print(f"Карта {card2} меньше {card1}")
