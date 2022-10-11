from deck_total import Card, Deck

# TODO: Создайте колоду из 52 карт. Перемешайте ее. Вытяните 10 карт сверху
#   и посчитайте карт какой/каких мастей среди вытянутых карт оказалось больше всего?
deck = Deck()
deck.shuffle()
hand = deck.draw(10)
suits = []
for card in hand:
    suits.append(card.suit)
print(suits)
hearts = suits.count('Hearts')
diamonds = suits.count('Diamonds')
clubs = suits.count('Clubs')
spades = suits.count('Spades')
if diamonds > hearts and clubs and spades:
    print('Больше всего бубей')
if hearts > diamonds and clubs and spades:
    print('Больше всего червей')
if clubs > hearts and diamonds and spades:
    print('Больше всего крестей')
if spades > hearts and clubs and diamonds:
    print('Больше всего пик')
