import random

class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты
        self.values_more = {'2':1, '3':2, '4':3, '5':4, '6':5, '7':6, '8':7, '9':8, '10':9, 'J':10, 'Q':11, 'K':12, 'A':13}
        self.suits_more = {"Hearts":1, "Diamonds":2, "Clubs":3, "Spades":4}

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

    # TODO-1: реализуем новые методы
    def more(self, other_card):

        res = self.values_more[self.value] == self.values_more[other_card.value]
        if res:
            res = self.suits_more[self.suit] > self.suits_more[other_card.suit]
        else:
            res = self.values_more[self.value] > self.values_more[other_card.value]

        return res

    def less(self, other_card):

        res = self.values_more[self.value] == self.values_more[other_card.value]
        if res:
            res = self.suits_more[self.suit] < self.suits_more[other_card.suit]
        else:
            res = self.values_more[self.value] < self.values_more[other_card.value]

        return res


class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.values_more = {'2':1, '3':2, '4':3, '5':4, '6':5, '7':6, '8':7, '9':8, '10':9, 'J':10, 'Q':11, 'K':12, 'A':13}
        self.suits_more = {"Hearts":1, "Diamonds":2, "Clubs":3, "Spades":4}
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
        # copy_cards = []
        # copy_cards.extend(self.cards)
        # cards = []
        # for i in range(1,x+1):
        #     cards.append(copy_cards[i-1])
        #     del self.cards[0]
        cards = self.cards[:x]
        self.cards = self.cards[x:]

        return cards

    def shuffle(self):
        # TODO-2: Принцип работы данного метода прописан в 00_task_deck.md
        #   Подсказка: https://www.w3schools.com/python/ref_random_shuffle.asp
        random.shuffle(self.cards)

    def shift(self, num_card):
        # TODO-1: реализуем новый метод "сдвиг"
        #  Принцип работы: перемещает num_card с верха колоды под низ
        cards = self.cards[:num_card]
        self.cards = self.cards[num_card:]
        self.cards.extend(cards)


# Создаем колоду
deck = Deck()
# Тусуем колоду
deck.shuffle()
print(deck.show())
# Сдвигаем 10 карт
deck.shift(10)
print(deck.show())
