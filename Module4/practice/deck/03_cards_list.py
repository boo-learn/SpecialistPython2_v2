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

        return f"{self.value}{suit_icon[self.suit]}"
        # TODO-1: метод возвращает строковое представление карты в виде: 10♥ и A♦

def equal_suit(card1:Card, card2:Card):
    if card1.suit==card2.suit:
        return True
    else:
        return False


values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

hearts_cards = []
diamonds_cards = []

for i in values:
    hearts_cards.append(Card(i,'Hearts'))
    diamonds_cards.append(Card(i, 'Diamonds'))

suits = []
for i in hearts_cards:
    suits.append(i.to_str())
print(*suits, sep=', ')
suits = []
for i in diamonds_cards:
    suits.append(i.to_str())
print(*suits, sep=', ')

