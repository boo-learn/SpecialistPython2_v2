import random
from enum import Enum

class SuitType(Enum):
    Spades = 0
    Hearts = 1
    Diamonds = 2
    Clubs = 3

cardtype_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]

# Начнем с создания карты
class Card:
    suit_icon = {
        SuitType.Spades: '\2660',
        SuitType.Hearts: '\2665',
        SuitType.Diamonds: '\2666',
        SuitType.Clubs: '\2663',
    }

    def __init__(self, card_type, suit_type):
        self.card_type = card_type
        self.suit_type = suit_type

    def to_str(self):
        return f"{self.card_type}{Card.suit_icon[self.suit_type]}"

    def same_suit(self, card):
        return self.suit_type == card.suit_type

# Задание: Теперь создадим колоду из 52-ух карт и реализуем все методы
class Deck:
    def __init__(self):
        self.cards = []
        for card_type in cardtype_list:
            for suit_type in SuitType:
                self.cards.append(Card(card_type, suit_type))

    def show(self):
        s = ""
        for i, card in enumerate(self.cards):
            if i < len(self.cards):
                s += card.to_str() + ","
            else:
                s += card.to_str()
        return f"Количество карт: {len(self.cards)}, карты: {s}"

    def draw(self, x):
        pass

    def shuffle(self):
        order = [i for i in range(len(self.cards))]
        count = len(order)
        for i in range(len(order)):
            j = random.randint(0, count - i + 1)
            card = self.cards[i]
            self.cards[i] = self.cards[j]
            self.cards[j] = card
            order[j] = order[count - i - 1]

deck = Deck()
deck.shuffle()
print(deck.show())
