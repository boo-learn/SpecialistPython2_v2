class Card:
    # TODO-0: сюда копируем реализацию класса карты из предыдущего задания
    ...


class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.cards = []
        for s in suits :
            for v in values:
                self.cards.append(Card(v, s))
        # TODO-1: конструктор добавляет в список self.cards все(52) карты

    def show(self):
        cardst = []
        cardcnt = 0
        for c in self.cards:
            cardst.append(c.to_str())
            cardcnt += 1
        return f"cards[{cardcnt}], {','.join(cardst)}"


# Создаем колоду
deck = Deck()
# Выводим колоду в формате указанном в основном задании
print(deck.show())
