class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        icons = {"Hearts": '\u2665',
                 "Diamonds": '\u2666',
                 "Clubs": '\u2667',
                 "Spades": '\u2664'
                 }
        return f"{self.value}{icons.get(self.suit)}"

    def equal_suit(self, other_card):
        return self.suit == other_card.suit


values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
# добавьте в список hearts_cards все червовые карты(от 2-ки до туза)
hearts_cards = [Card(val, "Hearts") for val in values]

# добавьте в список diamonds_cards все бубновые карты(от туза до 2-ки)
diamonds_cards = [Card(val, "Diamonds") for val in reversed(values)]

# выведите все карты из списка hearts_cards в терминал через запятую в одну строку:
print(', '.join([card.to_str() for card in hearts_cards]))
