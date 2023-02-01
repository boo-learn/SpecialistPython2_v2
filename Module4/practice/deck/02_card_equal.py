# Начнем с создания карты
class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        icon = None
        if self.suit == "Hearts":
            icon = '\u2665'
        elif self.suit == "Diamonds" :
            icon = '\u2666'
        elif self.suit == "Spades":
            icon = '\u2660'
        else:
            icon = '\u2663'
        return f'{self.value}{icon}'

    def equal_suit(self, other_card):
        
        if self.suit == other_card.suit:
            return True
        return False



# Создадим несколько карт
card1 = Card("10", "Hearts")
card2 = Card("A", "Diamond")

# Проверим, одинаковые ли масти у карт
if card1.equal_suit(card2):
    print(f"У карт: {card1.to_str()} и {card2.to_str()} одинаковые масти")
else:
    print(f"У карт: {card1.to_str()} и {card2.to_str()} разные масти")
