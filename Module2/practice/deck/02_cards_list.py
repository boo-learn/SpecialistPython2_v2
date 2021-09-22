class Card:
    _symbols = {
        "Spades": "\u2660",
        "Diamonds": "\u2666",
        "Hearts": "\u2665",
        "Clubs": "\u2663"
    }

    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def __repr__(self):
        return f"{self.value}{self._symbols[self.suit]}"

    def to_str(self):
        return f"{self.value}{self._symbols[self.suit]}"

    # def get_suit(self, suit):
    #     if suit not in self._symbols:
    #         raise KeyError("Такой масти нет")
    #     return self._symbols[suit]

    def equal_suit(self, other_card):
        return self.suit == other_card.suit


# карта для возможности иметь обьект класс
card_com = Card("J", "Clubs")

# старшие карты
grown_up_cards = ["J", "Q", "K", "A"]
# общая колода
common_deck = []
for i in range(2, 11, 1):
    common_deck.append(i)
common_deck = common_deck + grown_up_cards
# 1
hearts_cards = []
# symbol = Card.get_suit(card_com, "Hearts")
suit = "Hearts"

for card in common_deck:
    hearts_cards.append(Card(card,suit))

# 2
diamonds_cards = []
#symbol1 = Card.get_suit(card_com, "Diamonds")
suit = "Diamonds"
common_deck_rev = list(reversed(common_deck))

for card in common_deck_rev:
    diamonds_cards.append(Card(card,suit))

# 3
print(hearts_cards)
