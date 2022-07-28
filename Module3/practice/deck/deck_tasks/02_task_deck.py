from deck_total import Card, Deck

# TODO: Создайте колоду из 52 карт. Перемешайте ее. Вытяните 10 карт сверху
#   и посчитайте карт какой/каких мастей среди вытянутых карт оказалось больше всего?

deck1 = Deck()

deck1.shuffle()

deck1 = deck1.cards[:10]

hearts = 0
diamonds = 0
clubs = 0
spades = 0

for i in range(len(deck1)):
    if deck1[i].suit == 'Hearts':
        hearts+=1
        
for i in range(len(deck1)):
    if deck1[i].suit == 'Diamonds':
        diamonds+=1
        
for i in range(len(deck1)):
    if deck1[i].suit == 'Clubs':
        clubs+=1
        
for i in range(len(deck1)):
    if deck1[i].suit == 'Spades':
        spades+=1
suit_str = [hearts , diamonds , clubs , spades]

max1 = suit_str.pop(suit_str.index(max(suit_str))), suit_str.pop(suit_str.index(max(suit_str)))

print(max1)
