# Сюда отправляем решение первой задачи с колодой
import random


class Card:
    HEARTS = "Hearts"
    DIAMONDS = "Diamonds"
    CLUBS = "Clubs"
    SPADES = "Spades"


    points_dict_one = {
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


    points_dict_two = {
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
     "A": 1
    }
    suit_worth_dict = {
    "Spades": 0,
    "Clubs": 0,
    "Diamonds": 0,
    "Hearts": 0
    }

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def equal_suit(self, other_card):
        return self.suit == other_card.suit

    def __repr__(self):
        icons = {
            "Hearts": '\u2665',
            "Diamonds": '\u2666',
            "Clubs": '\u2663',
            "Spades": '\u2660',
        }
        return f"{self.value}{icons[self.suit]}"

    def __lt__(self, other_card):  # <
        value_index_self = Deck.values.index(self.value)
        value_index_other = Deck.values.index(other_card.value)
        if value_index_self == value_index_other:
            suit_index_self = Deck.suits.index(self.suit)
            suit_index_other = Deck.suits.index(other_card.suit)
            return suit_index_self < suit_index_other
        return value_index_self < value_index_other

    def __gt__(self, other_card):  # >
        value_index_self = Deck.values.index(self.value)
        value_index_other = Deck.values.index(other_card.value)
        if value_index_self == value_index_other:
            suit_index_self = Deck.suits.index(self.suit)
            suit_index_other = Deck.suits.index(other_card.suit)
            return suit_index_self > suit_index_other
        return value_index_self > value_index_other


class Deck:
    values = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
    suits = ("Spades", "Clubs", "Diamonds", "Hearts")


    def __init__(self):
        self.index_last_card = -1
        self.cards = []
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        for suit in Deck.suits:
            for value in Deck.values:
                card = Card(value, suit)
                self.cards.append(card)

    # magic-methods
    def __repr__(self):
        deck_str = f"deck[{len(self.cards)}]"
        for card in self.cards:
            deck_str += str(card) + ","
        return deck_str

    def __getitem__(self, index):
        return self.cards[index]

    def draw(self, x):
        cards_draw = self.cards[0:x]
        self.cards = self.cards[x:]
        return cards_draw

    def shuffle(self):
        random.shuffle(self.cards)

    def __iter__(self):
        self.index_last_card = -1
        return self

    def __next__(self):
        self.index_last_card += 1
        if self.index_last_card >= len(self.cards):
            raise StopIteration
        return self.cards[self.index_last_card]



deck = Deck()
#########################################################
############### ! # THE GAME #### ! #####################
#########################################################


# Задачи - реализовать нативную работу с объектами:
# 1. Вывод колоды в терминал:

print(deck)  # вместо print(deck.show())
# print(deck.__str__())
#card1, card2 = deck.draw(2)


# # # 2. Вывод карты в терминал:
#  print(card1)  # вместо print(card1.__str__())
#  hand = deck.draw(5)
# print(hand)  # print(hand.__str__())
#  el.__repr__()

# # 3. Сравнение карт:
# card1 > card2
# card1.__gt__(card2)
# card1 < card2
# card1.__lt__(card2)
# card1 == card2
# card1.__eq__(card2)

# card1.__gt__(card2)
# if card1 > card2:
#     print(f"{card1} больше {card2}")
# else:
#     print(f"{card2} меньше или равна {card1}")

# 4. Итерация по колоде:
# Итератор(последовательность)
deck = Deck()
# print(deck)
# min_card = min(deck)
# print("min_card = ", min_card)
for card in deck:
    print(card)
# min_card = min(deck)
# print(min_card)

# sum(deck)

# # Просмотр карты в колоде по ее индексу:
print(deck[6])

