"""Задание-5 “Дурак без козырей”

Теперь немного сложнее: создадим имитацию одного хода в “Дурака без козырей”.



1. Создайте колоду из 52 карт. Перемешайте ее.
2. Первый игрок берет сверху 6 карт
3. Второй игрок берет сверху 6 карт.
4. Игрок-1 ходит:
    1. игрок-1 выкладывает самую маленькую карту по значению
    2. игрок-2 пытается бить карту, если у него есть такая же масть но значением больше. 
    3. Если игрок-2 не может побить карту, то он проигрывает.
    4. Если игрок-2 бьет карту, то игрок-1 может подкинуть карту любого значения, которое есть на столе.
5. Выведите в консоль максимально наглядную визуализацию данного игрового хода."""



import random


class Card:
    SUITS = ['♥', '♦', '♣', '♠']
    VALUES = [str(i) for i in range(2, 11)] + ['J', 'Q', 'K', 'A']

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit        

    def __repr__(self):        
        return f'{self.value}{self.suit}'

    def __gt__(self, other):
        if self.value == other.value:
            return Card.SUITS.index(self.suit) < Card.SUITS.index(other.suit)
        else:
            return Card.VALUES.index(self.value) > Card.VALUES.index(other.value)
    def __eq__(self, other):
        return (self.suit == other.suit) & (self.value == other.value)

    def __lt__(self, other):
        return not self.__gt__(other)

    def equal_suit(self, other_card):
        return self.suit == other_card.suit


class Deck:
    def __init__(self, list_cards = None):
        self.count = 0
        self.deck = list_cards if list_cards else []
        for suit in Card.SUITS:
            for value in Card.VALUES:
                self.deck.append(Card(value, suit))

    def __repr__(self):
        return f'deck[{len(self.deck)}]: ' + ', '.join([str(card) for card in self.deck])

    def __len__(self):
        return len(self.deck)

    def __getitem__(self, key):        
        return self.deck[key]

    def __iter__(self):
        self.count = 0
        return self

    def __next__(self):
        if self.count >= len(self.deck):
            raise StopIteration
        card = self.deck[self.count]
        self.count += 1        
        return card

    def __add__(self, other):
        return Deck(self.deck + other.deck)

    def draw(self, how_much):
        out = []
        for i in range(how_much):
            try:
                out.append(self.deck.pop(0))
            except IndexError:
                break
        return out

    def shuffle(self):
        random.shuffle(self.deck)


class Deck_36(Deck):
    def __init__(self):
        self.count = 0
        self.deck = []
        for suit in Card.SUITS:
            for value in Card.VALUES[4:]:
                self.deck.append(Card(value, suit))

## Всегда ходит первый игрок :(

deck = Deck_36()
deck.shuffle()
player_1 = deck.draw(6)
player_2 = deck.draw(6)
while deck or player_1:
    print('*' * 40)
    table = []
    ## Добираем при необходимости
    if len(player_1) < 6:
        player_1 += deck.draw(6 - len(player_1))
    if len(player_2) < 6:
        player_2 += deck.draw(6 - len(player_2))        
    print('player1_hand', player_1)
    print('player2_hand', player_2)
    ## Игрок 1 решает с чего ходить
    move_1 = min(player_1)
    print('player1 move', move_1)
    table.append(move_1)
    player_1.remove(move_1)
    ## Игрок 2 решает с чего ходить
    while move_1:
        player_2_moves = []
        for card in player_2:
            if card.equal_suit(move_1) and card > move_1:
                player_2_moves.append(card)
        if player_2_moves:
            move_2 = min(player_2_moves)
            print('on table', table)
            table.append(move_2)            
            print('player2 move', move_2)
            player_2.remove(move_2)
            ## Игрок 1 решает может ли что-нибудь подкинуть
            player_1_moves = []
            for card_in_hand in player_1:
                for card_on_table in table:
                    if card_in_hand.value == card_on_table.value:
                        player_1_moves.append(card_in_hand)
            if player_1_moves:
                move_1 = min(player_1_moves)
                table.append(move_1)
                player_1.remove(move_1)
            else:                
                move_1 = []
        else:
            player_2 += table
            move_1 = []


