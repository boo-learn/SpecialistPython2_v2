# Начнем с создания карты
class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        # TODO-1: метод возвращает строковое представление карты в виде: 10♥ и A♦
        ...
        return f"{self.value}{suits.get(self.suit)}"
suits = {
"Red diamong": "\u2661",
"Black diamond": "\u2666",
"Red club": "\u2663",
"Black club": "\u2667",
"Red heart": "\u2665",
"Black heart": "\u2661",
"Red spade": "\u2660",
"Black spade": "\u2664"}

# Создадим несколько карт
card1 = Card("10", "Black spade")
card2 = Card("A", "Red heart")

# Выведем карты на экран в виде: 10♥ и A♦
print(card1.to_str())
print(card2.to_str())

# Пример, вывод иконок мастей:
# print('\u2661', '\u2665')
# print('\u2662', '\u2666')
# print('\u2667', '\u2663')
# print('\u2664', '\u2660')
