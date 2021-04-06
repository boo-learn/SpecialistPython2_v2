# Начнем с создания карты
class Card:
    def __init__(self, value, suit):
        self.value_card = value
        self.suit_card = suit

    def to_str(self):
        if self.suit_card == "Diamonds":
            self.suit_card_icone = "♦"
        elif self.suit_card == "Hearts":
            self.suit_card_icone = "♥"
        elif self.suit_card == "Spades":
            self.suit_card_icone = "♠"
        else:
            self.suit_card_icone = "♣"
        return f"{self.value_card}{self.suit_card_icone}"

    def equal_suit(self, other_card):
        if self.suit_card == other_card.suit_card:
            return True
        else:
            return False


# Создадим несколько карт
card1 = Card("10", "Hearts")
card2 = Card("A", "Diamonds")

# Выведем карты на экран в виде: 10♥ и A♦
print(card1.to_str())
print(card2.to_str())

# Проверим, одинаковые ли масти у карт
if card1.equal_suit(card2):
    print(f"У карт: {card1.to_str()} и {card2.to_str()} одинаковые масти")
else:
    print(f"У карт: {card1.to_str()} и {card2.to_str()} разные масти")
