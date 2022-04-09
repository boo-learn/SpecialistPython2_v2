import random


class Card:
    # TODO-0: сюда копируем реализацию класса карты из предыдущего задания
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        suits = {"Hearts": "♥", "Diamonds": "♦", "Clubs": "♧", "Spades": "♤"}
        return f'{self.value}{suits.get(self.suit)}'

    def equal_suit(self, other_card):
        return self.suit == other_card.suit

    # TODO-1: реализуем новые методы

    def more(self, other_card):
        suits = {"Hearts": 4, "Diamonds": 3, "Clubs": 2, "Spades": 1}
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        if values.index(self.value) == values.index(other_card.value):
            return suits.get(self.suit) > suits.get(other_card.suit)
        return values.index(self.value) > values.index(other_card.value)

    def less(self, other_card):
        suits = {"Hearts": 4, "Diamonds": 3, "Clubs": 2, "Spades": 1}
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        if values.index(self.value) == values.index(other_card.value):
            return suits.get(self.suit) < suits.get(other_card.suit)
        return values.index(self.value) < values.index(other_card.value)


class Deck:
    # TODO-0: сюда копируем реализацию класса колоды из предыдущего задания
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.cards = []
        # TODO-0: конструктор копируем из предыдущей задачи
        for suit in suits:
            for value in values:
                self.cards.append(Card(value, suit))

    def show(self):
        # TODO-2: Принцип работы данного метода прописан в 00_task_deck.md
        cards_str = [card.to_str() for card in self.cards]
        return f'cards[{len(self.cards)}]{", ".join(cards_str)}'

    def draw(self, x):
        # TODO-1: Принцип работы данного метода прописан в 00_task_deck.md
        draws = self.cards[:x]
        del self.cards[:x]
        return draws

    def shuffle(self):
        # TODO-2: Принцип работы данного метода прописан в 00_task_deck.md
        #   Подсказка: https://www.w3schools.com/python/ref_random_shuffle.asp
        random.shuffle(self.cards)

    def shift(self, num_card):
        # TODO-1: реализуем новый метод "сдвиг"
        #  Принцип работы: перемещает num_card с верха колоды под низ
        self.cards += self.cards[:num_card]
        del self.cards[:num_card]

# Создаем колоду
deck = Deck()
# Тусуем колоду
deck.shuffle()
print(deck.show())
# Сдвигаем 10 карт
deck.shift(10)
print(deck.show())
