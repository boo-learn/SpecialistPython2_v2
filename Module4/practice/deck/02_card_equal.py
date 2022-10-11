

# Начнем с создания карты
class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        st = ''
        # TODO-1: метод возвращает строковое представление карты в виде: 10♥ и A♦
        if self.suit == 'Hearts':
            st = '\u2665'
        elif self.suit == 'Diamonds':
            st = '\u2666'
        elif self.suit == 'Clubs':
            st = '\u2663'
        elif self.suit == 'Spades':
            st = '\u2660'

        return f'{self.value}{st}'

    def equal_suit(self, other_card):

            # TODO-1: метод возвращает True - если масти карт равны или False - если нет
        return True if other_card.suit == self.suit else False



# Создадим несколько карт
card1 = Card("10", "Hearts")
card2 = Card("A", "Diamonds")

# Выведем карты на экран в виде: 10♥ и A♦
print(card1.to_str())
print(card2.to_str())

'''
# Пример, вывод иконок мастей:
print('\u2661', '\u2665')
print('\u2662', '\u2666')
print('\u2667', '\u2663')
print('\u2664', '\u2660')
'''

if card1.equal_suit(card2):
    print(f"У карт: {card1.to_str()} и {card2.to_str()} одинаковые масти")
else:
    print(f"У карт: {card1.to_str()} и {card2.to_str()} разные масти")
