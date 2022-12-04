class Card:
    # TODO-0: сюда копируем реализацию класса карты из предыдущего задания
    ...


class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.cards = []
        # TODO-1: конструктор добавляет в список self.cards все(52) карты
        for suit in suits:
           for value in values:
               card = Card(value, suit)
               self.cards.append(card)
    def show(self):
        # TODO-2: Принцип работы данного метода прописан в 00_task_deck.md
        result = f"cards[{len(self.cards)}]{', '.join([card.to_str() for card in self.cards])}"
        return result


# Создаем колоду
deck = Deck()
# Выводим колоду в формате указанном в основном задании
print(deck.show())
