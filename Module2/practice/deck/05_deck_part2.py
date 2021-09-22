import random

class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        icons = {'Hearts': '\u2665',
                 'Diamonds': '\u2666',
                 'Clubs': '\u2663',
                 'Spades': '\u2660'}
        return f'{self.value}{icons[self.suit]}'

    def equal_suit(self, other_card):
        return other_card.suit == self.suit

    def __str__(self):
        icons = {'Hearts': '\u2665',
                 'Diamonds': '\u2666',
                 'Clubs': '\u2663',
                 'Spades': '\u2660'}
        return f'{self.value}{icons[self.suit]}'

    def more(self, other_card):
        icons_order = {'Hearts': 1, 'Diamonds': 2, 'Clubs': 3, 'Spades': 4}
        if self.value == other_card.value:
            return icons_order[self.suit] > icons_order[other_card.suit]
        else:
            return self.value > other_card.value

    def less(self, other_card):
        icons_order = {'Hearts': 1, 'Diamonds': 2, 'Clubs': 3, 'Spades': 4}
        if self.value == other_card.value:
            return icons_order[self.suit] < icons_order[other_card.suit]
        else:
            return self.value < other_card.value


class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        self.cards = []
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.last_index_card = None
        for suit in suits:
            for value in values:
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

    def show(self):
        # Принцип работы данного метода прописан в 00_task_deck.md
        cards_str = f"deck[{len(self.cards)}]{self.cards[0].to_str()}"
        for card in self.cards[1:]:
            cards_str += "," + card.to_str()
        return cards_str


deck = Deck()
deck.shuffle()
print(deck.show())
# Берем две карты из колоды
card1, card2 = deck.draw(2)

# Тестируем методы .less() и .more()
if card1.more(card2):
    print(f"{card1.to_str()} больше {card2.to_str()}")
if card1.less(card2):
    print(f"{card1.to_str()} меньше {card2.to_str()}")
