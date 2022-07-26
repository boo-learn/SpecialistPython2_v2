# Начнем с создания карты
class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты
        self.suit_to_pic = {"Hearts": '\u2665', "Diamonds": '\u2666', "Spades": '\u2664', "Clubs": '\u2667'}

    def to_str(self):
        return f"{self.value}{self.suit_to_pic[self.suit]}"


# Создадим несколько карт
card1 = Card("10", "Hearts")
card2 = Card("A", "Diamonds")
card3 = Card("K", "Clubs")

# Выведем карты на экран в виде: 10♥ и A♦
print(card1.to_str())
print(card2.to_str())
print(card3.to_str())
