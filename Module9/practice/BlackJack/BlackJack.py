import random


class Card:
    HEARTS = 'hearts'
    DIAMONDS = 'diamonds'
    CLUBS = 'clubs'
    SPADES = 'spades'
    types_symbols = {'hearts': '\u2661',
                     'diamonds': '\u2662',
                     'clubs': '\u2667',
                     'spades': '\u2664'}

    def __init__(self, value, type):
        self.value = value
        self.type = type

    def __repr__(self):
        return f'{self.value}{Card.types_symbols[self.type]}'

    def __gt__(self, other_card):
        if Deck.values.index(self.value) == Deck.values.index(other_card.value):
            return Deck.types.index(self.type) > Deck.types.index(other_card.type)
        else:
            return Deck.values.index(self.value) > Deck.values.index(other_card.value)

    def __eq__(self, other):
        return self.value == other.value and self.type == other.type


class Deck:
    types = ['spades', 'clubs', 'diamonds', 'hearts']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    points = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
              '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

    def __init__(self, num_cards=52):
        self.cards = []
        self.index = 0
        if num_cards == 36:
            self.values = Deck.values[4:]
        for t in Deck.types:
            for v in self.values:
                self.cards.append(Card(v, t))

    def show(self):
        string = f'deck[{len(self.cards)}]:'
        string += ', '.join([str(card) for card in self.cards])
        return string

    def __repr__(self):
        string = f'deck[{len(self.cards)}]:'
        string += ', '.join([str(card) for card in self.cards])
        return string

    def draw(self, x):
        cards = []
        for _ in range(x):
            cards.append(self.cards.pop(0))
        return cards

    def draw_card(self):
        return self.cards.pop(0)

    def shuffle(self):
        random.shuffle(self.cards)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        try:
            card = self.cards[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return card

    def __getitem__(self, index):
        return self.cards[index]

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
        sum_points += Deck.points[card.value]
    # Если сумма > 21, то перечитываем сумму, считая ТУЗ за 1(единицу)
    if sum_points > 21:
        sum_points = 0
        for card in cards:
            if card.value == "A":
                sum_points += 1
            else:
                sum_points += Deck.points[card.value]
    return sum_points


player_money = 100  # Деньги игрока
rate_value = 50  # Размер ставки

while player_money > 0:
    deck = Deck()
    deck.shuffle()
    # 0. Игрок делает ставку
    player_money -= rate_value
    # 1. В начале игры перемешиваем колоду
    # 2. Игроку выдаем две карты
    player_cards = deck.draw(2)
    # 3. Дилер берет одну карту
    dealer_cards = deck.draw(1)
    # 4. Отображаем в консоли карты игрока и дилера
    print(player_cards)
    print(dealer_cards)
    # 5. Проверяем нет ли у игрока блэкджека (21 очко)
    if sum_points(player_cards) == 21:
        # Выплачиваем выигрышь 3 и 2
        player_money += rate_value * 1.5
        print("Black Jack!!! Игрок победил")
    else:
        # Заканчиваем игру
    # Если нет блэкджека, то
        while True:  # Игрок добирает карты пока не скажет "достаточно" или не сделает перебор (>21)
            player_choice = input("еще(1)/достаточно(0): ")
            if player_choice == "1":
                player_cards.append(deck.draw_card())
                print(player_cards)
                # Раздаем еще одну карту
                # Если перебор (>21), заканчиваем добор
                if sum_points(player_cards) > 21:
                    print(f"Перебор: {sum_points(player_cards)} очков")
                    break
            if player_choice == "0":
                # Заканчиваем добирать карты
                break

        # Если у игрока не 21(блэкджек) и нет перебора, то
        if sum_points(player_cards) < 21:
            print("Диллер добирает карты")
            while sum_points(dealer_cards) < 17:
                dealer_cards.append(deck.draw_card())
                print(dealer_cards)
                # дилер начинает набирать карты.
                ...  # Смотри подробные правила добора дилера в задании

        # Выясняем кто набрал больше очков. Выплачиваем/забираем ставку
        if sum_points(player_cards) > 21:
            print("Дилер победил")
        elif sum_points(dealer_cards) > 21 or sum_points(dealer_cards) < sum_points(player_cards):
            print("Игрок победил")
            player_money += rate_value * 2
        elif sum_points(player_cards) < sum_points(dealer_cards):
            print("Дилер победил")
        else:
            print("Ничья")
            player_money += rate_value

    print (f'У игрока {round(player_money)} денег')
    print("*******************************")

print("Деньги закончились")
