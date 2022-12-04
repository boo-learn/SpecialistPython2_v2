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


    def equal_suit(self, other_card):
       if card1.suit == card2.suit:
           return True
       else:
           return False


# Создадим несколько карт
card1 = Card("10", "Hearts")
card2 = Card("A", "Diamonds")

# Проверим, одинаковые ли масти у карт
if card1.equal_suit(card2):
    print(f"У карт: {card1.to_str()} и {card2.to_str()} одинаковые масти")
else:
    print(f"У карт: {card1.to_str()} и {card2.to_str()} разные масти")
