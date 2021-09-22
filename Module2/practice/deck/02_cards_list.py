class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        symbols = {
            "Spades": "\u2660",
            "Hearts": "\u2665",
            "Diamonds": "\u2666",
            "Clubs": "\u2663"
        }
        return f"{self.value}{symbols[self.suit]}"

    def equal_suit(self, other_card):
        return self.suit == other_card.suit


values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']     # Список значений карт


spades_cards = []
for value in values:
    spades_cards.append(Card(value, 'Spades'))
    for card in spades_cards:
        print(card.to_str(), end=", ")


hearts_cards = []
for value in values:
    hearts_cards.append(Card(value, 'Hearts'))
    for card in hearts_cards:
        print(card.to_str(), end=", ")


diamonds_cards = []
for value in values:
    diamonds_cards.append(Card(value, 'Diamonds'))
    for card in diamonds_cards:
        print(card.to_str(), end=", ")

clubs_cards = []
for value in values:
    clubs_cards.append(Card(value, 'Clubs'))
    for card in clubs_cards:
        print(card.to_str(), end=", ")
