import random


class Card:
    """Игральная карта"""
    HEARTS = 'Hearts'
    DIAMONDS = 'Diamonds'
    SPADES = 'Spades'
    CLUBS = 'Clubs'
    SUITS = [CLUBS, SPADES, DIAMONDS, HEARTS]
    ICONS = ['♠', '♣', '♦', '♥']
    VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return self.to_str()

    def __str__(self):
        return self.to_str()

    def __gt__(self, other):    # >
        return self.more(other)

    def __ge__(self, other):    # >=
        return self.more(other) or self.equal(other)

    def __lt__(self, other):    # <
        return self.less(other)

    def __le__(self, other):    # <=
        return self.less(other) or self.equal(other)

    def __eq__(self, other):    # ==
        return self.equal(other)

    def __ne__(self, other):    # !=
        return not self.equal(other)

    def to_str(self):
        """Строковое представление объекта класса карты"""
        return f'{self.ICONS[self.SUITS.index(self.suit)]}{self.value}'

    def equal(self, other_card) -> bool:
        """Проверяет не одинаковые-ли карты"""
        return self.equal_suit(other_card) and self.equal_value(other_card)

    def equal_suit(self, other_card) -> bool:
        """Проверяет одинаковая-ли масть у двух карт"""
        return self.suit == other_card.suit

    def equal_value(self, other_card) -> bool:
        """Проверяет одинаковые-ли значения у карт"""
        return self.value == other_card.value

    def more(self, other_card) -> bool:
        """Сравнивает старше-ли одна карта другой"""
        if self.VALUES.index(self.value) == other_card.VALUES.index(other_card.value):
            return self.SUITS.index(self.suit) > other_card.SUITS.index(other_card.suit)
        else:
            return self.VALUES.index(self.value) > other_card.VALUES.index(other_card.value)

    def less(self, other_card) -> bool:
        """Сравнивает младще-ли одна карта другой"""
        return not self.more(other_card)


class Deck:
    """Карточная колода"""
    def __init__(self):
        self.card_index = 0
        self.cards = []
        self.generate_deck()

    def generate_deck(self):
        """Генерирует упорядоченную колоду"""
        self.cards = [Card(value=value, suit=suit) for suit in Card.SUITS for value in Card.VALUES]

    def __str__(self):
        return self.show()

    def __repr__(self):
        return self.show()

    def __getitem__(self, item):
        return self.cards[item]

    def __iter__(self):
        self.card_index = 0
        return self

    def __next__(self):
        card = self.cards[self.card_index]
        self.card_index += 1
        if self.card_index >= len(self.cards):
            raise StopIteration
        return card

    def __len__(self):
        return len(self.cards)

    def show(self):
        """Строковое представление колоды"""
        return f'deck[{len(self.cards)}]:{self.cards}'

    def draw(self, count=1) -> list:
        """Достаёт указанное количество карт из колоды и возвращает список этих карт"""
        cards_in_hand = self.cards[:count]
        self.cards = self.cards[count:]
        return cards_in_hand

    def shuffle(self):
        """Тасует колоду"""
        self.cards = random.sample(self.cards, len(self.cards))


class Deck36(Deck):
    """Колода 36 карт"""
    def generate_deck(self):
        """Генерирует упорядоченную колоду в 36 карт"""
        self.cards = [Card(value=value, suit=suit) for suit in Card.SUITS for value in Card.VALUES[4:]]



