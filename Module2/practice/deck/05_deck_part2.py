import random


class Card:
    pass

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


    def more(self, other_card):
        icons_values = {'Hearts': 4,
                        'Diamonds': 3,
                        'Clubs': 2,
                        'Spades': 1}
        if self.value != other_card.value:
            return self.value > other_card.value
        else:
            return icons_values[self.suit] > icons_values[other_card.suit]

    def less(self, other_card):
        icons_values = {'Hearts': 4,
                        'Diamonds': 3,
                        'Clubs': 2,
                        'Spades': 1}
        if self.value != other_card.value:
            return self.value < other_card.value
        else:
            return icons_values[self.suit] < icons_values[other_card.suit]


class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        self.cards = []
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        for suit in suits:
            for value in values:
                self.cards.append(Card(value, suit))

    def show(self):
        # Принцип работы данного метода прописан в 00_task_deck.md
        cards_str = f"deck[{len(self.cards)}]{self.cards[0].to_str()}"
        for card in self.cards[1:]:
            cards_str += "," + card.to_str()
        return cards_str

    def draw(self, x):
        # Принцип работы данного метода прописан в 00_task_deck.md
        taken_card = []
        for _ in range(x):
            card = self.cards.pop(0)
            taken_card.append(card)
        return taken_card

    def shuffle(self):
        random.shuffle(self.cards)


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
