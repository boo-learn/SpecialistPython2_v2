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

    def get_suit(self, suit):
        if suit not in self._symbols:
            raise KeyError("Такой масти нет")
        return self._symbols[suit]

    def equal_suit(self, other_card):
        return self.suit == other_card.suit


cards = []
# TODO-1: в список cards добавьте ВСЕ карты всех мастей

# TODO-2: Выведите карты в формате: cards[кол-во]2♥, 3♥, 4♥ ... A♥, 2♦, 3♦ ... A♦, ....

# старшие карты
grown_up_cards = ["J", "Q", "K", "A"]
suits = [ "\u2660","\u2666","\u2665","\u2663" ]
# общая колода
common_deck = []
for i in range(2, 11, 1):
    common_deck.append(i)
common_deck = common_deck + grown_up_cards

for card in common_deck:
    for suit in suits:
        cards.append(f"{card}{suit}")

print(', '.join(cards))
