class Card:
    # TODO-0: сюда копируем реализацию класса карты из предыдущего задания

    # TODO-1: реализуем новые методы
    def more(self, other_card):
        ...

    def less(self, other_card):
        ...


class Deck:
    # TODO-0: сюда копируем реализацию класса колоды из предыдущего задания
    ...


# Создаем колоду
deck = Deck()
# Тусуем колоду
deck.shuffle()
print(deck.show())
# Берем две карты из колоды
card1, card2 = deck.draw(2)

# Тестируем методы .less() и .more()
if card1.more(card2):
    print(f"{card1.to_str()} больше {card2.to_str()}")
if card1.less(card2):
    print(f"{card1.to_str()} меньше {card2.to_str()}")
