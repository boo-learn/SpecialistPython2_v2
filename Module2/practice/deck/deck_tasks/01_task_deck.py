import random
# Начнем с создания карты
class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты
        self.weight = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12,
                       'K': 13, 'A': 14}    # Вес карты

    def __str__(self):
        icons = {'Hearts': '\u2665', 'Diamonds': '\u2666', 'Clubs': '\u2663', 'Spades': '\u2660'}
        return f'{self.value}{icons[self.suit]}'

    def equal_suit(self, other_card):
        return self.suit == other_card.suit

    def __lt__(self, other):
        return self.weight[str(self.value)] < self.weight[str(other.value)]

    def __gt__(self, other):
        return self.weight[str(self.value)] > self.weight[str(other.value)]


class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        values = [char for char in range(2, 11)] + ['J', 'Q', 'K', 'A']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.last_index_card = None
        self.cards = []
        for suit in suits:
            for value in values:
                card = Card(value, suit)
                self.cards.append(card)

    def __str__(self):
        cards_str = f'deck[{len(self.cards)}]: {str(self.cards[0])}'
        for card in self.cards[1:]:
            cards_str += ', ' + str(card)
        return cards_str

    def draw(self, x):
        taken_card = []
        for _ in range(x):
            card = self.cards.pop(0)
            taken_card.append(card)
        return taken_card

    def shuffle(self):
        return random.shuffle(self.cards)

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

    def __getitem__(self, item):
        return self.cards[item]


deck = Deck()
deck.shuffle()
card1, card2 = deck.draw(2)
if card1 > card2:
    print(f"{card1} больше {card2}")
else:
    print(f"{card2} больше {card1}")
