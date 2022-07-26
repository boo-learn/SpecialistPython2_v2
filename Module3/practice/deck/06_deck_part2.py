import random

class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        # TODO-0: скопируйте реализацию метода из предыдущей задачи
        suits = {'Hearts':'\u2665','Diamonds':'\u2666','Clubs':'\u2663','Spades':'\u2660'}
        return f'{self.value}{suits[self.suit]}'

    def equal_suit(self, other_card):
        # TODO-1: метод возвращает True - если масти карт равны или False - если нет
        return self.suit == other_card.suit


class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        # TODO-0: конструктор копируем из предыдущей задачи
        self.cards = [Card(value, suit) for suit in suits for value in values]

    def show(self):
        # TODO-0: копируем из предыдущей задачи
        return f"deck[{len(self.cards)}]{', '.join([card.to_str() for card in self.cards])}"

    def draw(self, x):
        # TODO-1: Принцип работы данного метода прописан в 00_task_deck.md
        return [self.cards.pop() for _ in range(x)]

    def shuffle(self):
        # TODO-2: Принцип работы данного метода прописан в 00_task_deck.md
        #   Подсказка: https://www.w3schools.com/python/ref_random_shuffle.asp
        return random.shuffle(self.cards)


# Создаем колоду
deck = Deck()
print('Выводим колоду в формате указанном в основном задании')
print(deck.show())
print('Тусуем колоду')
deck.shuffle()
print(deck.show())

# Возьмем 5 карт "в руку"
hand = deck.draw(5)
print('Выводим колоду, чтобы убедиться что 5 верхних карт отсутствуют')
print(deck.show())

print('Выводим список карт "в руке"(список hand)')
print(', '.join([card.to_str() for card in hand]))
