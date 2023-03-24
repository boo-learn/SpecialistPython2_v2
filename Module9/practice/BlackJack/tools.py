from classes import Card

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

    sum_points = 0

    for card in cards:
        for key, value in card_points.items():
            if card.value == key:
                sum_points += value

    # Если сумма > 21, то перечитываем сумму, считая ТУЗ за 1(единицу)

    if sum_points > 21:
        for card in cards:
            if card.value == 'A':
                sum_points -= 10

    return sum_points


card1 = Card('3', Card.CLUBS)
card2 = Card('A', Card.HEARTS)
card3 = Card('A', Card.SPADES)

cards = [card1, card2, card3]

print(sum_points(cards))
