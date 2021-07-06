import random
from enum import Enum

class SuitType(Enum):
    Spades = 0
    Hearts = 1
    Diamonds = 2
    Clubs = 3


cardtype_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
cardtype_weight = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
    "A": 11
}

# Начнем с создания карты
class Card:
    suit_icon = {
        SuitType.Spades: "\u2660",
        SuitType.Hearts: "\u2665",
        SuitType.Diamonds: "\u2666",
        SuitType.Clubs: "\u2663",
    }

    def __init__(self, card_type, suit_type):
        self.card_type = card_type
        self.suit_type = suit_type

    def to_str(self):
        return f"{self.card_type}{Card.suit_icon[self.suit_type]}"

    def same_suit(self, card):
        return self.suit_type == card.suit_type

    def more(self, other_card):
        if self.card_type != other_card.card_type:
            return cardtype_weight[self.card_type] > cardtype_weight[other_card.card_type]
        else:
            return self.suit_type > other_card.suit_type

    def less(self, other_card):
        if self.card_type != other_card.card_type:
            return cardtype_weight[self.card_type] < cardtype_weight[other_card.card_type]
        else:
            return self.suit_type < other_card.suit_type

# Задание: Теперь создадим колоду из 52-ух карт и реализуем все методы
class Deck:
    def __init__(self):
        self.cards = []
        for card_type in cardtype_list:
            for suit_type in SuitType:
                self.cards.append(Card(str(card_type), suit_type))

    def show(self):
        s = ""
        for i, card in enumerate(self.cards):
            if i < len(self.cards):
                s += card.to_str() + ","
            else:
                s += card.to_str()
        return f"Количество карт: {len(self.cards)}, карты: {s}"

    def draw(self, x):
        card_list = self.cards[0:x]
        self.cards = self.cards[x:]
        return card_list
        """
        order = [i for i in range(len(self.cards))]
        count = len(order)
        card_list = []
        for i in range(x):
            j = random.randint(0, count - i - 1)
            card_list.append(self.cards[j])
            self.cards.pop(j)
            order[j] = order[count - i - 1]
        return card_list
        """

    def shuffle(self):
        random.shuffle(self.cards)
        """
        order = [i for i in range(len(self.cards))]
        count = len(order)
        for i in range(len(order)):
            j = random.randint(0, count - i - 1)
            card = self.cards[i]
            self.cards[i] = self.cards[j]
            self.cards[j] = card
            order[j] = order[count - i - 1]
        return True
        """

deck = Deck()
deck.shuffle()

# print(list(map(lambda card: card.to_str(), deck.draw(25))), " ")
card1, card2 = deck.draw(2)

if card1.more(card2):
    print(f"{card1.to_str()} больше {card2.to_str()}")
if card1.less(card2):
    print(f"{card1.to_str()} меньше {card2.to_str()}")

print(deck.show())
