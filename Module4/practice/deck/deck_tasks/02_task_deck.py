from deck_total import Card, Deck

# TODO: Создайте колоду из 52 карт. Перемешайте ее. Вытяните 10 карт сверху
#   и посчитайте карт какой/каких мастей среди вытянутых карт оказалось больше всего?

deck = Deck()
deck.shuffle()
hand = deck.draw(10)

num_suits = {
    'Diamonds': 0,
    'Hearts': 0,
    'Spades': 0,
    'Clubs': 0
}
for card in hand:
    num_suits[card.suit] += 1

max_num_suits = max(num_suits.values())

print('Больше всего выпало:')
for suit, num_suit in num_suits.items():
    if num_suit == max_num_suits:
        print(suit, num_suit)
