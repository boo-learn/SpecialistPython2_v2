# Начнем с создания карты
class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        # TODO-0: скопируйте реализацию метода из предыдущей задачи
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

    def equal_suit(self, other_card):
        # TODO-1: метод возвращает True - если масти карт равны или False - если нет
        if self.suit == other_card.suit:
            res = True
        else:
            res = False

        return res


# Создадим несколько карт
card1 = Card("10", "Hearts") 
card2 = Card("A", "Diamonds")

# Проверим, одинаковые ли масти у карт
if card1.equal_suit(card2):
    print(f"У карт: {card1.to_str()} и {card2.to_str()} одинаковые масти")
else:
    print(f"У карт: {card1.to_str()} и {card2.to_str()} разные масти")
