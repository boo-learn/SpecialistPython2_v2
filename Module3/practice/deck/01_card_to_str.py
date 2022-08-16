# Начнем с создания карты
class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        # TODO-1: метод возвращает строковое представление карты в виде: 10♥ и A♦
        res = f'{self.value}{self.to_suit()}'
        return res

    def to_suit(self):
        if self.suit == 'Diamonds':
            # print('\u2662', '\u2666')
            res = '\u2666'
        elif self.suit == 'Hearts':
            # print('\u2661', '\u2665')
            res = '\u2665'
        elif self.suit == 'Spades ':
            # print('\u2664', '\u2660')
            res = '\u2660'
        else: #Clubs
            # print('\u2667', '\u2663')
            res = '\u2663'

        return res


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
