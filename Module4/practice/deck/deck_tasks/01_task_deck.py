from deck_total import Card, Deck

# Важно! При решении задач данного блока классы Колоды и Карты размещаем в файле deck_total.py и импортируем

# TODO: Создайте колоду из 52 карт. Перемешайте ее. Вытяните две карты сверху.
#   Сравните эти карты и выведите сообщение формата: “карта A♦ больше J♣”

deck = Deck()
deck.shuffle()
hand = deck.draw(2)
print(deck)
print(hand)

if hand[0] < hand[1]:
    print(f"{hand[0]} меньше {hand[1]}")
elif hand[0] > hand[1]:
    print(f"{hand[0]} больше {hand[1]}")
else:
    print(f"{hand[0]} равно {hand[1]}")
