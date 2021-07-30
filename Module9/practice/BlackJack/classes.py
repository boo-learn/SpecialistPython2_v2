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

# cards=[Card("K", Card.HEARTS),
#        Card("A",Card.HEARTS),
#        Card("A",Card.HEARTS)]
# print (sum_points(cards))

while True:
    # 0. Игрок делает ставку
    player_money -= rate_value
    # 1. В начале игры перемешиваем колоду
    deck.shuffle()
    # 2. Игроку выдаем две карты
    
    player_cards=deck.draw(2)
    
    # 3. Дилер берет одну карту
    dealer_cards = deck.draw(1)
    # # 4. Отображаем в консоли карты игрока и дилера
    # for card in dealer_cards:
    # print(f"Карты игрока: {player_cards}")
    # for card in dealer_cards:
    #     print(card,end="")
    # 5. Проверяем нет ли у игрока блэкджека (21 очко)
    # if sum_points(player_cards) == 21:
    #     # Выплачиваем выигрышь 3 и 2
    #     player_money += rate_value * 1.5
    #     print("Black Jack!!! Игрок победил")
    #     # Заканчиваем игру
    # # Если нет блэкджека, то
    # while True:  # Игрок добирает карты пока не скажет "достаточно" или не сделает перебор (>21)
    #     player_choice = input("еще(1)/достаточно(0): ")
    #     if player_choice == "1":
    #         # Раздаем еще одну карту
    #         # Если перебор (>21), заканчиваем добор
    #         if sum_points(player_cards) > 21:
    #             print(f"Перебор: {sum_points(player_cards)} очков")
    #             ...
    #             break
    #     if player_choice == "0":
    #         # Заканчиваем добирать карты
    #         break
    #
    # # Если у игрока не 21(блэкджек) и нет перебора, то
    # if ...:
    #     print("Диллер добирает карты")
    #     while True:  # дилер начинает набирать карты.
    #         ...  # Смотри подробные правила добора дилера в задании
    #
    # # Выясняем кто набрал больше очков. Выплачиваем/забираем ставку
    # if sum_points(player_cards) > sum_points(dealer_cards):
    #     ...
    # else:
    #     ...
