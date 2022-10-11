
class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        if self.suit == 'Hearts':
            uni_suit = '\u2665'
        elif self.suit == 'Diamonds':
            uni_suit = '\u2666'
        elif self.suit == 'Spades':
            uni_suit = '\u2660'
        else:
            uni_suit = '\u2663'
        return f'{self.value}{uni_suit}'


# Создадим несколько карт
card1 = Card("10", "Hearts")
card2 = Card("A", "Diamonds")

# Выведем карты на экран в виде: 10♥ и A♦
print(card1.to_str())
print(card2.to_str())

# Пример, вывод иконок мастей:
