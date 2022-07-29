def sum_points(cards):
    """
    Напишите отдельную функцию для нахождения суммы очков всех карт в списке
    :param cards: список карт(рука игрока или диллера)
    :return: сумму очков
    """

    def calc_points(points, cards):
        sum_points = 0
        have_ace = False
        for card in cards:
            sum_points += points[card.value]
            if card.value == "A":
                have_ace = True
        return sum_points, have_ace

    points = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10,
              "K": 10, "A": 11}
    sum_points, have_ace = calc_points(points, cards)

    if sum_points > 21 and have_ace:
        points["A"] = 1
        sum_points = calc_points(points, cards)
    return sum_points
