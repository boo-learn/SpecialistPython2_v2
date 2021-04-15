# Возьмите классы Deck и Card с GIST'а второго занятия и доработайте их
from lass_Deck_vFinal import Deck, Card

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
    def calculate_values(one=False):
        if not one:
            values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '10', '10', '10', '11']
        else:
            values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '10', '10', '10', '1']
        current_values = []
        for card in cards:
            current_values.append(int(values[Deck.VALUES.index(card.value)]))

        return sum(current_values)


    sum_points = calculate_values()
    # Если сумма > 21, то перечитываем сумму, считая ТУЗ за 1(единицу)
    if sum_points > 21:
        sum_points = calculate_values(True)

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
    print('Карты игрока:', player_cards)
    print('Карты дилера:',dealer_cards)
    # 5. Проверяем нет ли у игрока блэкджека (21 очко)
    if sum_points(player_cards) == 21:
        # Выплачиваем выигрышь 3 и 2
        player_money += rate_value * 1.5
        print("Black Jack!!! Игрок победил")
        # Заканчиваем игру
        break
    # Если нет блэкджека, то
    while True:  # Игрок добирает карты пока не скажет "достаточно" или не сделает перебор (>21)
        player_choice = input("еще(1)/достаточно(0): ")
        if player_choice == "1":
            # Раздаем еще одну карту
            player_cards += deck.draw(1)
            # Если перебор (>21), заканчиваем добор
            if sum_points(player_cards) > 21:
                print(f"Перебор: {sum_points(player_cards)} очков")
                print('Дилер говорит: \"Много\"')
                player_money -= rate_value
                break
        if player_choice == "0":
            # Заканчиваем добирать карты
            break

    # Если у игрока не 21(блэкджек) и нет перебора, то
    if sum_points(player_cards) < 21:
        print("Диллер добирает карты")
        while True:  # дилер начинает набирать карты.
            dealer_cards += deck.draw(1)
            count_card = 0
            if count_card < 2 and sum_points(dealer_cards) == 21:
                # Забираем ставку
                player_money -= rate_value
                print("Black Jack!!! Дилер победил")
                # Заканчиваем игру
                count_card += 1
                break
            
            if sum_points(dealer_cards) < 21:
                
            ...  # Смотри подробные правила добора дилера в задании

    # Выясняем кто набрал больше очков. Выплачиваем/забираем ставку
    if sum_points(player_cards) > sum_points(dealer_cards):
        ...
    else:
        ...
