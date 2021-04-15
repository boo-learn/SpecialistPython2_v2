import random


class Card:
    HEARTS = "Hearts"
    DIAMONDS = "Diamonds"
    SPADES = "Spades"
    CLUBS = "Clubs"
    ICONS = {
        HEARTS: "♥",
        DIAMONDS: "♦",
        SPADES: "♠",
        CLUBS: "♣"
    }

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def to_str(self):
        return f"{self.value}{Card.ICONS[self.suit]}"

    def __repr__(self):
        return f"{self.value}{Card.ICONS[self.suit]}"

    def equal_suit(self, other_card):
        return self.suit == other_card.suit

    def more(self, other_card):
        if Deck.VALUES.index(self.value) == Deck.VALUES.index(other_card.value):
            return Deck.SUITS.index(self.suit) > Deck.SUITS.index(other_card.suit)
        else:
            return Deck.VALUES.index(self.value) > Deck.VALUES.index(other_card.value)

    def __gt__(self, other_card):
        if Deck.VALUES.index(self.value) == Deck.VALUES.index(other_card.value):
           return Deck.SUITS.index(self.suit) > Deck.SUITS.index(other_card.suit)
        else:
           return Deck.VALUES.index(self.value) > Deck.VALUES.index(other_card.value)

    def __lt__(self, other_card):
        if Deck.VALUES.index(self.value) == Deck.VALUES.index(other_card.value):
            return Deck.SUITS.index(self.suit) < Deck.SUITS.index(other_card.suit)
        else:
            return Deck.VALUES.index(self.value) < Deck.VALUES.index(other_card.value)

    def less(self, other_card):
        if Deck.VALUES.index(self.value) == Deck.VALUES.index(other_card.value):
            return Deck.SUITS.index(self.suit) < Deck.SUITS.index(other_card.suit)
        else:
            return Deck.VALUES.index(self.value) < Deck.VALUES.index(other_card.value)


class Deck:
    SUITS = [Card.SPADES, Card.CLUBS, Card.DIAMONDS, Card.HEARTS]
    VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    POINTS = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

    def __init__(self):
        self.card_index = 0
        self.cards = []
        for suit in Deck.SUITS:
            for value in Deck.VALUES:
                self.cards.append(Card(value, suit))

    def show(self):
        return f'deck[{len(self.cards)}]:' + ', '.join([card.to_str() for card in self.cards])

    def __repr__(self):
        return f'deck[{len(self.cards)}]:' + ', '.join([card.to_str() for card in self.cards])

    def draw(self, count):
        cards_in_hand = self.cards[:count]
        self.cards = self.cards[count:]
        return cards_in_hand

    def shuffle(self):
        random.shuffle(self.cards)

    def __len__(self):
        return len(self.cards)

    def __iter__(self):
        self.card_index = 0
        return self

    def __next__(self):
        card = self.cards[self.card_index]
        self.card_index += 1
        if self.card_index >= len(self.cards):
            raise StopIteration
        return card


deck = Deck()


player_money = 100  # Деньги игрока
rate_value = 10  # Размер ставки

deck = Deck()
deck.shuffle()


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
        sum_points += Deck.POINTS[card.value]
    # Если сумма > 21, то перечитываем сумму, считая ТУЗ за 1(единицу)
    if sum_points > 21:
        sum_points = 0
        for card in cards:
            if card.value == 'A':
                sum_points += 1
            else:
                sum_points += Deck.POINTS[card.value]
    return sum_points


while deck:
    # 0. Игрок делает ставку
    player_money -= rate_value
    # 1. В начале игры перемешиваем колоду
    # 2. Игроку выдаем две карты
    player_cards = deck.draw(2)
    # 3. Дилер берет одну карту
    dealer_cards = deck.draw(1)
    # 4. Отображаем в консоли карты игрока и дилера
    print(f'Карты игрока: {player_cards} = {sum_points(player_cards)}')
    print(f'Карты дилера: {dealer_cards} = {sum_points(dealer_cards)}')

    # 5. Проверяем нет ли у игрока блэкджека (21 очко)
    if sum_points(player_cards) == 21:
        # Выплачиваем выигрышь 3 и 2
        player_money += rate_value * 1.5
        print("Black Jack!!! Игрок победил")
        # Заканчиваем игру
    # Если нет блэкджека, то
    while True:  # Игрок добирает карты пока не скажет "достаточно" или не сделает перебор (>21)
        player_choice = input("еще(1)/достаточно(0): ")
        if player_choice == "1":
            # Раздаем еще одну карту
            player_cards += deck.draw(1)
            print(f'Карты игрока: {player_cards} = {sum_points(player_cards)}')
            # Если перебор (>21), заканчиваем добор
            if sum_points(player_cards) > 21:
                print(f"Перебор: {sum_points(player_cards)} очков")
                player_money -= rate_value
                break
        if player_choice == "0":
            # Заканчиваем добирать карты
            break

    # Если у игрока не 21(блэкджек) и нет перебора, то
    if sum_points(player_cards) < 21:
        print("Диллер добирает карты")
        while sum_points(dealer_cards) <= 17:  # дилер начинает набирать карты.
            dealer_cards += deck.draw(1)
            print(f'Карты дилера: {dealer_cards} = {sum_points(dealer_cards)}')
            if sum_points(dealer_cards) > 21:
                break
    print(f'Карты игрока: {player_cards} = {sum_points(player_cards)}')

    # Выясняем кто набрал больше очков. Выплачиваем/забираем ставку
    if (((sum_points(dealer_cards) > 21) and (sum_points(player_cards) <= 21)) or
        (sum_points(player_cards) > sum_points(dealer_cards)) and (sum_points(dealer_cards) <= 21)):
        player_money += 2 * rate_value
        print(f'Игрок победил, его счет теперь: {player_money}')
    elif (sum_points(player_cards) == sum_points(dealer_cards)) and sum_points(dealer_cards) <= 21:
        player_money += rate_value
        print(f'Ничья, счет игрока: {player_money}')
    else:
        print(f'Игрок проиграл, его счет теперь: {player_money}')


    print('*' * 20)
