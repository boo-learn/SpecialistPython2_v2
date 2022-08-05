def sum_points(cards):
    """
    Напишите отдельную функцию для нахождения суммы очков всех карт в списке
    :param cards: список карт(рука игрока или диллера)
    :return: сумму очков
    """
    # Совет: храните кол-во очков за карту внутри класса Колоды(колода "знает", сколько дает очков каждая карта)
    # Данный список находится в классе Deck
    # card_values = {"J": 10, "Q": 10, "K": 10, "A": 11}

    #  Сначала считаем сумму карт, считая ТУЗ за 11-очков
    num_aces = 0
    sum_points = 0
    for card in cards:
        card_value = Deck.card_values.get(card.value) or int(card.value)
        if card.value == "A":
            num_aces += 1
        sum_points += card_value

    # Если сумма > 21, то перечитываем сумму, считая ТУЗ за 1(единицу)
    if sum_points > 21 and num_aces > 0:
        sum_points = sum_points - num_aces * Deck.card_values.get("A") + num_aces

    return sum_points
