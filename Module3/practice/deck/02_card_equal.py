# Начнем с создания карты

class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты
        self.suit_dict = {
            'Hearts': '\u2665',
            'Diamonds': '\u2666',
            'Spades': '\u2660',
            'Clubs': '\u2663'
        }

    def to_str(self):
        return self.value + self.suit_dict.get(self.suit)

    def equal_suit(self, other_card):
        # TODO-1: метод возвращает True - если масти карт равны или False - если нет
        return self.suit == other_card.suit



# Создадим несколько карт
card1 = Card("10", "Spades")
card2 = Card("A", "Hearts")

# Выведем карты на экран в виде: 10♥ и A♦
print(card1.to_str())
print(card2.to_str())

# Проверим, одинаковые ли масти у карт
if card1.equal_suit(card2):
    print(f"У карт: {card1.to_str()} и {card2.to_str()} одинаковые масти")
else:
    print(f"У карт: {card1.to_str()} и {card2.to_str()} разные масти")