if __name__ == '__main__':
    # Задание 1
    print('Сравнение двух карт')
    deck = Deck()
    print(f'Имеется колода карт: {deck}')
    deck.shuffle()
    print(f'Перемешаем её: {deck}')
    card1, card2 = deck.draw(2)
    print(f'Достанем две карты из колоды: {card1}, {card2}')
    print(f'В колоде остаётся: {deck}')
    if card1 > card2:
        print(f'Карта {card1} больше чем {card2}')
    else:
        print(f'Карта {card1} меньше чем {card2}')

    # Задание 2
    print('\n\nКаких мастей больше всего в колоде')
    deck = Deck()
    print(f'Достаём следующую колоду: {deck}')
    deck.shuffle()
    print(f'Перемешаем её: {deck}')
    hand = deck.draw(10)
    print(f'Берём 10 карт из колоды {hand}')
    hearts, diamonds, spades, clubs = [], [], [], []
    for card in hand:
        if card.suit == Card.HEARTS:
            hearts.append(card)
        elif card.suit == Card.DIAMONDS:
            diamonds.append(card)
        elif card.suit == Card.SPADES:
            spades.append(card)
        elif card.suit == Card.CLUBS:
            clubs.append(card)
    print(f'Черви {hearts}')
    print(f'Буби {diamonds}')
    print(f'Трефы {spades}')
    print(f'Пики {clubs}')
    counts = [len(clubs), len(spades), len(diamonds), len(hearts)]
    more_in_hand = Card.ICONS[counts.index(max(counts))]
    print(f'Больше всего в колоде: {more_in_hand} {Card.SUITS[Card.ICONS.index(more_in_hand)]}')

    # Задание 3
    print('\n\nВытягиваем карты по одной до тех пор пока в руке карты по возрастанию')
    deck = Deck()
    deck.shuffle()
    cards = []
    need_to_draw = True
    prev = Card(value=Card.VALUES[0], suit=Card.SUITS[0])
    print('Берём новую колоду, мешаем и начинаем тянуть по одной карте перемешивая пока не попадётся '
          'карта больше предыдущей')
    while need_to_draw:
        card_in_hand, = deck.draw(1)
        cards.append(card_in_hand)
        deck.shuffle()
        if card_in_hand > prev:
            need_to_draw = False
        prev = card_in_hand
    print(f'Получилась такая рука: {cards}')

    # Задание 4
    print('\n\nБитва колод')
    deck1 = Deck36()
    deck2 = Deck36()
    print(deck1)
    print(deck2)
    deck1.shuffle()
    deck2.shuffle()
    print(deck1)
    print(deck2)
    res = {'deck1': 0, 'deck2': 0}
    for i in range(len(deck1)):
        deck1_card = deck1.draw()
        deck2_card = deck2.draw()
        if deck1_card > deck2_card:
            res['deck1'] += 1
        else:
            res['deck2'] += 1
    print(f"Первая колода заработала {res['deck1']} очков, а вторая колода {res['deck2']}")

    # Задание 5 дурак без козырей
    print('\n\nДурак без козырей')
    deck = Deck36()
    deck.shuffle()
    player1_hand = sorted(deck.draw(6))
    player2_hand = sorted(deck.draw(6))
    desk = []
    game = True
    print(f'У игрока 1 в руке {player1_hand}, у игрока 2 в руке {player2_hand}')
    player1_card = player1_hand[0]
    player1_hand.remove(player1_card)
    print(f'Игрок 1 ходит картой {player1_card}')
    desk.append(player1_card)
    while game:
        fail = True
        for player2_card in player2_hand:
            if (desk[-1].suit == player2_card.suit) and (player2_card > desk[-1]):
                print(f'Игрок 2 бьёт картой {player2_card}')
                desk.append(player2_card)
                player2_hand.remove(player2_card)
                fail = False
                break
        if fail:
            game = False
            if len(desk) % 2 == 0:
                print('Ничья')
            else:
                print('Игрок 2 проиграл')
        player_one_can_throw = False
        for desk_card in desk:
            for player1_card in player1_hand:
                if player1_card.value == desk_card.value:
                    player_one_can_throw = True
                    print(f'Игрок 1 подкидывает {player1_card}')
                    desk.append(player1_card)
                    player1_hand.remove(player1_card)
                    break
        if not player_one_can_throw:
            print('Игроку 1 нечего подкидывать')
        print(f'На столе лежат карты {desk}')

    # Задание 6 Игра в две колоды
    print('\n\nИгра в две колоды')
    deck1 = Deck()
    deck2 = Deck()
    deck1.shuffle()
    deck2.shuffle()
    big_deck = Deck()
    big_deck.cards = deck1.draw(52) + deck2.draw(52)
    print(big_deck)
    big_deck.shuffle()
    print(big_deck)
    big_deck.draw(52)
    print(big_deck)
    hearts, diamonds, spades, clubs = [], [], [], []
    for card in big_deck:
        if card.suit == Card.HEARTS:
            hearts.append(card)
        elif card.suit == Card.DIAMONDS:
            diamonds.append(card)
        elif card.suit == Card.SPADES:
            spades.append(card)
        elif card.suit == Card.CLUBS:
            clubs.append(card)
    print(f'Черви {hearts}')
    print(f'Буби {diamonds}')
    print(f'Трефы {spades}')
    print(f'Пики {clubs}')
    counts = [len(clubs), len(spades), len(diamonds), len(hearts)]
    more_in_hand = Card.ICONS[counts.index(max(counts))]
    print(f'Больше всего в колоде: {more_in_hand} {Card.SUITS[Card.ICONS.index(more_in_hand)]}')


"""
Задание-6 “Игра в две колоды”

Создайте две колоды по 52 карты. Перемешайте их вместе - в итоге получится одна колода из 104 карт. Выбросите/вытяните половину карт. Узнайте, какой/каких мастей в колоде осталось больше всего?
"""
