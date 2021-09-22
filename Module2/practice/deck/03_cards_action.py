class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        symbols = {
            'Hearts': '\u2665',
            'Diamonds': '\u2666',
            'Clubs': '\u2663',
            'Spades': '\u2660'
        }
        return f'{self.value}{symbols[self.suit]}'
    
    def equal_suit(self, other_card): #проверяет, одинаковые ли масти у карт
        return self.suit == other_card.suit

cards = []
# TODO-1: в список cards добавьте ВСЕ карты всех мастей
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

for suit in suits:
    for value in values:
        card = Card(value, suit)
        cards.append(card)

# TODO-2: Выведите карты в формате: cards[кол-во]2♥, 3♥, 4♥ ... A♥, 2♦, 3♦ ... A♦, ....
print(", ".join([card.to_str() for card in cards]))
