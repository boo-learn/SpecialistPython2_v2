import random


class Card:
    # TODO-0: сюда копируем реализацию класса карты из предыдущего задания
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        # TODO-1: метод возвращает строковое представление карты в виде: 10♥ и A♦
        suits = {'Hearts': '\u2665', 'Diamonds': '\u2666', 'Clubs': '\u2667', 'Spades': '\u2664'}
        return f'{self.value}{suits[self.suit]}'


class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.cards = []
        for suit in suits:
            for value in values:
                self.cards.append(Card(value, suit))
        # TODO-1: конструктор добавляет в список self.cards все(52) карты

    def show(self):
        # TODO-2: Принцип работы данного метода прописан в 00_task_deck.md
        return f"cards[{len(self.cards)}]{', '.join([card.to_str() for card in self.cards])}"

    def draw(self, x):
        # TODO-1: Принцип работы данного метода прописан в 00_task_deck.md
        drawn_cards = []
        for card in range(x):
            drawn_cards.append(self.cards.pop(0))
        return drawn_cards

    def shuffle(self):
        # TODO-2: Принцип работы данного метода прописан в 00_task_deck.md
        #   Подсказка: https://www.w3schools.com/python/ref_random_shuffle.asp
        random.shuffle(self.cards)


# Создаем колоду
deck = Deck()
# Выводим колоду в формате указанном в основном задании
print(deck.show())
# Тусуем колоду
deck.shuffle()
print(deck.show())

# Возьмем 5 карт "в руку"
hand = deck.draw(5)
# Выводим колоду, чтобы убедиться что 5 верхних карт отсутствуют
print(deck.show())
# Выводим список карт "в руке"(список hand)
print('hand: ', ','.join([card.to_str() for card in hand]))
