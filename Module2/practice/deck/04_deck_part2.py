import random


class Card:
    HEARTS = "Hearts"
    DIAMONDS = "Diamonds"
    SPADES = "Spades"
    CLUBS = "Clubs"

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        icons = {
            "Diamonds": "\u2666",
            "Hearts": "\u2665",
            "Spades": "\u2660",
            "Clubs": "\u2663"
        }
        return f"{self.value}{icons[self.suit]}"

    def equal_suit(self, other_card):
        return self.suit == other_card.suit

    def more(self, other_card):
        values = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
        suits = (Card.SPADES, Card.CLUBS, Card.DIAMONDS, Card.HEARTS)
        if values.index(self.value) == values.index(other_card.value):
            return suits.index(self.suit) > suits.index(other_card.suit)
        else:
            return values.index(self.value) > values.index(other_card.value)

    def less(self, other_card):
        values = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
        suits = (Card.SPADES, Card.CLUBS, Card.DIAMONDS, Card.HEARTS)
        if values.index(self.value) == values.index(other_card.value):
            return suits.index(self.suit) < suits.index(other_card.suit)
        else:
            return values.index(self.value) < values.index(other_card.value)


class Deck:
    def __init__(self):
        self.cards = []
        values = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
        suits = (Card.HEARTS, Card.DIAMONDS, Card.CLUBS, Card.SPADES)
        for i in range(len(suits)):
            for j in range(len(values)):
                self.cards.append(Card(values[j], suits[i]))

    def show(self):
        res_str = f"deck[{len(self.cards)}]: "
        for card in self.cards:
            res_str += f"{card}, "
        return res_str[:-2]

    def draw(self, x):
        hand = []
        for _ in range(x):
            hand.append(self.cards.pop(0))
        return hand

    def shuffle(self):
        random.shuffle(self.cards)


deck = Deck()
deck.shuffle()
print(deck.show())
# Берем две карты из колоды
card1, card2 = deck.draw(2)

# Тестируем методы .less() и .more()
if card1.more(card2):
    print(f"{card1} больше {card2}")
if card1.less(card2):
    print(f"{card1} меньше {card2}")
