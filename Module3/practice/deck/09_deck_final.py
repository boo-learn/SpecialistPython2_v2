import random


class Card:
    # TODO-0: сюда копируем реализацию класса карты из предыдущего задания
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def __str__(self):
        suits = {"Hearts": "♥", "Diamonds": "♦", "Clubs": "♧", "Spades": "♤"}
        return f'{self.value}{suits.get(self.suit)}'

    def equal_suit(self, other_card):
        return self.suit == other_card.suit

    def __gt__(self, other_card):
        suits = {"Hearts": 4, "Diamonds": 3, "Clubs": 2, "Spades": 1}
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        if values.index(self.value) == values.index(other_card.value):
            return suits.get(self.suit) > suits.get(other_card.suit)
        return values.index(self.value) > values.index(other_card.value)

    def __lt__(self, other_card):
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

    def __str__(self):
        # TODO-2: Принцип работы данного метода прописан в 00_task_deck.md
        cards_str = [card.__str__() for card in self.cards]
        return f'cards[{len(self.cards)}]{", ".join(cards_str)}'

    def __getitem__(self, item):
        return self.cards[item]

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


deck = Deck()
# TODO-final: реализовать нативную работу с объектами:
# 1. Вывод колоды в терминал:
print(deck)
# вместо print(deck.show())

card1, card2 = deck.draw(2)
# 2. Вывод карты в терминал:
print(card1)  # вместо print(card1.to_str())

# 3. Сравнение карт:
if card1 > card2:
    print(f"{card1} больше {card2}")

# 4. Итерация по колоде:
for card in deck:
    print(card)

# 5. Просмотр карты в колоде по ее индексу:
print(deck[6])


# Список ВСЕХ magic-методов см. тут: http://pythonworld.ru/osnovy/peregruzka-operatorov.html
