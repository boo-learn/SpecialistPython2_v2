import random


class Card:
    HEARTS = "Hearts"
    DIAMONDS = "Diamonds"
    CLUBS = "Clubs"
    SPADES = "Spades"

    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def __str__(self):
        suits = {"Hearts": "♥", "Diamonds": "♦", "Clubs": "♧", "Spades": "♤"}
        return f'{self.value}{suits.get(self.suit)}'

    def equal_suit(self, other_card):
        return self.suit == other_card.suit

    def __gt__(self, other_card):

        if Deck.values.index(self.value) == Deck.values.index(other_card.value):
            return list(reversed(Deck.suits)).index(self.suit) > list(reversed(Deck.suits)).index(other_card.suit)
        return Deck.values.index(self.value) > Deck.values.index(other_card.value)

    def __lt__(self, other_card):

        if Deck.values.index(self.value) == Deck.values.index(other_card.value):
            return list(reversed(Deck.suits)).index(self.suit) < list(reversed(Deck.suits)).index(other_card.suit)
        return Deck.values.index(self.value) < Deck.values.index(other_card.value)

    def __eq__(self, other_card):
        if Deck.values.index(self.value) == Deck.values.index(other_card.value):
            return list(reversed(Deck.suits)).index(self.suit) < list(reversed(Deck.suits)).index(other_card.suit)
        return Deck.values.index(self.value) == Deck.values.index(other_card.value) and Deck.suits.index(
            self.suit) == Deck.suits.index(other_card.suit)


class Deck:
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        self.cards = []
        # TODO-0: конструктор копируем из предыдущей задачи
        for suit in Deck.suits:
            for value in Deck.values:
                self.cards.append(Card(value, suit))

    def __str__(self):
        # TODO-2: Принцип работы данного метода прописан в 00_task_deck.md
        cards_str = [card.__str__() for card in self.cards]
        return f'cards[{len(self.cards)}]{", ".join(cards_str)}'

    def __iter__(self):
        self.index_next_card = 0
        return self

    def __next__(self):
        try:
            card = self.cards[self.index_next_card]
        except IndexError:
            raise StopIteration
        self.index_next_card += 1
        return card

    def __getitem__(self, item):
        return self.cards[item]

    def draw(self, x):
        # TODO-1: Принцип работы данного метода прописан в 00_task_deck.md
        draws = self.cards[:x]
        self.cards = self.cards[x:]
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

    def __add__(self, other):
        self.cards += other.cards
        return self


# В этом файле дорабатываем классы, если это требуется для решения задачи
# Важно! При доработке классов для решение очередной задачи, необходимо не сломать решение предыдущей

if __name__ == "__main__":
    # Тут можно разместить тесты классов
    ...
