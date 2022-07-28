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

    def more(self, other_card):
        suit_order = {'Hearts': 4, 'Diamonds': 3, 'Clubs': 2, 'Spades': 1}
        value_order = {'2': 2, '3': 3, '4': 3, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12,
                       'K': 13, 'A': 14}
        if value_order[self.value] > value_order[other_card.value]:
            return True
        elif value_order[self.value] == value_order[other_card.value] and suit_order[self.suit] > suit_order[
            other_card.suit]:
            return True
        else:
            return False

    def less(self, other_card):
        suit_order = {'Hearts': 4, 'Diamonds': 3, 'Clubs': 2, 'Spades': 1}
        value_order = {'2': 2, '3': 3, '4': 3, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12,
                       'K': 13, 'A': 14}
        if value_order[self.value] < value_order[other_card.value]:
            return True
        elif value_order[self.value] == value_order[other_card.value] and suit_order[self.suit] < suit_order[
            other_card.suit]:
            return True
        else:
            return False


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
        return cards_in_hand

    def shuffle(self):
        return random.shuffle(self.cards)

    def shift(self, num_card):
        for _ in range(num_card):
            self.cards.append(self.cards.pop(0))


# Создаем колоду
deck = Deck()
# Тусуем колоду
deck.shuffle()
print(deck.show())
# Сдвигаем 10 карт
deck.shift(10)
print(deck.show())
