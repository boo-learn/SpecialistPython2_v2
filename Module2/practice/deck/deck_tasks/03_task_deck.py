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


# Задание: Теперь создадим колоду из 52-ух карт и реализуем все методы
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


# Создаем колоду
deck = Deck()

# Выводим колоду в формате указанном в основном задании
print(deck.show())
# Тусуем колоду
deck.shuffle()
print(deck.show())

# Возьмем 5 карт "в руку"
hand = deck.draw(5)
# Выводим колоду, чтобы убедиться что 5 верхних карт отсутствуют
print(deck.show())
# Выводим список карт "в руке"(список hand)
print(*hand)
