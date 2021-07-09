# пока без проверки на больше 21
from card import Deck, Card
deck = Deck()

def sum_points(cards):
    card_points = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 10,
        "Q": 10,
        "k": 10,
        "A": 11
    }
    summ = 0
    for card in cards:
        print(card)
        for card_set, point in card_points.items():
            if card[0] == card_set:
                summ += point
    return summ

card1 = ["9", "Hearts"]
card2 = ["A", "Diamonds"]
cards = (card1, card2)
print(sum_points(cards))
