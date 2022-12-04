class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        if self.suit == "Hearts":
            self.suit = '\u2665'
            return self.value + self.suit
        elif self.suit == "Diamonds":
            self.suit = '\u2666'
            return self.value + self.suit
        elif self.suit == "Clubs":
            self.suit = '\u2663'
            return self.value + self.suit
        elif self.suit == "Spades":
            self.suit = '\u2660'
            return self.value + self.suit


# Создадим несколько карт
card1 = Card("10", "Hearts")
card2 = Card("A", "Diamonds")

# Выведем карты на экран в виде: 10♥ и A♦
print(card1.to_str())
print(card2.to_str())

# Пример, вывод иконок мастей:
print('\u2661', '\u2665')
print('\u2662', '\u2666')
print('\u2667', '\u2663')
print('\u2664', '\u2660')
