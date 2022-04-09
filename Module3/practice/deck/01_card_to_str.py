# Начнем с создания карты
class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        if self.suit == "Diamonds":
            print('\u2662')
        elif self.suit == "Hearts":
            print('\u2664')
        elif self.suit == "Spades":
            print('\u2667')
        elif self.suit == "Clubs":
            print('\u2661')
        return f'{self.value} {self.suit}'
        # TODO-1: метод возвращает строковое представление карты в виде: 10♥ и A♦
        ...


# Создадим несколько карт
card1 = Card("10", "Hearts")
card2 = Card("A", "Diamonds")

# Выведем карты на экран в виде: 10♥ и A♦
print(card1.to_str())
print(card2.to_str())
