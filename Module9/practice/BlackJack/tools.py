def sum_points(cards):
    # Совет: храните кол-во очков за карту внутри класса Колоды(колода "знает", сколько дает очков каждая карта)

    #  Сначала считаем сумму карт, считая ТУЗ за 11-очков

    # Если сумма > 21, то перечитываем сумму, считая ТУЗ за 1(единицу)
    sum_points = 0

    for card in cards:
        if card.value == 'A':
            sum_points += 11
        else:
            sum_points += card.value

    if sum_points > 21:
        sum_points = 0

        for card in cards:
            if card.value == 'A':
                sum_points += 1
            else:
                sum_points += card.value

    return sum_points
