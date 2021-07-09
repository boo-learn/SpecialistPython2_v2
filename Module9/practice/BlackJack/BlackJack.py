import task_11_card_deck3 as cc


def sum_points(cards):
    """
    Напишите отдельную функцию для нахождения суммы очков всех карт в списке
    :param cards: список карт(рука игрока или диллера)
    :return: сумму очков
    """
    # Совет: храните кол-во очков за карту внутри класса Колоды(колода "знает", сколько дает очков каждая карта)

    #  Сначала считаем сумму карт, считая ТУЗ за 11-очков
    sum_points = 0
    for card in cards:
        if card.suit == "A" and sum_points > 21:
            sum_points += 1
            continue
        sum_points += cc.Deck.points[cc.Deck.values.index(card.suit)]

    return sum_points

class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.money = 0

def take_cards(deck, who, n:):
    cards = deck.draw(n)
    print(f"{who.name} takes ", end="")
    who.cards += cards
    for card in cards:
        print(card, end = " ")
    pass

def show_cards(who):
    print(f"{who.name}'s cards: ", end="")
    for card in who.cards:
        print(card, end=" ")

def game_loop():
    deck = cc.Deck()
    player = Player("Player")
    dealer = Player("Dealer")
    player.money = 100  # Деньги игрока
    rate_value = 10  # Размер ставки

    while True:
        # 0. Игрок делает ставку
        player.money -= rate_value
        # 1. В начале игры перемешиваем колоду
        deck.shuffle()
        # 2. Игроку выдаем две карты
        take_cards(deck, player, 2)
        # 3. Дилер берет одну карту
        take_cards(deck, dealer, 1)
        # 4. Отображаем в консоли карты игрока и дилера
        show_cards(player)
        show_cards(dealer)
        # 5. Проверяем нет ли у игрока блэкджека (21 очко)
        if sum_points(player.cards) == 21:
            # Выплачиваем выигрышь 3 и 2
            player.money += rate_value * 1.5
            print("Black Jack!!! Игрок победил")
            # Заканчиваем игру
            break
        # Если нет блэкджека, то
        while True:  # Игрок добирает карты пока не скажет "достаточно" или не сделает перебор (>21)
            player_choice = input("еще(1)/достаточно(0): ")
            if player_choice == "1":
                # Раздаем еще одну карту
                take_cards(deck, player, 1)
                # Если перебор (>21), заканчиваем добор
                if sum_points(player.cards) > 21:
                    print(f"Перебор: {sum_points(player.cards)} очков")
                    break
            if player_choice == "0":
                # Заканчиваем добирать карты
                break

        # Если у игрока не 21(блэкджек) и нет перебора, то
        if sum_points(player.cards) < 21:
            print("Диллер добирает карты")
            while True:  # дилер начинает набирать карты.
                if sum_points(dealer.cards) < 17:
                    take_cards(deck, dealer, 1)
                else:
                    break


        # Выясняем кто набрал больше очков. Выплачиваем/забираем ставку
        if sum_points(player_cards) > sum_points(dealer_cards):
            ...
        else:
            ...


def main():
    pass


if __name__ == "__main__":
    main()
