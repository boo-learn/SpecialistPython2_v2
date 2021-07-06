import random


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def to_str(self):
        icons = {
            'Hearts': '\u2665',
            'Diamonds': '\u2666',
            'Clubs': '\u2663',
            'Spades': '\u2660'
        }
        return f"{self.value}{icons.get(self.suit)}"

    def equal_suit(self, other_card):
        return self.suit == other_card.suit

    def more(self, other_card):
        value = {''
                 '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
                 'J': 11, 'Q': 12, 'K': 13, 'A': 14
                 }
        value1 = value.get(self.value)
        value2 = value.get(other_card.value)
        return value1 > value2

    def less(self, other_card):
        value = {''
                 '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
                 'J': 11, 'Q': 12, 'K': 13, 'A': 14
                 }
        value1 = value.get(self.value)
        value2 = value.get(other_card.value)
        return value1 < value2


class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'A', 'K', 'Q', 'J']
        suits = ['Hearts', 'Diamonds', 'Clubs', "Spades"]
        self.cards = []
        for suit in suits:
            for value in values:
                card = Card(value, suit)
                self.cards.append(card)

    def show(self):
        deck_str = f"deck[{len(self.cards)}]"
        for card in self.cards:
            deck_str += card.to_str() + ','
        return deck_str

    def draw(self, x):
        cards_draw = self.cards[:x]
        self.cards = self.cards[x:]
        return cards_draw

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
