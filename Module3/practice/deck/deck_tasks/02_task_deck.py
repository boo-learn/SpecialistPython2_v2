from deck_total import Card, Deck

# TODO: Создайте колоду из 52 карт. Перемешайте ее. Вытяните 10 карт сверху
#   и посчитайте карт какой/каких мастей среди вытянутых карт оказалось больше всего?
deck = Deck()
deck.shuffle()
hand = deck .draw(10)
ratio_hand = {"Hearts": 0, "Diamonds": 0, "Clubs": 0, "Spades": 0}
for key in ratio_hand.keys():
    for card in hand:
        if card.suit == key:
            ratio_hand.update({key: ratio_hand.get(key)+1})
for key in ratio_hand.keys():
    if ratio_hand.get(key) == max(ratio_hand.values()):
        print(key)
