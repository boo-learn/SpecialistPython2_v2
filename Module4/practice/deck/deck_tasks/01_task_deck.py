from deck_total import Card, Deck

# Важно! При решении задач данного блока классы Колоды и Карты размещаем в файле deck_total.py и импортируем

# TODO: Создайте колоду из 52 карт. Перемешайте ее. Вытяните две карты сверху.

deck1 = Deck()
deck1.shuffle()
two_cards = deck1.draw(2)
print(two_cards)
if two_cards[0] > two_cards[1]:
    print(f'Карта {two_cards[0]} больше {two_cards[1]}')
else:
    print(f'Карта {two_cards[0]} меньше {two_cards[1]}')
#   Сравните эти карты и выведите сообщение формата: “карта A♦ больше J♣”

