# Начнем с создания карты
class Suit:
    def __init__(self, rusname: str, inglname: str, sign):
        self.rusname = rusname
        self.inglname = inglname
        self.sign = sign
#     def to_sign(self):
#         return f"{self.sign}"
    
class Card:
    def __init__(self, value, suit: Suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        # TODO-1: метод возвращает строковое представление карты в виде: 10♥ и A♦
        return f"{self.value} {self.suit.sign}"

spades = Suit("пики", "spades", '\u2660')
# print(spades.to_sign())
clubs = Suit("трефы", "clubs", '\u2663')
# print(clubs.to_sign())
diamonds = Suit("бубны", "diamonds", '\u2666')
hearts = Suit("червы", "hearts", '\u2665')


# Создадим несколько карт
card1 = Card("10", hearts)
card2 = Card("A", diamonds)

# Выведем карты на экран в виде: 10♥ и A♦
print(card1.to_str())
print(card2.to_str())
