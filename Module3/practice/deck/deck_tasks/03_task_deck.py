from deck_total import Card, Deck


# TODO: Создайте колоду из 52 карт. Перемешайте ее. Вытяните одну карту сверху.
#   Снова перемешайте колоду и вытяните еще одну. Если вторая карта меньше первой, повторите “перемешать + вытянуть”,
#   до тех пор, пока не вытяните карту больше предыдущей карты.
#   В качестве результата выведи все вытягиваемые карты в консоль.
def more_than_first():
    cards = []
    deck = Deck()
    deck.shuffle()
    card1 = deck.draw(1)[0]
    cards.append(card1)
    deck.shuffle()
    card2 = deck.draw(1)[0]
    while card2 < card1:
        deck.shuffle()
        card2 = deck.draw(1)[0]
        cards.append(card2)
    return cards


for card in more_than_first():
    print(card)
