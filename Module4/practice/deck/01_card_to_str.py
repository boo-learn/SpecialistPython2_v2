# Начнем с создания карты
class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        # TODO-1: метод возвращает строковое представление карты в виде: 10♥ и A♦
        if self.suit == 'Diamonds': return f" {self.value}{Diamonds}"
        elif self.suit == 'Hearts': return f" {self.value}{Hearts}"
        elif self.suit == 'Spades': return f" {self.value}{Spades}"
        elif self.suit == 'Clubs': return f" {self.value}{Clubs}"

Diamonds = '\u2666'
Hearts = '\u2665'
Spades = '\u2660'
Clubs = '\u2663'

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
