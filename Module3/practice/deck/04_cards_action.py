class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        suit_to_pic = {"Hearts": '\u2665', "Diamonds": '\u2666', "Spades": '\u2664', "Clubs": '\u2667'}
        return f"{self.value}{suit_to_pic[self.suit]}"

    def equal_suit(self, other_card):
        return self.suit == other_card.suit


cards = []
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
for suit in suits:
    for value in values:
        cards.append(Card(value, suit))

print("cards[", len(cards), "]", ', '.join([card.to_str() for card in cards]), sep="")

