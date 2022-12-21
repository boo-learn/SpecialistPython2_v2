# Начнем с создания карты
class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        if self.suit == "Hearts":
            icon = '\u2665'
        elif self.suit == "Diamonds":
            icon = '\u2666'
        elif self.suit == "Clubs":
            icon = '\u2667'
        elif self.suit == "Spades":
            icon = '\u2664'
        else:
            return
        return f"{self.value}{icon}"

    def equal_suit(self, other_card):
        return self.suit == other_card.suit


# Создадим несколько карт
card1 = Card("10", "Hearts")
card2 = Card("A", "Hearts")

# Проверим, одинаковые ли масти у карт
if card1.equal_suit(card2):
    print(f"У карт: {card1.to_str()} и {card2.to_str()} одинаковые масти")
else:
    print(f"У карт: {card1.to_str()} и {card2.to_str()} разные масти")
