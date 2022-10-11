import random


class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def __repr__(self):
        suit_icon = {
            'Diamonds': '\u2666',
            'Hearts': '\u2665',
            'Spades': '\u2664',
            'Clubs': '\u2667'
        }
        return f'{self.value}{suit_icon[self.suit]}'

    def __gt__(self, other_card):
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["Spades", "Clubs", "Diamonds", "Hearts"]
        if values.index(self.value) == values.index(other_card.value):
            return suits.index(self.suit) > suits.index(other_card.suit)
        else:
            return values.index(self.value) > values.index(other_card.value)

    def __eq__(self, other_card):
        return self.value == other_card.value and self.suit == other_card.suit

    def __lt__(self, other_card):
        return not self > other_card and not self == other_card

    def equal_suit(self, other_card):
        return self.suit == other_card.suit


class Deck:
    def __init__(self, first_value=0):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.cards = []
        for suit in suits:
            for value in values[first_value:]:
                self.cards.append(Card(value, suit))

    def __str__(self):
        cards_str = []
        for card in self.cards:
            cards_str.append(str(card))
        return f'cards[{len(self.cards)}]' + ', '.join(cards_str)

    def __getitem__(self, index):
        return self.cards[index]

    def draw(self, x):
        hand = self.cards[:x]
        self.cards = self.cards[x:]
        return hand

    def shuffle(self):
        random.shuffle(self.cards)

    def shift(self, num_card):
        shift_cards = self.cards[:num_card]
        self.cards = self.cards[num_card:]
        for card in shift_cards:
            self.cards.append(card)


# В этом файле дорабатываем классы, если это требуется для решения задачи
# Важно! При доработке классов для решение очередной задачи, необходимо не сломать решение предыдущей

if __name__ == "__main__":
    # Тут можно разместить тесты классов
    ...
