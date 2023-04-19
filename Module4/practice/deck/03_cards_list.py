class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def to_str(self):
        suit_symbols = {"Hearts": "\u2665", "Diamonds": "\u2666", "Clubs": "\u2665", "Spades": "\u2665"}
        return self.value + suit_symbols[self.suit]

    def equal_suit(self, new_card) -> bool:
        return self.suit == new_card.suit


def print_cards(cards_list):
    temp_st = ""
    for card in cards_list:
        temp_st += f"{card.to_str()}, "
    print(temp_st[:-2])


values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
hearts_cards = []
for value in values:
    hearts_cards.append(Card(value, "Hearts"))

diamonds_cards = []
for value in reversed(values):
    diamonds_cards.append(Card(value, "Hearts"))

print_cards(hearts_cards)
print_cards(diamonds_cards)
