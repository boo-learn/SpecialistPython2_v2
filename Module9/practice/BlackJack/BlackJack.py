# Возьмите классы Deck и Card с GIST'а второго занятия и доработайте их
from Deck import Deck, Card

player_money = 100  # Деньги игрока
rate_value = 10  # Размер ставки

deck = Deck()


def sum_points(cards):
    """
    Напишите отдельную функцию для нахождения суммы очков всех карт в списке
    :param cards: список карт(рука игрока или диллера)
    :return: сумму очков
    """
    # Совет: храните кол-во очков за карту внутри класса Колоды(колода "знает", сколько дает очков каждая карта)
    #  Сначала считаем сумму карт, считая ТУЗ за 11-очков
    sum_points=0
    A_count=0
    for card in cards:
        if card.value=="A":
            A_count+=1
        for i in range(len(Deck.values)):
            if card.value==Deck.values[i]:
                sum_points+=int(Deck.points[i])

    # Если сумма > 21, то перечитываем сумму, считая ТУЗ за 1(единицу)
    if sum_points > 21 and A_count>0:
           sum_points=sum_points-(11*A_count)+A_count


    return sum_points
