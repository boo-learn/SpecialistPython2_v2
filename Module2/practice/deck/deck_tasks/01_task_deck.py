# Сюда отправляем решение первой задачи с колодой
import random


class Card:
    HEARTS = "Hearts"
    DIAMONDS = "Diamonds"
    SPADES = "Spades"
    CLUBS = "Clubs"
    suits_symbols = {"Diamonds": '\u2666',
                     "Hearts": '\u2665',
                     "Spades": '\u2660',
                     "Clubs": '\u2663'}

    def __init__(self, value, type):
        self.value = value
        self.type = type

    def __repr__(self):
        return f"{self.value}{Card.suits_symbols[self.type]}"

    def compare(self, last_card):
        types = {"spades": 0, "clubs": 1, "diamonds": 2, "hearts": 3}
        values = {'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7,
                  '10': 8, 'J': 9, 'Q': 10, 'K': 11, 'A': 12}
        if self.value == last_card.value:
            return types[self.type] > types[last_card.type]
        else:
            return types[self.value] > types[last_card.value]

class Deck:
    types = [Card.HEARTS, Card.DIAMONDS, Card.SPADES, Card.CLUBS]
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self):
        self.cards = []
        for type in Deck.types:
            for value in Deck.values:
                self.cards.append(Card(value, type))


    def __repr__(self):
        string = f"deck[{len(self.cards)}]: "
        string += ", ".join([str(card) for card in self.cards])
        return string

    def draw(self, x):
        # Считаем начало списка - верхом колоды
        # buf = self.cards
        # self.cards = self.cards[x:]
        # return buf[:x]
        cards = []
        for _ in range(x):
            cards.append(self.cards.pop(0))
        return cards

    def shuffle(self):
        random.shuffle(self.cards)


deck = Deck()
# print(deck.show())
print(deck)  # --> print(deck.__repr__())
deck.shuffle()
print(deck)
cards = deck.draw(2)
print(deck)
print(cards)
# for card in cards:
#     print(card.to_str(), end=" ")
# print("cards = ", cards)


last_card = cards[0]
current_card = cards[1]
if last_card.compare(current_card):
    print(f'Карта {last_card} больше чем карта {current_card}')
else:
    print(f'Карта {current_card} больше чем карта {last_card}')

