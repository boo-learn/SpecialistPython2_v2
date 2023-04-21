from deck_total import Deck

# TODO: Создайте колоду из 52 карт. Перемешайте ее. Вытяните 10 карт сверху
#   и посчитайте карт какой/каких мастей среди вытянутых карт оказалось больше всего?
deck_52_cards = Deck()
deck_52_cards.shuffle()
cards_10 = deck_52_cards.draw(10)
cards_suit = {}
for card in cards_10:
    cards_suit[card.suit] = cards_suit.get(card.suit, 0) + 1
print(cards_suit)
most_suits = []
for suit in cards_suit:
    pass
