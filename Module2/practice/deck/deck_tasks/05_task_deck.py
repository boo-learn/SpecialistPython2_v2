import random


class Card:
    HEARTS = 'Hearts'
    DIAMONDS = 'Diamonds'
    SPADES = 'Spades'
    CLUBS = 'Clubs'

    suit_symbol = {HEARTS: '\u2665',
                   DIAMONDS: '\u2666',
                   SPADES: '\u2660',
                   CLUBS: '\u2663'}

    def __init__(self, value, type_card):
        self.value = value
        self.type = type_card

    def __repr__(self):
        return f"{self.value}{Card.suit_symbol[self.type]}"

    def __gt__(self, other):
        if Deck.values.index(self.value) == Deck.values.index(other.value):
            return Deck.suits.index(self.type) > Deck.suits.index(other.type)
        else:
            return Deck.values.index(self.value) > Deck.values.index(other.value)

    def __lt__(self, other):
        if Deck.values.index(self.value) == Deck.values.index(other.value):
            return Deck.suits.index(self.type) < Deck.suits.index(other.type)
        else:
            return Deck.values.index(self.value) < Deck.values.index(other.value)

    def equal_suit(self, card):
        return self.type == card.type


class Deck:
    suits = [Card.HEARTS, Card.DIAMONDS, Card.CLUBS, Card.SPADES]
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self, num_cards=52):
        if num_cards == 36:
            self.cards = [Card(value, type_card)
                          for type_card in Deck.suits for value in Deck.values[4:]]
        else:
            self.cards = [Card(value, type_card)
                          for type_card in Deck.suits for value in Deck.values]

    def __repr__(self):
        return f'deck[{len(self.cards)}]: {", ".join([str(card) for card in self.cards])}'

    def draw(self, x):
        cards = []
        for _ in range(x):
            cards.append(self.cards.pop(0))
        return cards

    def shuffle(self):
        random.shuffle(self.cards)


def find_beat_card(deck, card):
    for i in deck:
        if i.equal_suit(card) and i > card:
            return i
    return None


def find_attack_card(table, deck_player):
    for i in table:
        for j in deck_player:
            if j.equal_suit(i):
                return j
    return None


pull = []
deck = Deck()
deck.shuffle()
player1 = deck.draw(6)
player2 = deck.draw(6)
min_card_player1 = min(player1)
print(f'Игрок 1 выкладывает на стол карту {min_card_player1}')
pull.append(min_card_player1)
player1.remove(min_card_player1)
card_beat_pl2 = find_beat_card(player2, min_card_player1)
if card_beat_pl2 != None:
    print(
        f'Игрок 2 бьет карту {min_card_player1} Игрока 1 картой {card_beat_pl2}')
    pull.append(card_beat_pl2)
    player2.remove(card_beat_pl2)
    card_attack_pl1 = find_attack_card(pull, player1)
    if card_attack_pl1 != None:
        print(f'Игрок 1 подкидывает карту {card_attack_pl1}')
    else:
        print(f'Игроку 1 нечего подкидывать')
else:
    print(f'Игрок 2 не может побить карту {min_card_player1} Игрока 1')
