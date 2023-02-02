import random


class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        suit_icons = {
            "Hearts": "\u2665",
            "Diamonds": "\u2666",
            "Clubs": "\u2663",
            "Spades": "\u2660"
        }
        return f"{self.value}{suit_icons[self.suit]}"

    def equal_suit(self, other_card):

        if self.suit == other_card.suit:
            return True
        return False

    def more(self, other_card):
        suit_weight = {
            "Hearts": 4,
            "Diamonds": 3,
            "Clubs": 2,
            "Spades": 1
        }
        value_weight = {
            "A": 14,
            "K": 13,
            "Q": 12,
            "J": 11,
            "10": 10,
            "9": 9,
            "8": 8,
            "7": 7,
            "6": 6,
            "5": 5,
            "4": 4,
            "3": 3,
            "2": 2,
        }

        if value_weight[self.value] == value_weight[other_card.value]:
            return suit_weight[self.suit] > suit_weight[other_card.suit]
        else:
            return value_weight[self.value] > value_weight[other_card.value]

    def less(self, other_card):
        suit_weight = {
            "Hearts": 4,
            "Diamonds": 3,
            "Clubs": 2,
            "Spades": 1
        }
        value_weight = {
            "A": 14,
            "K": 13,
            "Q": 12,
            "J": 11,
            "10": 10,
            "9": 9,
            "8": 8,
            "7": 7,
            "6": 6,
            "5": 5,
            "4": 4,
            "3": 3,
            "2": 2,
        }
        if value_weight[self.value] == value_weight[other_card.value]:
            return suit_weight[self.suit] < suit_weight[other_card.suit]
        else:
            return value_weight[self.value] < value_weight[other_card.value]


class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        values = ['2', '3', '4', '5', '6', '7',
                  '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.cards = []
        for value in values:
            for suit in suits:
                self.cards.append(Card(value, suit))

    def show(self):
        final_str = f'deck[{len(self.cards)}]'
        str_cards = []
        for card in self.cards:
            str_cards.append(card.to_str())
        return final_str + ", ".join(str_cards)

    def draw(self, x):

        hand, self.cards = self.cards[:x], self.cards[x:]
        return hand

    def shuffle(self):
        random.shuffle(self.cards)

    def shift(self, num_card):

        self.cards = self.cards[num_card:] + self.cards[:num_card]


# Создаем колоду
deck = Deck()
# Тусуем колоду
deck.shuffle()
print(deck.show())
print('─' * 10)
# Сдвигаем 10 карт
deck.shift(10)
print(deck.show())
