from task_11_card_deck3 import Deck, Card


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
        sum_points += Deck.points[Deck.values.index(card.value)]
    if sum_points <= 21:
        return sum_points
    sum_points = 0
    for card in cards:
        if card.value != "A":
            sum_points += Deck.points[Deck.values.index(card.value)]
        else:
            sum_points += 1
    return sum_points


class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.money = 0


def take_cards(deck, who, n):
    cards = deck.draw(n)
    print(f"{who.name} takes ", end="")
    who.cards += cards
    for card in cards:
        print(card, end = " ")
    print()
    pass


def show_cards(who):
    print(f"{who.name}'s cards: ", end="")
    for card in who.cards:
        print(card, end=" ")
    print(f"for {sum_points(who.cards)} points.")


def game_loop():
    YES = "y"
    NO = "n"
    deck = Deck()
    player = Player("Player")
    dealer = Player("Dealer")
    player.money = 100  # Деньги игрока
    rate_value = 10  # Размер ставки

    while True:
        print("*"*40)
        print(f"{player.name} has {player.money}")
        exceed = False
        # 0. Игрок делает ставку
        if player.money < rate_value:
            print("Sorry, you are broke!")
            break
        print("New round!")
        deck = Deck()
        player.cards = []
        dealer.cards = []
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
            player_choice = input("Another card? (y/n): ")
            if player_choice == YES.lower():
                # Раздаем еще одну карту
                take_cards(deck, player, 1)
                show_cards(player)
                # Если перебор (>21), заканчиваем добор
                if sum_points(player.cards) > 21:
                    print(f"Перебор: {sum_points(player.cards)} очков")
                    exceed = True
                    break
            else:
                # Заканчиваем добирать карты
                break

        if sum_points(player.cards) == 21:
            player.money += rate_value * 1.5
            print(f"{player.name} wins and receives {rate_value * 2}")
        # Если у игрока не 21(блэкджек) и нет перебора, то
        elif sum_points(player.cards) < 21:
            print("Диллер добирает карты")
            while True:  # дилер начинает набирать карты.
                if sum_points(dealer.cards) < 17:
                    take_cards(deck, dealer, 1)
                else:
                    break
            show_cards(dealer)
            # Выясняем кто набрал больше очков. Выплачиваем/забираем ставку
            if sum_points(player.cards) > sum_points(dealer.cards) or sum_points(dealer.cards) > 21:
                player.money += rate_value * 2
                print(f"{player.name} wins and receives {rate_value * 2}")
            elif sum_points(player.cards) < sum_points(dealer.cards):
                print(f"{dealer.name} wins.")
            else:
                print("Draw.")
        else:
            print(f"{dealer.name} wins.")
        answer = input("Play again?(y,n):")
        if answer.lower() != YES:
                print("Bye!")
                break


def main():
    game_loop()


if __name__ == "__main__":
    main()
