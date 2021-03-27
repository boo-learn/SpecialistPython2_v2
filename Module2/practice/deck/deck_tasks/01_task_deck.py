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
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = [HEARTS, DIAMONDS, CLUBS, SPADES]

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f'{self.value}{Card.suit_simbol[self.suit]}'

    def equal_suit(self, card2):
        return self.suit == card2.suit

    def more(self, card2):
        if self.equal_suit(card2):
            return Card.suits.index(self.suit) < Card.suits.index(card2.suit)
        else:
            return Card.values.index(self.value) > Card.values.index(card2.value)


class Deck:
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = [Card.HEARTS, Card.DIAMONDS, Card.CLUBS, Card.SPADES]

    def __init__(self):
        self.cards = []
        for key in Deck.suits:
            for i in Deck.values:
                self.cards.append(Card(i, key))

    def __repr__(self):
        # Переопределелили метод repr (принт)
        tmp = []
        for i in self.cards:
            tmp.append(Card.__repr__(i))
        return f'deck[{len(self.cards)}]: {", ".join(tmp)}'

    def draw(self, x):
        # начало списка считаем верхом колоды
        cards = []
        for _ in range(x):
            cards.append(self.cards.pop(0))
        return cards

    def shuffle(self):
        random.shuffle(self.cards)


# Задание-1
# Создайте колоду из 52 карт.
deck = Deck()
# Перемешайте ее.
deck.shuffle()
# Вытяните две карты сверху.
cards = deck.draw(2)
print(cards)

# Сравните эти карты и выведите сообщение формата: “карта A♦ больше J♣”
if cards[0].more(cards[1]):
    print(f'карта {cards[0]} больше {cards[1]}')
else:
    print(f'карта {cards[1]} больше {cards[0]}')
