from classes import Deck, Card
from tools import sum_points

player_money = 100  # Деньги игрока
rate_value = 10  # Размер ставки

while True:
    # 0. Игрок делает ставку
    player_money -= rate_value
    if player_money < 0:  # Если денег на новую ставку недостаточно, то игра заканчивается
        print("У вас закончились деньги. Игра окончена!")
        break
    print(f"Игрок делает ставку: {rate_value}")
    # 1. В начале игры создаем колоду и перемешиваем ее
    deck = Deck()
    ...
    # 2. Игроку выдаем две карты
    player_cards = ...
    # 3. Дилер берет одну карту
    dealer_cards = ...
    # 4. Отображаем в консоли карты игрока и дилера
    ...
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
            # Если перебор (>21), заканчиваем добор
            if sum_points(player_cards) > 21:
                print(f"Перебор: {sum_points(player_cards)} очков")
                ...
                break
        elif player_choice == "0":
            # Заканчиваем добирать карты
            break
        else:  # Обработка некорректного ввода
            print(...)

    # Если у игрока не 21(блэкджек) и нет перебора, то
    if ...:
        print("Диллер добирает карты")
        while True:  # дилер начинает набирать карты.
            ...  # Смотри подробные правила добора дилера в задании

    # Выясняем кто набрал больше очков. Выплачиваем/забираем ставку
    if sum_points(player_cards) > sum_points(dealer_cards):
        ...
    else:
        ...
