# Начнем с создания карты
class Card:
    def __init__(self, value, type):
        self.value = value
        self.type = type

        if self.type == 'Hearts':
            self.suit = '\u2665'
        elif self.type == 'Diamonds':
            self.suit = '\u2666'
        elif self.type == 'Clubs':
            self.suit = '\u2663'
        elif self.type == 'Spades':
            self.suit = '\u2660'
        else:
            self.suit = None

    def to_str(self):
        return self.value + self.suit

    def equal_suit(self, other_card):
        if self.suit == other_card.suit:
            return True


# Создадим несколько карт
card1 = Card("10", "Hearts")
card2 = Card("A", "Spades")

# Выведем карты на экран в виде: 10♥ и A♦
print(card1.to_str())
print(card2.to_str())

# Проверим, одинаковые ли масти у карт
if card1.equal_suit(card2):
    print(f"У карт: {card1.to_str()} и {card2.to_str()} одинаковые масти")
else:
    print(f"У карт: {card1.to_str()} и {card2.to_str()} разные масти")
