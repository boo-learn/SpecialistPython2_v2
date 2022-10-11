# Начнем с создания карты
class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        suit_icon = {
        'Hearts':'\u2665',
        'Diamonds':'\u2666',
        'Clubs':'\u2663',
        'Spades':'\u2660',
        }
        for k, v in suit_icon.items():
            if k == self.suit:
                return "{}{}".format(self.value,v)
        # TODO-1: метод возвращает строковое представление карты в виде: 10♥ и A♦

def equal_suit(card1:Card, card2:Card):
    if card1.suit==card2.suit:
        return True
    else:
        return False



# TODO-1: метод возвращает True - если масти карт равны или False - если нет

# Создадим несколько карт
card1 = Card("10", "Hearts")
card2 = Card("A", "Diamonds")
card3 = Card("A", "Hearts")

# Выведем карты на экран в виде: 10♥ и A♦
print(card1.to_str())
print(card2.to_str())

print(equal_suit(card1,card2))
print(equal_suit(card1,card3))
