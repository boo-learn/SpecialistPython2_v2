class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        if self.suit == "Hearts":
            return f"{self.value}\u2665"
        if self.suit == "Diamonds":
            return f"{self.value}\u2666"
        if self.suit == "Spades":
            return f"{self.value}\u2663"
        else:
            return f"{self.value}\u2660"

    def equal_suit(self, other_card):
        pass


# Создадим несколько карт
card1 = Card("10", "Hearts")
card2 = Card("A", "Diamonds")
card3 = Card("A", "Spades")
card4 = Card("A", "Clubs")

# Выведем карты на экран в виде: 10♥ и A♦
print(card1.to_str())
print(card2.to_str())
print(card3.to_str())
print(card4.to_str())

# Проверим, одинаковые ли масти у карт
if card1.equal_suit(card2):
    print(f"У карт: {card1.to_str()} и {card2.to_str()} одинаковые масти")
else:
    print(f"У карт: {card1.to_str()} и {card2.to_str()} разные масти")
