import random

class Card:
    
    HEARTS = "Hearts"
    DIAMONDS = "Diamonds"
    SPADES = "Spades"
    CLUBS = "Clubs"
    VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    SUITS_RANKS = ["Spades", "Clubs", "Diamonds", "Hearts"]

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def to_str(self):
        icons = {
            "Hearts": '\u2665',
            "Diamonds": '\u2666',
            "Spades": '\u2663',
            "Clubs": '\u2660',
        }
        return f"{self.value}{icons[self.suit]}"

    def equal_suit(self, other_card):
        return self.suit == other_card.suit
    
    def more(self, other_card):
        if self.value != other_card.value:
            return Card.VALUES.index(self.value) > Card.VALUES.index(other_card.value)
        else:
            return Card.SUITS_RANKS.index(self.suit) > Card.SUITS_RANKS.index(other_card.suit)

    def less(self, other_card):
        if self.value != other_card.value:
            return Card.VALUES.index(self.value) < Card.VALUES.index(other_card.value)
        else:
            return Card.SUITS_RANKS.index(self.suit) < Card.SUITS_RANKS.index(other_card.suit)


# card1 = Card("10", Card.HEARTS)
# card2 = Card("A", Card.DIAMONDS)
# 
# if card1.equal_suit(card2):
#     print(f'У карт: {card1.to_str()} и {card2.to_str()} одинаковые масти')
# else:
#     print(f'У карт: {card1.to_str()} и {card2.to_str()} разные масти')

# Задание: Теперь создадим колоду из 52-ух карт и реализуем все методы
class Deck:
    pass
    # TODO: сюда копируем реализацию класса колоды из предыдущего задания
    def __init__(self):
        self.cards = []
        self.create_deck()

    def create_deck(self):
        res = list()
        for suit in [Card.HEARTS, Card.DIAMONDS, Card.SPADES, Card.CLUBS]:
            for value in Card.VALUES:
                res.append(Card(value, suit))
        self.cards = res

    def show(self):
        to_show = [card.to_str() for card in self.cards]
        return f'deck[{len(self.cards)}]: {", ".join(to_show)}'

    def draw(self, number):
        to_show = self.cards[:number]
        self.cards = self.cards[number:]
        return to_show

    def shuffle(self):
        random.shuffle(self.cards)

    # TODO: сюда копируем реализацию класса карты из предыдущего задания
    #  реализуем новые методы



# deck = Deck()
# print(deck.show())
# deck.shuffle()
# print(deck.show())

deck = Deck()
deck.shuffle()
# print(deck.show())
# Берем две карты из колоды
card1, card2 = deck.draw(2)

if card1.more(card2):
    print(f"{card1.to_str()} больше {card2.to_str()}")
if card1.less(card2):
    print(f"{card1.to_str()} меньше {card2.to_str()}")


