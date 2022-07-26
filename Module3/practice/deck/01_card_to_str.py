# Начнем с создания карты
class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        if self.suit == 'Hearts':
            return f"{self.value}\u2661"
        if self.suit == 'Diamonds':
            return f"{self.value}\u2662"
        if self.suit == 'Clubs':
            return f"{self.value}\u2667"
        if self.suit == 'Spades':
            return f"{self.value}\u2664"

# Создадим несколько карт
card1 = Card("10", "Hearts")
card2 = Card("A", "Diamonds")
card3 = Card("10", "Clubs")
card4 = Card("A", "Spades")

# Выведем карты на экран в виде: 10♥ и A♦
print(card1.to_str())
print(card2.to_str())
print(card3.to_str())
print(card4.to_str())

# Пример, вывод иконок мастей:
