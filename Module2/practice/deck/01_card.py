class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        if self.suit == "Spades":
            return self.value + "\u2660"
        elif self.suit == "Hearts":
            return self.value + "\u2665"
        elif self.suit == "Diamonds":
            return self.value + "\u2666"
        else:
            return self.value + "\u2663"

