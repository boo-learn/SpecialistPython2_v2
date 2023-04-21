from deck_total import Card, Deck

# Важно! При решении задач данного блока классы Колоды и Карты размещаем в файле deck_total.py и импортируем

# TODO: Создайте колоду из 52 карт. Перемешайте ее. Вытяните две карты сверху.
#   Сравните эти карты и выведите сообщение формата: “карта A♦ больше J♣”
deck_52_cards = Deck()
deck_52_cards.shuffle()
card1, card2 = deck_52_cards.draw(2)
if card1 > card2:
    print(f"карта {card1} больше {card2}")
else:
    print(f"карта {card2} больше {card1}")
