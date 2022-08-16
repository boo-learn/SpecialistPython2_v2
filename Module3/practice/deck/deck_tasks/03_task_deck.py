from deck_total import Card, Deck

deck = Deck()
deck.shuffle()
prev_card = deck.draw(1)[0]
deck.shuffle()
curr_card = deck.draw(1)[0]
hand = [prev_card, curr_card]

while curr_card < prev_card and deck.cards:
    deck.shuffle()
    prev_card = curr_card
    curr_card = deck.draw(1)[0]
    hand.append(curr_card)

# for card in hand:
#     print(card, end = ' ')

print(' '.join(map(str, hand)))



# TODO: Создайте колоду из 52 карт. Перемешайте ее. Вытяните одну карту сверху.
#   Снова перемешайте колоду и вытяните еще одну. Если вторая карта меньше первой, повторите “перемешать + вытянуть”,
#   до тех пор, пока не вытяните карту больше предыдущей карты.
#   В качестве результата выведи все вытягиваемые карты в консоль.
