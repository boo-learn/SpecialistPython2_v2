# Начнем с создания карты
class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        if self.suit == "Hearts"  : g_suit = '\u2665'
        if self.suit == "Diamonds": g_suit = '\u2666'
        if self.suit == "Clubs"   : g_suit = '\u2663'
        if self.suit == "Spades"  : g_suit = '\u2660'
        return f"{self.value}{g_suit}"
        # TODO-1: метод возвращает строковое представление карты в виде: 10♥ и A♦
        ...

    def equal_suit(self, other_card):
        if self.suit == other_card.suit: return True
        else :                      return False
        # TODO-1: метод возвращает True - если масти карт равны или False - если нет
        ...


# Создадим несколько карт
card1 = Card("10", "Hearts")
card2 = Card("A", "Diamonds")

# Проверим, одинаковые ли масти у карт
if card1.equal_suit(card2):
    print(f"У карт: {card1.to_str()} и {card2.to_str()} одинаковые масти")
else:
    print(f"У карт: {card1.to_str()} и {card2.to_str()} разные масти")
