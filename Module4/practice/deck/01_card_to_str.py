# Начнем с создания карты
class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты
        self.suit_new = ...

    def to_str(self):
        # TODO-1: метод возвращает строковое представление карты в виде: 10♥ и A♦
        if self.suit == 'Hearts':
            self.suit_new = '\u2661'
        elif self.suit == 'Diamonds':
            self.suit_new = '\u2662'
        elif self.suit == 'Spades':
            self.suit_new = '\u2664'
        elif self.suit == 'Clubs':
            self.suit_new = '\u2667'
        return self.value + self.suit_new


# Создадим несколько карт
card1 = Card("10", "Hearts")
card2 = Card("A", "Diamonds")
card3 = Card("10", "Spades")
card4 = Card("A", "Clubs")

# Выведем карты на экран в виде: 10♥ и A♦
print(card1.to_str())
print(card2.to_str())
print(card3.to_str())
print(card4.to_str())

# Пример, вывод иконок мастей:
#print('\u2661', '\u2665')
#print('\u2662', '\u2666')
#print('\u2667', '\u2663')
#print('\u2664', '\u2660')
