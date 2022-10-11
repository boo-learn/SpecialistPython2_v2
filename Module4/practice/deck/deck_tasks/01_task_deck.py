from deck_total import Card, Deck

# Важно! При решении задач данного блока классы Колоды и Карты размещаем в файле deck_total.py и импортируем

# TODO: Создайте колоду из 52 карт. Перемешайте ее. Вытяните две карты сверху.
#   Сравните эти карты и выведите сообщение формата: “карта A♦ больше J♣”

deck = Deck()
deck.shuffle()
card1, card2 = deck.draw(2)
if card1 > card2:
    print(f'карта {card1} больше {card2}')
else:
    print(f'карта {card1} меньше {card2}')
