# Возьмите классы Deck и Card с GIST'а второго занятия и доработайте их
from deck import Deck, Card

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
    cards_weights = [card.weight for card in cards]
    sum_points = sum(cards_weights)
    # Если сумма > 21, то перечитываем сумму, считая ТУЗ за 1(единицу)
    if sum_points > 21:
        while 11 in cards_weights:
            cards_weights.remove(11)
            cards_weights.append(1)
        sum_points = sum(cards_weights)

    return sum_points

def greetings():
    print('*' * 20)
    print('* Игра начинается! *')
    rate_value = int(input('* Введите ставку: $ '))
    print(f'* Ваша ставка {rate_value} $ *')
    print('*' * 20)
    return rate_value

def whos_cards():
    print(f'Карты дилера: {[str(card) for card in dealer_cards]}. Очки дилера {sum_points(dealer_cards)}')
    print(f'Ваши карты: {[str(card) for card in player_cards]}. Ваши очки {sum_points(player_cards)}')

while True:
    rate_value = greetings()
    # 0. Игрок делает ставку
    player_money -= rate_value
    # 1. В начале игры перемешиваем колоду
    deck.shuffle()
    # 2. Игроку выдаем две карты
    player_cards = deck.draw(2)
    # 3. Дилер берет одну карту
    dealer_cards = deck.draw(1)
    # 4. Отображаем в консоли карты игрока и дилера
    whos_cards()
    # 5. Проверяем нет ли у игрока блэкджека (21 очко)
    if sum_points(player_cards) == 21:
        # Выплачиваем выигрышь 3 и 2
        player_money += rate_value * 1.5
        print("Black Jack!!! Игрок победил")
        print(f'Ваш выигрыш {rate_value * 1.5} $')
        # Заканчиваем игру
    # Если нет блэкджека, то
    while True:  # Игрок добирает карты пока не скажет "достаточно" или не сделает перебор (>21)
        player_choice = input("еще(1)/достаточно(0): ")
        if player_choice == "1":
            # Раздаем еще одну карту
            player_cards += deck.draw(1)
            # Если перебор (>21), заканчиваем добор
            print(f'Ваши карты: {[str(card) for card in player_cards]}. Ваши очки {sum_points(player_cards)}')
            if sum_points(player_cards) == 21:
                # Выплачиваем выигрышь 3 и 2
                player_money += rate_value * 1.5
                print("Black Jack!!! Игрок победил")
                print(f'Ваш выигрыш {rate_value * 1.5} $')
                break
            if sum_points(player_cards) > 21:
                print(f"Перебор: {sum_points(player_cards)} очков")
                break
        if player_choice == "0":
            # Заканчиваем добирать карты
            break

    # Если у игрока не 21(блэкджек) и нет перебора, то
    if not sum_points(player_cards) >= 21:
        print("Диллер добирает карты")
        while sum_points(dealer_cards) < 17:  # дилер начинает набирать карты.
            dealer_cards += deck.draw(1)  # Смотри подробные правила добора дилера в задании

    # Выясняем кто набрал больше очков. Выплачиваем/забираем ставку
    if sum_points(player_cards) == 21:
        continue
    elif sum_points(dealer_cards) < sum_points(player_cards) < 21 and sum_points(dealer_cards) != sum_points(player_cards):
        whos_cards()
        print(f'Вы выиграли у казино. Ваш выигрыш {rate_value * 2} $')
        player_money += rate_value * 2
    elif sum_points(dealer_cards) == sum_points(player_cards):
        print(f'Ничья! Повторим!')
    else:
        whos_cards()
        print(f'Вы проиграли {rate_value} $')
        player_money -= rate_value
