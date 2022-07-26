# Начнем с создания карты
class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def unicode_suit(self):
        if self.suit == "Hearts":
            return '\u2665'
        if self.suit == "Diamonds":
            return '\u2666'
        if self.suit == "Spades":
            return '\u2660'
        if self.suit == "Clubs":
            return '\u2663'
        else:
            return 'Suit error'

    def to_str(self):
        return f'{self.value}{self.unicode_suit()}'


# Создадим несколько карт
card1 = Card("10", "Hearts")
card2 = Card("A", "Diamonds")

# Выведем карты на экран в виде: 10♥ и A♦
print(card1.to_str())
print(card2.to_str())

# # Пример, вывод иконок мастей:
# print('\u2661', '\u2665')
# print('\u2662', '\u2666')
# print('\u2667', '\u2663')
# print('\u2664', '\u2660')
