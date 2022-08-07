from classes import Deck
from tools import sum_points

player_money = 100  # Деньги игрока
rate_value = 10  # Размер ставки

while True:
    # 0. Игрок делает ставку
    in_play = True
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
    print('player_cards', player_cards, sum_points(player_cards))
    print('dealer_cards', dealer_cards, sum_points(dealer_cards))
    # 5. Проверяем нет ли у игрока блэкджека (21 очко)
    if sum_points(player_cards) == 21:
        # Выплачиваем выигрышь 3 и 2
        player_money += rate_value * 1.5
        print(f"Black Jack!!! Вы победили, ваш выигрыш {rate_value * 1.5}")
        # Заканчиваем игру
    # Если нет блэкджека, то
    while True:  # Игрок добирает карты пока не скажет "достаточно" или не сделает перебор (>21)
        player_choice = input("еще(1)/достаточно(0): ")
        if player_choice == "1":
            # Раздаем еще одну карту
            player_cards = player_cards + deck.draw(1)
            print(player_cards, sum_points(player_cards))
            # Если перебор (>21), заканчиваем добор
            if sum_points(player_cards) > 21:
                print(f"Перебор: {sum_points(player_cards)} очков")
                in_play = False
                break
        elif player_choice == "0":
            # Заканчиваем добирать карты
            break
        else:  # Обработка некорректного ввода
            print('Некорректный ввод, повторите')

    # Если у игрока не 21(блэкджек) и нет перебора, то
    if in_play:
        diller_points = sum_points(dealer_cards)
        if diller_points == 21:
            print(f"Диллер выиграл: {diller_points} очков")
            in_play = False
            continue
        print("Диллер добирает карты")
        while True:  # дилер начинает набирать карты.
            if diller_points < 17:
                dealer_cards = dealer_cards + deck.draw(1)
                diller_points = sum_points(dealer_cards)
                if diller_points > 21:
                    player_money += rate_value * 2
                    print('dealer_cards', dealer_cards, sum_points(dealer_cards))
                    print(f"Вы победили, ваш выигрыш {rate_value * 2}")
                    in_play = False
                    break
            else:
                print('dealer_cards', dealer_cards, sum_points(dealer_cards))
                break

    # Выясняем кто набрал больше очков. Выплачиваем/забираем ставку
    if in_play:
        if sum_points(player_cards) > sum_points(dealer_cards):
            print(f"Вы победили, ваш выигрыш {rate_value * 2}")
        else:
            print(f"Диллер выиграл")
    player_choice = input(f"Ваши деньги {player_money} еще игру(1)/достаточно(0): ")
    if player_choice == "0":
        break
