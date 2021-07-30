import random


class Card:
    HEARTS = "Hearts"
    DIAMONDS = "Diamonds"
    CLUBS = "Clubs"
    SPADES = "Spades"

    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты
        self.weight = 0
        if 8 < Deck.values.index(self.value) < 12:
            self.weight = 10
        elif Deck.values.index(self.value) == 12:
            self.weight = 11
        else:
            self.weight += Deck.values.index(self.value) + 2

    def __str__(self):
        icons = {'Hearts': '\u2665',
                 'Diamonds': '\u2666',
                 'Clubs': '\u2663',
                 'Spades': '\u2660'}
        return f'{self.value}{icons[self.suit]}'

    def equal_suit(self, other_card):
        return other_card.suit == self.suit

    def __gt__(self, other_card):
        index_value_card1 = Deck.values.index(self.value)
        index_value_card2 = Deck.values.index(other_card.value)
        index_suit_card1 = Deck.suits.index(self.suit)
        index_suit_card2 = Deck.suits.index(other_card.suit)

        if index_value_card1 == index_value_card2:
            return index_suit_card1 > index_suit_card2

        return index_value_card1 > index_value_card2

    def __lt__(self, other_card):
        if self == other_card:
            return False
        return not self > other_card

    def __eq__(self, other_card):
        return self.value == other_card.value and self.suit == other_card.suit


class Deck:
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        self.cards = []
        self.last_index_card = None
        for suit in Deck.suits:
            for value in Deck.values:
                self.cards.append(Card(value, suit))

    def __str__(self):
        # Принцип работы данного метода прописан в 00_task_deck.md
        cards_str = f"deck[{len(self.cards)}]{str(self.cards[0])}"
        for card in self.cards[1:]:
            cards_str += "," + str(card)
        return cards_str

    def draw(self, x):
        # Принцип работы данного метода прописан в 00_task_deck.md
        taken_card = []
        for _ in range(x):
            card = self.cards.pop(0)
            taken_card.append(card)
        return taken_card

    def shuffle(self):
        # Обратите внимание на: https://www.w3schools.com/python/ref_random_shuffle.asp
        random.shuffle(self.cards)

    def __iter__(self):
        return self

    def __next__(self):
        if self.last_index_card is None:
            self.last_index_card = 0
        else:
            self.last_index_card += 1
        if self.last_index_card >= len(self.cards):
            raise StopIteration
        return self.cards[self.last_index_card]

    def __getitem__(self, index):
        return self.cards[index]

# deck = Deck()
# print(deck.cards[12].weight)
