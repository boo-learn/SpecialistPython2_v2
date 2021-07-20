class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты


cards = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']

hearts_cards = []
for i in range(len(cards)):
    hearts_cards.append(Card(cards[i],"Hearts"))

diamonds_cards = []
for i in range(len(cards)):
    hearts_cards.append(Card(cards[i],"Diamonds"))

S=""
for i in range(len(hearts_cards)):
    S= S + hearts_cards[i].value + '\u2665 ,'

print(S)

