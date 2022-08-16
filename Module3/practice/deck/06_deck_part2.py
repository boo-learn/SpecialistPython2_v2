import random

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
        # TODO-0: конструктор копируем из предыдущей задачи
        for suit in suits:
            for value in values:
                self.cards.append(Card(value, suit))

    def show(self):
        # TODO-0: копируем из предыдущей задачи
        cards_str = []
        for value in self.cards:
            cards_str.append(value.to_str())

        res = ','.join(cards_str)
        return f'cards[{str(len(cards_str))}]{res}'

    def draw(self, x):
        # TODO-1: Принцип работы данного метода прописан в 00_task_deck.md
        copy_cards = []
        copy_cards.extend(self.cards)
        cards = []
        for i in range(1,x+1):
            cards.append(copy_cards[i-1])
            del self.cards[0]

        return cards

    def shuffle(self):
        # TODO-2: Принцип работы данного метода прописан в 00_task_deck.md
        #   Подсказка: https://www.w3schools.com/python/ref_random_shuffle.asp
        random.shuffle(self.cards)

class Deck_New:
    def __init__(self, cards_in):

        self.cards = []

        for card in cards_in:
                self.cards.append(card)

    def show(self):
        # TODO-0: копируем из предыдущей задачи
        cards_str = []
        for value in self.cards:
            cards_str.append(value.to_str())

        res = ','.join(cards_str)
        return f'cards[{str(len(cards_str))}]{res}'

    def draw(self, x):
        # TODO-1: Принцип работы данного метода прописан в 00_task_deck.md
        copy_cards = []
        copy_cards.extend(self.cards)
        cards = []
        for i in range(1,x+1):
            cards.append(copy_cards[i-1])
            del self.cards[0]

        return cards

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

deck2 = Deck_New(hand)
# hand = deck.draw(1)
# Выводим колоду, чтобы убедиться что 5 верхних карт отсутствуют
print(deck.show())
# Выводим список карт "в руке"(список hand)
print(deck2.show())
