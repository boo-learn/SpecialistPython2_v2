class Card:
    pass

    # TODO: сюда копируем реализацию класса карты из предыдущего задания


class Deck:
    pass
    # TODO: сюда копируем реализацию класса колоды из предыдущего задания


deck = Deck()
# Задачи - реализовать нативную работу с объектами:
# 1. Вывод колоды в терминал:
print(deck)  # вместо print(deck.show())

card1, card2 = deck.draw(2)
# 2. Вывод карты в терминал:
print(card1)  # вместо print(card1.to_str())

# 3. Сравнение карт:
if card1 > card2:
    print(f"{card1} больше {card2}")

# 4. Итерация по колоде:
for card in deck:
    print(card)

# Просмотр карты в колоде по ее индексу:
print(deck[6])


# Список ВСЕХ magic-методов см. тут: http://pythonworld.ru/osnovy/peregruzka-operatorov.html
