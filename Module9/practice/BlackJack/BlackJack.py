# Возьмите классы Deck и Card с GIST'а второго занятия и доработайте их
from class_Deck_final import Deck, Card

player_money = 100  # Деньги игрока
rate_value = 10  # Размер ставки

deck = Deck()

def sum_points(cards):
    """
    Напишите отдельную функцию для нахождения суммы очков всех карт в списке
    :param cards: список карт(рука игрока или диллера)
    :return: сумму очков
    """
    # Совет: храните кол-во очков за карту внутри класса Колоды (колода "знает", сколько дает очков каждая карта)

    #  Сначала считаем сумму карт, считая ТУЗ за 11-очков

    sum_points = 0
    for card in cards:
        sum_points += Deck.card_point[Deck.values.index(card.value)]

    if sum_points <= 21:
        return sum_points

    # Если сумма > 21, то перечитываем сумму, считая ТУЗ за 1(единицу)
    if sum_points > 21:
        sum_points = 0
        for card in cards:
            sum_points += Deck.card_pointA[Deck.values.index(card.value)]

    return sum_points

while True:
    # 0. Игрок делает ставку
    player_money -= rate_value
    # 1. В начале игры перемешиваем колоду
    deck.shuffle()
    # 2. Игроку выдаем две карты
    player_cards = deck.draw(2)
    # 3. Дилер берет одну карту
    dealer_cards = deck.draw(1)
    # 4. Отображаем в консоли карты игрока и дилера
    print('У игрока:', player_cards)
    print('У дилера:', dealer_cards)
    # 5. Проверяем нет ли у игрока блэкджека (21 очко)
    if sum_points(player_cards) == 21:
        # Выплачиваем выигрыш 3 к 2
        player_money += rate_value * 1.5
        print("Black Jack!!! Игрок победил")
        # Заканчиваем игру
        break
    # Если нет блэкджека, то
    print('У игрока', sum_points(player_cards), ' очков')
    while True:  # Игрок добирает карты пока не скажет "достаточно" или не сделает перебор (>21)
        player_choice = input("еще(1)/достаточно(0): ")
        if player_choice == "1":
            # Раздаем еще одну карту
            player_cards.extend(deck.draw(1))
            print('У игрока:', player_cards, 'Очков', sum_points(player_cards))
            # Если перебор (>21), заканчиваем добор
            if sum_points(player_cards) > 21:
                print(f"Перебор: {sum_points(player_cards)} очков")
                ...
                break
        if player_choice == "0":
            # Заканчиваем добирать карты
            break

    # Если у игрока не 21(блэкджек) и нет перебора, то
    if sum_points(player_cards) < 21:
        print("Диллер добирает карты")
        while True:  # дилер начинает набирать карты.
            dealer_cards.extend(deck.draw(1))
            print('У дилера:', dealer_cards, 'Очков', sum_points(dealer_cards))
            # Смотри подробные правила добора дилера в задании
            if sum_points(dealer_cards) >= 17:
                break

    # Выясняем кто набрал больше очков. Выплачиваем/забираем ставку
    if sum_points(player_cards) > sum_points(dealer_cards):
        print('Выиграл игрок')
        player_money += rate_value
    elif sum_points(player_cards) == sum_points(dealer_cards):
        print("ничья")
    else:
        print('Игрок проиграл')
        player_money -= rate_value

    if player_money <= 0:
        print('Игрок банкрот')
        break
    print("*" * 20)
