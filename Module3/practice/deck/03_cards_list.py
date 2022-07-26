class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        to_unic_char = {
            "Hearts": "\u2665",
            "Diamonds": "\u2666",
            "Spades": "\u2660",
            "Clubs": "\u2663"
        }

        return f"{self.value}{to_unic_char[self.suit]}"

    def equal_suit(self, other_card):
        return self.suit == other_card.suit


values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
hearts_cards = [Card(value=val, suit="Hearts") for val in values]
diamonds_cards = [Card(value=val, suit="Diamonds") for val in values]

# Пример вывода: 2♥, 3♥, 4♥ ... A♥

print(", ".join([card.to_str() for card in hearts_cards]))
