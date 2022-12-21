import itertools
import random


class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        icons = {"Hearts": '\u2665',
                 "Diamonds": '\u2666',
                 "Clubs": '\u2667',
                 "Spades": '\u2664'
                 }
        return f"{self.value}{icons.get(self.suit)}"

    def equal_suit(self, other_card):
        return self.suit == other_card.suit

    def more(self, other_card):
        if self.equal_suit(other_card):
            return self.value > other_card.value

    def less(self, other_card):
        if self.equal_suit(other_card):
            return self.value < other_card.value


class Deck:
    def __init__(self):
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.cards = [Card(value, suite) for suite, value in itertools.product(suits, values)]

    def show(self):
        return f'deck[{len(self.cards)}]: {", ".join([card.to_str() for card in self.cards])}'

    def draw(self, x):
        cards = self.cards[0:x]
        del(self.cards[0:x])
        return cards

    def shuffle(self):
        random.shuffle(self.cards)


# Создаем колоду
deck = Deck()
# Тусуем колоду
deck.shuffle()
print(deck.show())
# Берем две карты из колоды
card1, card2 = deck.draw(2)
print(card1.to_str(), card2.to_str())

# Тестируем методы .less() и .more()
if card1.more(card2):
    print(f"{card1.to_str()} больше {card2.to_str()}")
if card1.less(card2):
    print(f"{card1.to_str()} меньше {card2.to_str()}")
