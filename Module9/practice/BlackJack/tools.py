def sum_points(cards):
    """
    Напишите отдельную функцию для нахождения суммы очков всех карт в списке
    :param cards: список карт(рука игрока или диллера)
    :return: сумму очков
    """
    # Совет: храните кол-во очков за карту внутри класса Колоды(колода "знает", сколько дает очков каждая карта)
    card_points ={
        '2' : 2 , '3' : 3, '4' : 4 , '5' : 5, '6' : 6, '7' : 7, '8' : 8 , '9': 9 , '10' : 10, 'J' : 10, 'Q' : 10, 'K' : 10, 'A' : 10
        }
    
    #  Сначала считаем сумму карт, считая ТУЗ за 11-очков
    sum_points = 0
    for card in cards:
        sum_points += card_point[card]
    # Если сумма > 21, то перечитываем сумму, считая ТУЗ за 1(единицу)
    if sum_points > 21:
        sum_points = 0
        for card in cards:
            if card == 'A':
                sum_points += 1
            else:
              for card in cards:
                  sum_points += card_point[card]  

    return sum_points
