from deck_total import Card, Deck

# Важно! При решении задач данного блока классы Колоды и Карты размещаем в файле deck_total.py и импортируем

# TODO: Создайте колоду из 52 карт. Перемешайте ее. Вытяните две карты сверху.
#   Сравните эти карты и выведите сообщение формата: “карта A♦ больше J♣”

# Создаем колоду
deck = Deck()
# Тусуем колоду
deck.shuffle()
print(deck)
# Берем две карты из колоды
card1, card2 = deck.draw(2)

# Тестируем методы .less() и .more()
if card1 > card2:
    print(f"{str(card1)} больше {str(card2)}")
if card1 < card2:
    print(f"{str(card1)} меньше {str(card2)}")
