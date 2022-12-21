import itertools


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


values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ["Hearts", "Diamonds", "Spades", "Clubs"]

# в список cards добавьте ВСЕ карты всех мастей
cards = [Card(value, suite) for suite, value in itertools.product(suits, values)]

# Выведите карты в формате: cards[кол-во]2♥, 3♥, 4♥ ... A♥, 2♦, 3♦ ... A♦, ...
print(f'cards[{len(cards)}]:', ', '.join([card.to_str() for card in cards]))
