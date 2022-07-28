import random


class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты
        self.suit_icons = {'Spades': '\u2660', 'Clubs': '\u2663', 'Diamonds': '\u2666', 'Hearts': '\u2665'}
        self.card_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def to_str(self):
        return f'{self.value}{self.suit_icons[self.suit]}'

    def equal_suit(self, other_card):
        return self.suit == other_card.suit

    def more(self, other_card):
        if self.value == other_card.value:
            return list(self.suit_icons.keys()).index(self.suit) > list(other_card.suit_icons.keys()).index(
                other_card.suit)
        return self.card_values.index(self.value) > self.card_values.index(other_card.value)

    def less(self, other_card):
        if self.value == other_card.value:
            return list(self.suit_icons.keys()).index(self.suit) < list(other_card.suit_icons.keys()).index(
                other_card.suit)
        return self.card_values.index(self.value) < self.card_values.index(other_card.value)


class Deck:
    def __init__(self):
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.cards = [Card(value, suit) for suit in suits for value in values]

    def show(self):
        return f'cards[{len(self.cards)}]: {", ".join([card.to_str() for card in self.cards])}'

    def draw(self, x):
        first_cards = []
        for _ in range(x):
            first_cards.append(self.cards[0])
            self.cards.pop(0)
        return first_cards

    def shuffle(self):
        random.shuffle(self.cards)


# Создаем колоду
deck = Deck()
# Тусуем колоду
deck.shuffle()
print(deck.show())
# Берем две карты из колоды
card1, card2 = deck.draw(2)

# Тестируем методы .less() и .more()
if card1.more(card2):
    print(f"{card1.to_str()} больше {card2.to_str()}")
if card1.less(card2):
    print(f"{card1.to_str()} меньше {card2.to_str()}")
