import random


class Card:
    HEARTS = 'Hearts'
    DIAMONDS = 'Diamonds'
    SPADES = 'Spades'
    CLUBS = 'Clubs'

    suit_simbol = {HEARTS: '\u2665',
                   DIAMONDS: '\u2666',
                   CLUBS: '\u2663',
                   SPADES: '\u2660'}

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f'{self.value}{Card.suit_simbol[self.suit]}'

    def equal_suit(self, card2):
        return self.suit == card2.suit

    def __gt__(self, card2):
        if Deck.values.index(self.value) == Deck.values.index(card2.value):
            return Deck.suits.index(self.suit) > Deck.suits.index(card2.suit)
        else:
            return Deck.values.index(self.value) > Deck.values.index(card2.value)

    def __eq__(self, other):
        return self.value == other.value and self.suit == other.suit


class Deck:
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = [Card.HEARTS, Card.DIAMONDS, Card.CLUBS, Card.SPADES]

    def __init__(self, num_cards=52):
        self.cards = []
        if num_cards == 36:
            self.values = Deck.values[4:]
        for key in Deck.suits:
            for i in self.values:
                self.cards.append(Card(i, key))
        self.index = 0

    def __repr__(self):
        # Переопределелили метод repr (принт)
        tmp = []
        for i in self.cards:
            tmp.append(Card.__repr__(i))
        return f'deck[{len(self.cards)}]: {", ".join(tmp)}'

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        try:
            card = self.cards[self.index]
        except:
            raise StopIteration
        self.index += 1
        return card

    def draw(self, x):
        # начало списка считаем верхом колоды
        cards = []
        for _ in range(x):
            cards.append(self.cards.pop(0))
        return cards

    def draw_card(self):
        return self.cards.pop(0)

    def shuffle(self):
        random.shuffle(self.cards)

    def suit_calc(self):
        hearts = []
        diamonds = []
        clubes = []
        spades = []
        for i in range(len(self.cards)):
            if self.cards[i].suit == Card.HEARTS:
                hearts.append(self.cards[i])
            elif self.cards[i].suit == Card.DIAMONDS:
                diamonds.append(self.cards[i])
            elif self.cards[i].suit == Card.CLUBS:
                clubes.append(self.cards[i])
            else:
                spades.append(self.cards[i])
        return max(len(hearts), len(diamonds), len(clubes), len(spades))

    def __getitem__(self, index):
        return self.cards[index]


class Hand:
    HAND_SIZE_DEF = 6

    def __init__(self, deck, hand_size=HAND_SIZE_DEF):
        self.cards = Deck.draw(deck, hand_size)

    def __repr__(self):
        tmp = []
        for i in self.cards:
            tmp.append(Card.__repr__(i))
        return f'[{len(self.cards)}]: {", ".join(tmp)}'

    def attack_move(self, table):
        attack_choice = []
        if table:
            for i in range(len(self.cards)):
                for j in range(len(table)):
                    try:
                        if self.cards[i].value == table[j].value:
                            attack_choice.append(self.cards[i])
                    except AttributeError:
                        continue

            if attack_choice:
                attack_card = min(attack_choice)
                self.cards.remove(attack_card)
                return attack_card
            else:
                return None
        else:
            attack_card = min(self.cards)
            self.cards.remove(attack_card)
            return attack_card

    def defence_move(self, attack_card):
        defence_choice = []
        for i in range(len(self.cards)):
            try:
                if self.cards[i].suit == attack_card.suit and self.cards[i].value > attack_card.value:
                    defence_choice.append(self.cards[i])
            except AttributeError:
                continue
        if defence_choice:
            defence_card = min(defence_choice)
            self.cards.remove(defence_card)
            return defence_card
        else:
            return None

# Задание-5 “Дурак без козырей”
# Теперь немного сложнее: создадим имитацию одного хода в “Дурака без козырей”.
# 1. Создайте колоду из 52 карт. Перемешайте ее.
# 2. Первый игрок берет сверху 6 карт
# 3. Второй игрок берет сверху 6 карт.
# 4. Игрок-1 ходит:
#     1. игрок-1 выкладывает самую маленькую карту по значению
#     2. игрок-2 пытается бить карту, если у него есть такая же масть но значением больше.
#     3. Если игрок-2 не может побить карту, то он проигрывает.
#     4. Если игрок-2 бьет карту, то игрок-1 может подкинуть карту любого значения, которое есть на столе.
# 5. Выведите в консоль максимально наглядную визуализацию данного игрового хода.

table = []
deck = Deck()
deck.shuffle()
hand1 = Hand(deck)
print(f'Рука игрока 1: {hand1}')
hand2 = Hand(deck)
print(f'Рука игрока 2: {hand2}')
attack_card = []
defence_card = []

while attack_card is not None and defence_card is not None:
    attack_card = hand1.attack_move(table)
    table.append(attack_card)
    if attack_card is None:
        print('Игроку 1 нечего подкинуть - ход завершен')
        break
    else:
        print(f'Игрок 1 ходит картой {attack_card}')
    defence_card = hand2.defence_move(attack_card)
    table.append(defence_card)
    if defence_card is None:
        print('Игрок 2 не может отбить карту и проигрывает')
    else:
        print(f'Игрок 2 отбивается картой {defence_card}')
