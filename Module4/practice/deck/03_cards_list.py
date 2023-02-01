class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        icon = None
        if self.suit == "Hearts":
            icon = '\u2665'
        elif self.suit == "Diamonds" :
            icon = '\u2666'
        elif self.suit == "Spades":
            icon = '\u2660'
        else:
            icon = '\u2663'
        return f'{self.value}{icon}'

    def equal_suit(self, other_card):
        
        if self.suit == other_card.suit:
            return True
        return False

values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
hearts_cards = []

for value in values:
    hearts_cards.append(Card(value, "Hearts"))

diamonds_cards = []
values.reverse()
for value in values:
    diamonds_cards.append(Card(value, "Diamond"))


for heart_card in hearts_cards:
    print(heart_card.to_str())
# cards = [
#     Card("2", "Hearts"),
#     Card("3", "Hearts"),
#     Card("4", "Hearts"),
#     ...]
