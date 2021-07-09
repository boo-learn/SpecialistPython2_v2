from card import Deck, Card

player_money = 100  # Деньги игрока
rate_value = 10  # Размер ставки

deck = Deck()


def sum_points(cards):
    summ_points = 0
    for card in cards:
        for card_key in Deck.card_points.keys():
            if card.value == card_key:
                summ_points += Deck.card_points[card.value]
    if summ_points > 21:
        summ_points = 0
        for card in cards:
            for card_key in Deck.card_points.keys():
                if card.value == card_key:
                    if card.value == 'A':
                        summ_points += 1
                    else:
                            summ_points += Deck.card_points[card.value]
    return summ_points

cards = [
    Card("9", Card.HEARTS),
    Card("A", Card.DIAMONDS),
    # Card("2", Card.DIAMONDS),
    # Card("A", Card.DIAMONDS),

]
print(sum_points(cards))

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
    print(f'Карты игрока: {player_cards} /n карты Дилера {dealer_cards}')
    # 5. Проверяем нет ли у игрока блэкджека (21 очко)
    if sum_points(player_cards) == 21:
        player_money += rate_value * 1.5
        print("Black Jack!!! Игрок победил")
        exit(0)    
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
        if player_choice == "0":
            # Заканчиваем добирать карты
            break

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
