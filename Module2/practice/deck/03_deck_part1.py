# Начнем с создания карты
import random


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def to_str(self):
        icons = {
            'Hearts': '\u2665',
            'Diamonds': '\u2666',
            'Clubs': '\u2663',
            'Spades': '\u2660'
        }
        return f"{self.value}{icons.get(self.suit)}"

    def equal_suit(self, other_card):
        return self.suit == other_card.suit


class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'A', 'K', 'Q', 'J']
        suits = ['Hearts', 'Diamonds', 'Clubs', "Spades"]
        self.cards = []
        for suit in suits:
            for value in values:
                card = Card(value, suit)
                self.cards.append(card)

    def show(self):
        deck_str = f"deck[{len(self.cards)}]"
        for card in self.cards:
            deck_str += card.to_str() + ','
        return deck_str

    def draw(self, x):
        self.cards = self.cards[x:]
        return self.cards[:x]

    def shuffle(self):
        random.shuffle(self.cards)


# Создаем колоду
deck = Deck()
# Выводим колоду в формате указанном в основном задании
print(deck.show())
# Тусуем колоду
deck.shuffle()
print(deck.show())
#
# # Возьмем 5 карт "в руку"
hand = deck.draw(5)
# # Выводим колоду, чтобы убедиться что 5 верхних карт отсутствуют
print(deck.show())
# # Выводим список карт "в руке"(список hand)
print(hand)
