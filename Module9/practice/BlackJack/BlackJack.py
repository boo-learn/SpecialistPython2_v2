# Возьмите классы Deck и Card с GIST'а второго занятия и доработайте их
from card import Deck, Card

player_money = 100  # Деньги игрока
rate_value = 10  # Размер ставки
deck = Deck()


def sum_points(cards):
    sum_points = 0
    """
    Напишите отдельную функцию для нахождения суммы очков всех карт в списке
    :param cards: список карт(рука игрока или диллера)
    :return: сумму очков
    """
    # Совет: храните кол-во очков за карту внутри класса Колоды(колода "знает", сколько дает очков каждая карта)

    #  Сначала считаем сумму карт, считая ТУЗ за 11-очков
    for card in cards:
        sum_points += deck.points[card.value]
    # Если сумма > 21, то перечитываем сумму, считая ТУЗ за 1(единицу)
    if sum_points <= 21:
        return sum_points
    sum_points = 0
    for card in cards:
        if card.value == "A":
            sum_points += 1
        else:
            sum_points += deck.points[card.value]
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
    print(sum_points(player_cards))
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
            print(player_cards)
            print(sum_points(player_cards))
            # Проверяем нет ли у игрока блэкджека (21 очко)
            if sum_points(player_cards) == 21:
                # Выплачиваем выигрышь 3 и 2
                player_money += rate_value * 1.5
                print("Black Jack!!! Игрок победил")
                # Заканчиваем игру
                break
            # Если перебор (>21), заканчиваем добор
            if sum_points(player_cards) > 21:
                print(f"Перебор: {sum_points(player_cards)} очков")
                ...
                break
        if player_choice == "0":
            # Заканчиваем добирать карты
            break

    # Если у игрока не 21(блэкджек) и нет перебора, то
    if sum_points(player_cards) != 21 and sum_points(player_cards) < 21:
        print("Диллер добирает карты")
        while True:  # дилер начинает набирать карты.
            dealer_cards += deck.draw(1)
            print(dealer_cards)
            if sum_points(dealer_cards) == 21:
                print("Black Jack!!! Игрок проиграл!")
                # Заканчиваем игру
                break
                # Если перебор (>21), заканчиваем добор
            while sum_points(dealer_cards) <= 17:
                dealer_cards += deck.draw(1)
                print(dealer_cards)
                if sum_points(dealer_cards) > 21:
                    print(f"Перебор: {sum_points(dealer_cards)} очков")
                    player_money += rate_value * 2
                    break
            print(f"Дилер остановился")
            break

    # Выясняем кто набрал больше очков. Выплачиваем/забираем ставку
    print(f"Очки игрока: {sum_points(player_cards)}")
    print(f"Очки дилера: {sum_points(dealer_cards)}")
    if sum_points(player_cards) > sum_points(dealer_cards):
        player_money += rate_value * 2
        print("Игрок победил, деньги ", player_money)
        break
    else:
        print("Игрок проиграл, деньги ", player_money)
        break
