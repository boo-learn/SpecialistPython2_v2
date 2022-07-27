# Начнем с создания карты
class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты
        self.suit_icons = {'Hearts': '\u2665', 'Diamonds': '\u2666', 'Clubs': '\u2663', 'Spades': '\u2660'}

    def to_str(self):
        return f'{self.value}{self.suit_icons[self.suit]}'

    def equal_suit(self, other_card):
        return True if self.suit == other_card.suit else False


# Создадим несколько карт
card1 = Card("10", "Hearts")
card2 = Card("A", "Diamonds")

# Проверим, одинаковые ли масти у карт
if card1.equal_suit(card2):
    print(f"У карт: {card1.to_str()} и {card2.to_str()} одинаковые масти")
else:
    print(f"У карт: {card1.to_str()} и {card2.to_str()} разные масти")

