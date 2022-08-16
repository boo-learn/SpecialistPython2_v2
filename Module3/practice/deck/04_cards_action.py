class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):

        res = f'{self.value}{self.to_suit()}'
        return res

    def to_suit(self):
        res = ''
        if self.suit == 'Diamonds':
            # print('\u2662', '\u2666')
            res = '\u2666'
        elif self.suit == 'Hearts':
            # print('\u2661', '\u2665')
            res = '\u2665'
        elif self.suit == 'Spades':
            # print('\u2664', '\u2660')
            res = '\u2660'
        elif self.suit == 'Clubs':
            # print('\u2667', '\u2663')
            res = '\u2663'

        return res

    def equal_suit(self, other_card):

        return self.suit == other_card.suit


cards = []
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
# TODO-1: в список cards добавьте ВСЕ карты всех мастей
for suit in suits:
    for value in values:
        cards.append(Card(value,suit))

# TODO-2: Выведите карты в формате: cards[кол-во]2♥, 3♥, 4♥ ... A♥, 2♦, 3♦ ... A♦, ...
#  кол-во берем от размера списка cards

cards_str = []
for value in cards:
    cards_str.append(value.to_str())

res = ','.join(cards_str)
print(f'cards[{str(len(cards_str))}]{res}')
