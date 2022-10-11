from deck_total import Card, Deck

# TODO: Создайте колоду из 52 карт. Перемешайте ее. Вытяните одну карту сверху.
#   Снова перемешайте колоду и вытяните еще одну. Если вторая карта меньше первой, повторите “перемешать + вытянуть”,
#   до тех пор, пока не вытяните карту больше предыдущей карты.
#   В качестве результата выведи все вытягиваемые карты в консоль.

deck = Deck()
cards = []
while deck:
    deck.shuffle()
    card1 = deck.draw(1)
    deck.shuffle()
    card2 = deck.draw(1)
    if card1 < card2:
        cards.append(card1)
        cards.append(card2)
        break
    else:
        cards.append(card1)
        cards.append(card2)
print(cards)
