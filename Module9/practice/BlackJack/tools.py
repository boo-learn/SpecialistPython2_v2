def sum_points(cards):
    # Совет: храните кол-во очков за карту внутри класса Колоды(колода "знает", сколько дает очков каждая карта)

    #  Сначала считаем сумму карт, считая ТУЗ за 11-очков
    sum_points = 0
    for card in cards:
        sum_points += card.points()
    # Если сумма > 21, то перечитываем сумму, считая ТУЗ за 1(единицу)

    if sum_points > 21:
        sum_points = 0
        for card in cards:
            if card.points() == 11:
                sum_points += 1
                continue
            sum_points += card.points()

    return sum_points
