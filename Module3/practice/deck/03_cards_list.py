class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        self.suit_to_pic = {"Hearts": '\u2665', "Diamonds": '\u2666', "Spades": '\u2664', "Clubs": '\u2667'}
        return f"{self.value}{self.suit_to_pic[self.suit]}"

    def equal_suit(self, other_card):
        return self.suit == other_card.suit


values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
hearts_cards = [Card(value, "Hearts") for value in values]

diamonds_cards = [Card(value, "Diamonds") for value in reversed(values)]

print(', '.join([card.to_str() for card in hearts_cards]))
print(', '.join([card.to_str() for card in diamonds_cards]))



cards = [
    Card("2", "Hearts"),
    Card("3", "Hearts"),
    Card("4", "Hearts"),
    ...]
