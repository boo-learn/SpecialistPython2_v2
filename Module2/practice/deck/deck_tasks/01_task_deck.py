import random


class Card:
    DIAMONDS = "Diamonds"
    SPADES = "Spades"
    HEARTS = "Hearts"
    CLUBS = "Clubs"
    suits_symbols = {DIAMONDS: '\u2665',
                     SPADES: '\u2666',
                     HEARTS: '\u2663',
                     CLUBS: '\u2660'}

    def __init__(self, value, type):
        self.value = value
        self.type = type

    def __repr__(self):
        return f"{self.value} {Card.suits_symbols[self.type]}"

    def __gt__(self, other_card):
        if Deck.cards_list.index(self.value) == Deck.cards_list.index(other_card.value):
            return Deck.suits.index(self.type) > Deck.suits.index(other_card.type)
        else:
            return Deck.cards_list.index(self.value) > Deck.cards_list.index(other_card.value)

    def __lt__(self, other_card):
        if Deck.cards_list.index(self.value) == Deck.cards_list.index(other_card.value):
            return Deck.suits.index(self.type) < Deck.suits.index(other_card.type)
        else:
            return Deck.cards_list.index(self.value) < Deck.cards_list.index(other_card.value)


class Deck:
    suits = [Card.SPADES, Card.CLUBS, Card.DIAMONDS, Card.HEARTS]
    cards_list = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self):
        self.cards = []
        for suit in Deck.suits:
            for card in Deck.cards_list:
                self.cards.append(Card(card, suit))

    def __repr__(self):
        string = f"deck[{len(self.cards)}]: "
        string += ", ".join([str(card) for card in self.cards])
        return string

    def draw(self, x):
        # Начало списка - верх колоды
        buf = self.cards
        self.cards = self.cards[x:]
        return buf[:x]

    def shuffle(self):
        random.shuffle(self.cards)


# Задание-1
# Создайте колоду из 52 карт. Перемешайте ее. Вытяните две карты сверху.
# Сравните эти карты и выведите сообщение формата: “карта A♦ больше J♣”


deck = Deck()
deck.shuffle()
card1, card2 = deck.draw(2)
if card1 > card2:
    print(f"{card1} > {card2}")
else:
    print(f"{card2} > {card1}")
