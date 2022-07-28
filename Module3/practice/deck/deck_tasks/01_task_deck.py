from deck_total import Card, Deck

# Важно! При решении задач данного блока классы Колоды и Карты размещаем в файле deck_total.py и импортируем

# TODO: Создайте колоду из 52 карт. Перемешайте ее. Вытяните две карты сверху.
#   Сравните эти карты и выведите сообщение формата: “карта A♦ больше J♣”



deck1 = Deck()

deck1.shuffle()

card1 , card2 = deck1.draw(2)


if card1 < card2:  # card1.__gt__(card2)
    print(f"{card1} меньше {card2}")
else:
    print(f"{card1} больше {card2}")
