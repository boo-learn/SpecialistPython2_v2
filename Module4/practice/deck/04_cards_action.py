class Card:
    # TODO-0: сюда копируем реализацию класса карты из предыдущего задания
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):        
        card_suits = {'Diamonds':'\u2666' ,'Hearts':'\u2665' , 'Spades':'\u2663' , 'Clubs':'\u2660'}
        return f'{self.value}{card_suits[self.suit]}'

    def equal_suit(self, other_card):
        # TODO-1: метод возвращает True - если масти карт равны или False - если нет
        return self.suit == other_card.suit


cards = []
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
for suit in suits:
    for value in values:
        card = Card(value, suit)
        cards.append(card)

# TODO-2: Выведите карты в формате: cards[кол-во]2♥, 3♥, 4♥ ... A♥, 2♦, 3♦ ... A♦, ...
#  кол-во берем от размера списка cards
print('cards[{}]{}'.format(len(cards), (', '.join([card.to_str() for card in cards]))))
