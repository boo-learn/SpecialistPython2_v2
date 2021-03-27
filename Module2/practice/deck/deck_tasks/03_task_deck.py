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

    def __eq__(self, other):
        return self.value == other.value and self.suit == other.suit


class Deck:
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = [Card.HEARTS, Card.DIAMONDS, Card.CLUBS, Card.SPADES]

    def __init__(self):
        self.__cards = []
        for key in Deck.suits:
            for i in Deck.values:
                self.__cards.append(Card(i, key))
        self.index = 0

    def __repr__(self):
        # Переопределелили метод repr (принт)
        tmp = []
        for i in self.__cards:
            tmp.append(Card.__repr__(i))
        return f'deck[{len(self.__cards)}]: {", ".join(tmp)}'

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        try:
            card = self.__cards[self.index]
        except:
            raise StopIteration
        self.index += 1
        return card

    def draw(self, x):
        # начало списка считаем верхом колоды
        cards = []
        for _ in range(x):
            cards.append(self.__cards.pop(0))
        return cards

    def shuffle(self):
        random.shuffle(self.__cards)

    def suit_calc(self):
        hearts = []
        diamonds = []
        clubes = []
        spades = []
        for i in range(len(self.__cards)):
            if self.__cards[i].suit == Card.HEARTS:
                hearts.append(self.__cards[i])
            elif self.__cards[i].suit == Card.DIAMONDS:
                diamonds.append(self.__cards[i])
            elif self.__cards[i].suit == Card.CLUBS:
                clubes.append(self.__cards[i])
            else:
                spades.append(self.__cards[i])
        return max(len(hearts), len(diamonds), len(clubes), len(spades))

# Задание-3
# Создайте колоду из 52 карт.
# Перемешайте ее.
# Вытяните одну карту сверху.
# Снова перемешайте колоду и вытяните еще одну.
# Если вторая карта меньше первой, повторите “перемешать + вытянуть”, до тех пор,
# пока не вытяните карту больше предыдущей карты. В качестве результата выведи все вытягиваемые карты в консоль.
deck = Deck()
deck.shuffle()
card_zero = deck.draw(1)
deck.shuffle()
card_next = deck.draw(1)
hand = [card_zero]
print(card_zero)
print(card_next)
while card_next < card_zero:
    deck.shuffle()
    hand.append(card_next)
    card_zero = card_next
    card_next = deck.draw(1)
else:
    hand.append(card_next)

print(*hand)
