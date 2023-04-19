# Начнем с создания карты
class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        # TODO-1: метод возвращает строковое представление карты в виде: 10♥ и A♦
        # Словарь
        value_str = {"2": "2", "3": "3", "4": "4", "5": "5", "6": "6",
                     "7": "7", "8": "8", "9": "9", "10": "10", "J": "J",
                     "Q": "Q", "K": "K", "A": "A"}
        # Символы для отображения мастей
        suit_symbols = {"Hearts": "\u2665", "Diamonds": "\u2666",
                        "Clubs": "\u2663", "Spades": "\u2660"}
        # Строковое представление "значение масть"
        return value_str[self.value] + suit_symbols[self.suit]
# Создадим несколько карт
card1 = Card("10", "Hearts")
card2 = Card("A", "Diamonds")

# Выведем карты на экран в виде: 10♥ и A♦
print(card1.to_str())
print(card2.to_str())

# Пример, вывод иконок мастей:
# print('\u2661', '\u2665')
# print('\u2662', '\u2666')
# print('\u2667', '\u2663')
# print('\u2664', '\u2660')
