from deck_total import Card, Deck

# TODO: Создайте колоду из 52 карт. Перемешайте ее. Вытяните 10 карт сверху
#   и посчитайте карт какой/каких мастей среди вытянутых карт оказалось больше всего?

deck = Deck()
deck.shuffle()
cards_hand = [card.suit for card in deck.draw(10)]
suit_counts = {suit:cards_hand.count(suit) for suit in cards_hand}
print(suit_counts)
