from classes import  Card, Deck

def sum_points(cards):
    """
    Напишите отдельную функцию для нахождения суммы очков всех карт в списке
    :param cards: список карт(рука игрока или диллера)
    :return: сумму очков
    """
    # Совет: храните кол-во очков за карту внутри класса Колоды(колода "знает", сколько дает очков каждая карта)
    card_points = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
                   'J': 10, 'Q': 10, 'K': 10, 'A': 11}
    #  Сначала считаем сумму карт, считая ТУЗ за 11-очков
    sum_points = card_points[cards[0].value]+card_points[cards[1].value]+card_points[cards[2].value]
    # Если сумма > 21, то перечитываем сумму, считая ТУЗ за 1(единицу)

    if sum_points > 21:
        if cards[0].value == 'A':
            sum_points -= 10
        if cards[1].value == 'A':
            sum_points -= 10
        if cards[2].value == 'A':
            sum_points -= 10

    return sum_points


card1 = Card('10',Card.HEARTS)
card2 = Card('2',Card.HEARTS)
card3 = Card('A',Card.HEARTS)

hands = [card1,card2,card3]
print(sum_points(hands))

