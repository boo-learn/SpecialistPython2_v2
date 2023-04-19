class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def to_str(self):
        suit_symbols = {"Hearts": "\u2665", "Diamonds": "\u2666", "Clubs": "\u2663", "Spades": "\u2660"}
        return self.value + suit_symbols[self.suit]

    def equal_suit(self, new_card) -> bool:
        return self.suit == new_card.suit


def print_cards(cards_list):
    temp_st = ""
    for card in cards_list:
        temp_st += f"{card.to_str()}, "
    print(temp_st[:-2])


cards = []
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ["Hearts", "Diamonds", "Spades", "Clubs"]

# Вариант №1
# TODO-1: в список cards добавьте ВСЕ карты всех мастей
for suit in suits:
    for value in values:
        cards.append(Card(value, suit))
print_cards(cards)
print()

# Вариант № 2
# TODO-2: Выведите карты в формате: cards[кол-во]2♥, 3♥, 4♥ ... A♥, 2♦, 3♦ ... A♦, ...
#  кол-во берем от размера списка cards
i = 0
temp_string = ""
while i < len(cards):
    temp_string += f"{cards[i].to_str()}, "
    i += 1
print(temp_string[:-2])
