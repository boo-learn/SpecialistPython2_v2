from deck_total import Card, Deck

deck = Deck()

deck.shuffle()
hand = deck.draw(10)

cards_by_suits = []
for card in hand:
    cards_by_suits.append(card.suit)
suits = set(cards_by_suits)
max_number = {'suit': None, 'num': 0}
for suit in suits:
    number = cards_by_suits.count(suit)
    if number > max_number.get('num'):
        max_number['num'] = number
        max_number['suit'] = suit
print(max_number.get('num'), max_number.get('suit'))

# TODO: Создайте колоду из 52 карт. Перемешайте ее. Вытяните 10 карт сверху
#   и посчитайте карт какой/каких мастей среди вытянутых карт оказалось больше всего?
