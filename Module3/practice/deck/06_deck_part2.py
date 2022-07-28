import random


class Card:

    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты
        self.suit_icons = {'Hearts': '\u2665', 'Diamonds': '\u2666', 'Clubs': '\u2663', 'Spades': '\u2660'}

    def to_str(self):
        return f'{self.value}{self.suit_icons[self.suit]}'

    def equal_suit(self, other_card):
        return self.suit == other_card.suit


class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.cards = []
        for suit in suits:
            for value in values:
                self.cards.append(Card(value, suit))

    def show(self):
        return f"cards[{len(self.cards)}]{', '.join([card.to_str() for card in self.cards])}"

    def draw(self, x):
        cards_in_hand = []
        for _ in range(x):
            cards_in_hand.append(self.cards.pop(0))
        return [card.to_str() for card in cards_in_hand]

    def shuffle(self):
        return random.shuffle(self.cards)


# Создаем колоду
deck = Deck()
# Выводим колоду в формате указанном в основном задании
print(deck.show())
# Тусуем колоду
deck.shuffle()
print(deck.show())

# Возьмем 5 карт "в руку"
hand = deck.draw(5)
# Выводим колоду, чтобы убедиться что 5 верхних карт отсутствуют
print(deck.show())
# Выводим список карт "в руке"(список hand)
print(hand)
