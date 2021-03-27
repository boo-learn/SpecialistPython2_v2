import random


class Card:
    HEARTS = 'Hearts'
    DIAMONDS = 'Diamonds'
    SPADES = 'Spades'
    CLUBS = 'Clubs'

    suit_simbol = {HEARTS: '\u2665',
                   DIAMONDS: '\u2666',
                   CLUBS: '\u2663',
                   SPADES: '\u2660'}

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f'{self.value}{Card.suit_simbol[self.suit]}'

    def equal_suit(self, card2):
        return self.suit == card2.suit

    def __gt__(self, card2):
        if self.equal_suit(card2):
            return Deck.suits.index(self.suit) < Deck.suits.index(card2.suit)
        else:
            return Deck.values.index(self.value) > Deck.values.index(card2.value)


class Deck:
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = [Card.HEARTS, Card.DIAMONDS, Card.CLUBS, Card.SPADES]

    def __init__(self):
        self.__cards = []
        for key in Deck.suits:
            for i in Deck.values:
                self.__cards.append(Card(i, key))

    def __repr__(self):
        # Переопределелили метод repr (принт)
        tmp = []
        for i in self.__cards:
            tmp.append(Card.__repr__(i))
        return f'deck[{len(self.__cards)}]: {", ".join(tmp)}'

    def draw(self, x):
        # начало списка считаем верхом колоды
        cards = []
        for _ in range(x):
            cards.append(self.__cards.pop(0))
        return cards

    def shuffle(self):
        random.shuffle(self.__cards)


# Задание-2
# Создайте колоду из 52 карт.
deck = Deck()
# Перемешайте ее.
deck.shuffle()
# Вытяните 10 карт сверху и посчитайте карт какой/каких мастей среди вытянутых карт оказалось больше всего?
cards = deck.draw(10)

hearts = []
diamonds = []
clubs = []
spades = []

print(cards)
for i in range(len(cards)):
    if cards[i].suit == Card.HEARTS:
        hearts.append(cards[i])
    elif cards[i].suit == Card.DIAMONDS:
        diamonds.append(cards[i])
    elif cards[i].suit == Card.CLUBS:
        clubs.append(cards[i])
    else:
        spades.append(cards[i])
max_suits = max(len(hearts), len(diamonds), len(clubs), len(spades))

result = []
if len(hearts) == max_suits:
    result.append(Card.HEARTS)
if len(diamonds) == max_suits:
    result.append(Card.DIAMONDS)
if len(clubs) == max_suits:
    result.append(Card.CLUBS)
if len(spades) == max_suits:
    result.append(Card.SPADES)
print('в вытянутой руке больше всего карт масти: ', *result)
