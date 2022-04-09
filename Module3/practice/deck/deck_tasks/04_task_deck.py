from deck_total import Card, Deck


# TODO: Создайте две колоды, в каждой должно быть 36 карт(старшинство карт начинается с 6-ки). Перемешайте их.
#   Вытягивайте карты парами - одну из первой колоды, вторую из второй.
#   Если карта из первой колоды окажется больше(старше), то записываем 1:0(условно начисляем победное очко первой колоде),
#   если карты одинаковые, то не учитываем очко никуда.
#   Выведите итоговый счет, сравнив попарно все карты в колодах.
def two_decks():
    Deck.values = Deck.values[4:]
    deck1 = Deck()
    deck2 = Deck()
    deck1.shuffle()
    deck2.shuffle()
    count_deck1, count_deck2 = 0, 0
    for card1, card2 in zip(deck1, deck2):
        if card1 > card2:
            count_deck1 += 1
        elif card1 < card2:
            count_deck2 += 1
    return f'{count_deck1} : {count_deck2}'


print(two_decks())
