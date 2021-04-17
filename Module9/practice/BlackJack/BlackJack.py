# Возьмите классы Deck и Card с GIST'а второго занятия и доработайте их
from classes import Deck

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
    def sum_values(Ace_value=11):
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '10', '10', '10', str(Ace_value)]
        current_values = []
        for card in cards:
            current_values.append(int(values[Deck.values.index(card.value)]))
        return sum(current_values)

    sum_points = sum_values()
    # Если сумма > 21, то перечитываем сумму, считая ТУЗ за 1(единицу)
    if sum_points > 21:
        sum_values(1)
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
    print(player_cards)
    print(dealer_cards)
    # 5. Проверяем нет ли у игрока блэкджека (21 очко)
    if sum_points(player_cards) == 21:
        # Выплачиваем выигрыш 3 и 2
        player_money += rate_value * 1.5
        print("Black Jack!!! Игрок победил")
        # Заканчиваем игру
    # Если нет блэкджека, то
    while True:  # Игрок добирает карты пока не скажет "достаточно" или не сделает перебор (>21)
        player_choice = input("еще(1)/достаточно(0): ")
        if player_choice == "1":
            # Раздаем еще одну карту
            player_cards.append(*deck.draw(1))
            print(player_cards, dealer_cards, sum_points(player_cards), sum_points(dealer_cards), sep='\n')
            # Если перебор (>21), заканчиваем добор
            if sum_points(player_cards) > 21:
                print(f"Перебор: {sum_points(player_cards)} очков")
                rate_value = 0
                break
        if player_choice == "0":
            # Заканчиваем добирать карты
            break

    # Если у игрока не 21(блэкджек) и нет перебора, то
    if sum_points(player_cards) < 21:
        print("Диллер добирает карты")
        while True:  # дилер начинает набирать карты.
            while sum_points(dealer_cards) < 17:
                dealer_cards.append(*deck.draw(1))
                print(player_cards, dealer_cards, sum_points(player_cards), sum_points(dealer_cards), sep='\n')
                break
            else:
                break
            ...  # Смотри подробные правила добора дилера в задании

    # Выясняем кто набрал больше очков. Выплачиваем/забираем ставку
    if rate_value > 0 and sum_points(player_cards) > sum_points(dealer_cards):
        player_money += rate_value * 2
        print('Игрок победил')
    elif rate_value > 0 and sum_points(player_cards) == sum_points(dealer_cards):
        player_money += rate_value
        print('Ничья')
    else:
        rate_value = 0
        print('Игрок проиграл')
    print(f'{player_money=}')
    print('Новый раунд')
    print('*' * 40)
