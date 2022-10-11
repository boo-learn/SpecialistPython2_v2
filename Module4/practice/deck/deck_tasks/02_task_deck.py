from deck_total import Card, Deck

# TODO: Создайте колоду из 52 карт. Перемешайте ее. Вытяните 10 карт сверху
#   и посчитайте карт какой/каких мастей среди вытянутых карт оказалось больше всего?

deck = Deck()
deck.shuffle()
hand = deck.draw(10)
hearts = 0
diamonds = 0
clubs = 0
spades = 0
for kard in hand:
    if kard.suit == 'Hearts':
        hearts += 1
    elif kard.suit == 'Diamonds':
        diamonds += 1
    elif kard.suit == 'Clubs':
        clubs += 1
    elif kard.suit == 'Spades':
        spades += 1

print(hearts, diamonds,clubs, spades)
