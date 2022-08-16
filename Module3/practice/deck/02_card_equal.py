class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        if self.suit == "Hearts":
            return f"\u2665 {self.value} "
        elif self.suit == "Diamonds":
            return f"\u2666 {self.value} "
        elif self.suit == "Spades":
            return f"\u2664{self.value} "
        elif self.suit == "Clubs":
            return f"\u2667{self.value} "

    def equal_suit(self, other_card):
        if self.suit == other_card:
            return 1
        else:
            return 0


# Создадим несколько карт
card1 = Card("10", "Hearts")
card2 = Card("A", "Diamonds")

# Выведем карты на экран в виде: 10♥ и A♦
print(card1.to_str())
print(card2.to_str())

# Пример, вывод иконок мастей:
#print('\u2661', '\u2665')
#print('\u2662', '\u2666')
#print('\u2667', '\u2663')
#print('\u2664', '\u2660')
if card1.equal_suit(card2):
    print(f"У карт: {card1.to_str()} и {card2.to_str()} одинаковые масти")
else:
    print(f"У карт: {card1.to_str()} и {card2.to_str()} разные масти")

