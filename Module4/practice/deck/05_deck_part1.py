import itertools


class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        icons = {"Hearts": '\u2665',
                 "Diamonds": '\u2666',
                 "Clubs": '\u2667',
                 "Spades": '\u2664'
                 }
        return f"{self.value}{icons.get(self.suit)}"

    def equal_suit(self, other_card):
        return self.suit == other_card.suit


class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.cards = [Card(value, suite) for suite, value in itertools.product(suits, values)]
        # конструктор добавляет в список self.cards все(52) карты

    def show(self):
        return f'deck[{len(self.cards)}]: {", ".join([card.to_str() for card in self.cards])}'


# Создаем колоду
deck = Deck()
# Выводим колоду в формате указанном в основном задании
print(deck.show())
