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


# Создадим несколько карт
card1 = Card("10", "Hearts")
card2 = Card("A", "Diamonds")

# Выведем карты на экран в виде: 10♥ и A♦
print(card1.to_str())
print(card2.to_str())

# Пример, вывод иконок мастей:
print('\u2661', '\u2665')
print('\u2662', '\u2666')
print('\u2667', '\u2663')
print('\u2664', '\u2660')
