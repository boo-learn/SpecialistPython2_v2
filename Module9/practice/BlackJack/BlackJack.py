from card import Deck, Card
deck = Deck()

def sum_points(cards):
    summ = 0
    for card in cards:
        for card_key in Deck.card_points.keys():
            if card.value == card_key:
                summ += Deck.card_points[card.value]
    if summ > 21:
        summ = 0
        for card in cards:
            for card_key in Deck.card_points.keys():
                if card.value == card_key:
                    if card.value == 'A':
                        summ += 1
                    else:
                        summ += Deck.card_points[card.value]
    return summ


cards = [
    Card("9", Card.HEARTS),
    Card("A", Card.DIAMONDS),
    # Card("2", Card.DIAMONDS),
    # Card("A", Card.DIAMONDS),

]
print(sum_points(cards))
