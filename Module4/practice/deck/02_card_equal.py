# Начнем с создания карты
class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        symb = ''
        if self.suit == 'Diamonds':
            symb = '\u2666'
        elif self.suit == 'Hearts':
            symb = '\u2665'
        elif self.suit == 'Spades':
            symb = '\u2660'
        elif self.suit == 'Clubs':
            symb = '\u2663'
        return f"{self.value}{symb}"

    def equal_suit(self, other_card):
        return (True if self.suit == other_card.suit else False)


# Создадим несколько карт
card1 = Card("10", "Hearts")
card2 = Card("A", "Diamonds")

# Проверим, одинаковые ли масти у карт
if card1.equal_suit(card2):
    print(f"У карт: {card1.to_str()} и {card2.to_str()} одинаковые масти")
else:
    print(f"У карт: {card1.to_str()} и {card2.to_str()} разные масти")
