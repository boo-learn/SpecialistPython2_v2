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

    def __gt__(self, other_card):
        values = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
        suits = (Card.SPADES, Card.CLUBS, Card.DIAMONDS, Card.HEARTS)
        if values.index(self.value) == values.index(other_card.value):
            return suits.index(self.suit) > suits.index(other_card.suit)
        else:
            return values.index(self.value) > values.index(other_card.value)

    def __lt__(self, other_card):
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

    def __str__(self):
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

    def __getitem__(self, item):
        return self.cards[item]

    def __iter__(self):
        return iter(self.cards)


deck = Deck()
# Задачи - реализовать нативную работу с объектами:
# 1. Вывод колоды в терминал:
print(deck)  # вместо print(deck.show())
deck.shuffle()
card1, card2 = deck.draw(2)
# 2. Вывод карты в терминал:
print(card1)  # вместо print(card1.to_str())

# 3. Сравнение карт:
if card1 > card2:
    print(f"{card1} больше {card2}")

# 4. Итерация по колоде:
for card in deck:
    print(card)

# Просмотр карты в колоде по ее индексу:
print(deck[6])
