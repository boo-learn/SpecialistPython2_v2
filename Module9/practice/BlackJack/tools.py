from classes import Card, Deck

def sum_points(cards):
    """
    Напишите отдельную функцию для нахождения суммы очков всех карт в списке
    :param cards: список карт(рука игрока или диллера)
    :return: сумму очков
    """
    # Совет: храните кол-во очков за карту внутри класса Колоды(колода "знает", сколько дает очков каждая карта)

    #  Сначала считаем сумму карт, считая ТУЗ за 11-очков
    sum_points = 0
    for card in cards:
        sum_points += Deck.card_points[card.value]
    # Если сумма > 21, то перечитываем сумму, считая ТУЗ за 1(единицу)
    if sum_points > 21:
        sum_points = 0
        for card in cards:
            if card.value == 'A':
                sum_points += 1
            else:
                sum_points += Deck.card_points[card.value]

    return sum_points

cards = [Card('Q', Card.CLUBS), Card('A', Card.HEARTS), Card('10', Card.SPADES)]
print(sum_points(cards))
