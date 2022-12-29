from Classes import Deck, Card
from Tools import sum_points

player_money = 50  # Деньги игрока
rate_value = 10  # Размер ставки
round = 1 # Раунд игры

while True:
    print (f"***** Раунд {round}, текущий баланс игрока {player_money} *****")
    # 0. Игрок делает ставку
    player_money -= rate_value
    if player_money < 0:  # Если денег на новую ставку недостаточно, то игра заканчивается
        print("У вас закончились деньги. Игра окончена!")
        break
    print(f"Игрок делает ставку: {rate_value}")
    # 1. В начале игры создаем колоду и перемешиваем ее
    deck = Deck()
    deck.shuffle()
    # 2. Игроку выдаем две карты
    player_cards = deck.draw(2)
    # 3. Дилер берет одну карту
    dealer_cards = deck.draw(1)
    # 4. Отображаем в консоли карты игрока и дилера
    print(f"Player cards {' '.join(str(card) for card in player_cards)}")
    print(f"Dealer cards {' '.join(str(card) for card in dealer_cards)}")
    # 5. Проверяем нет ли у игрока блэкджека (21 очко)
    if sum_points(player_cards) == 21:
        # Выплачиваем выигрыш 3 и 2
        player_money += rate_value * 1.5
        print(f"Black Jack!!! Вы победили, ваш выигрыш {rate_value * 1.5}")
        # Заканчиваем игру
    # Если нет блэкджека, то
    while True:  # Игрок добирает карты пока не скажет "достаточно" или не сделает перебор (>21)
        player_choice = input("еще(1)/достаточно(0): ")
        if player_choice == "1":
            # Раздаем еще одну карту
            # Если перебор (>21), заканчиваем добор
            player_cards.append(deck.draw(1)[0])
            if sum_points(player_cards) > 21:
                print(f"Перебор: {sum_points(player_cards)} очков")
                print (f"Заканчиваем добор")
                break
        elif player_choice == "0":
            # Заканчиваем добирать карты
            break
        else:  # Обработка некорректного ввода
            print("Введено некорректное значение (нужно ввести 0 или 1) повторите ввод")

    # Если у игрока не 21(блэкджек) и нет перебора, то
    if sum_points(player_cards) != 21:
        print("Дилер добирает карты")
        while True:  # дилер начинает набирать карты.
            # Смотри подробные правила добора дилера в задании
            if sum_points(dealer_cards) > 17:
                break
            else:
                dealer_cards.append (deck.draw(1)[0])

    # Выясняем кто набрал больше очков. Выплачиваем/забираем ставку
    if sum_points(player_cards) > sum_points(dealer_cards):
        player_money += rate_value * 2
        print(f"Black Jack!!! Вы победили, ваш выигрыш {rate_value * 2}")
    elif sum_points(player_cards) > sum_points(dealer_cards):
        player_money += rate_value
        print(f"Боевая ничья! Ставка {rate_value} не сыграна")
    else:
        print(f"Sorry!!! Вы проиграли, ваш проигрыш {rate_value}")

    print (f"Баланс игрока после очередного раунда {player_money}")

    round += 1
