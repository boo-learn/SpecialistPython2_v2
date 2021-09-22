class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        symbols = {
            'Hearts': '\u2665',
            'Diamonds': '\u2666',
            'Clubs': '\u2663',
            'Spades': '\u2660'
        }
        return f'{self.value}{symbols[self.suit]}'


    def equal_suit(self, other_card):
        return self.suit == other_card.suit




values = ["2", "3", "4", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

hearts_cards = []
for value in values:
    H_card = Card(value, "Hearts")
    hearts_cards.append(H_card)

diamonds_cards = []
for value in values:
    d_card = Card(value, "Diamonds")
    diamonds_cards.append(d_card)


for card in hearts_cards:
    print(card.to_str(), end=", ")
