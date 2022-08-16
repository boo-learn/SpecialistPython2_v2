class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):

        res = f'{self.value}{self.to_suit()}'
        return res

    def to_suit(self):
        res = ''
        if self.suit == 'Diamonds':
            # print('\u2662', '\u2666')
            res = '\u2666'
        elif self.suit == 'Hearts':
            # print('\u2661', '\u2665')
            res = '\u2665'
        elif self.suit == 'Spades':
            # print('\u2664', '\u2660')
            res = '\u2660'
        elif self.suit == 'Clubs':
            # print('\u2667', '\u2663')
            res = '\u2663'

        return res

    def equal_suit(self, other_card):

        return self.suit == other_card.suit


class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.cards = []
        # TODO-1: конструктор добавляет в список self.cards все(52) карты
        for suit in suits:
            for value in values:
                self.cards.append(Card(value, suit))

    def show(self):
        # TODO-2: Принцип работы данного метода прописан в 00_task_deck.md
        cards_str = []
        for value in self.cards:
            cards_str.append(value.to_str())

        res = ','.join(cards_str)
        return f'cards[{str(len(cards_str))}]{res}'


# Создаем колоду
deck = Deck()
# Выводим колоду в формате указанном в основном задании
print(deck.show())
