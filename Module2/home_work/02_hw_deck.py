# Закончите все Задания: с колодой карт из файла practice/06_task_with_deck.md

# Закончите все Задания: с колодой карт из файла practice/06_task_with_deck.md
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

    def __str__(self):
        return f"{self.value}{Card.ICONS[self.suit]}"

    def to_str(self):
        return f"{self.value}{Card.ICONS[self.suit]}"

    def equal_suit(self, other_card):
        return self.suit == other_card.suit

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


class Deck:
    SUITS = [Card.SPADES, Card.CLUBS, Card.DIAMONDS, Card.HEARTS]
    VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self):
        self.card_index = 0
        self.cards = []
        for value in Deck.VALUES:
            for suit in Deck.SUITS:
                self.cards.append(Card(value, suit))

    def show(self):
        return f'deck[{len(self.cards)}]:' + ', '.join([card.to_str() for card in self.cards])

    def __str__(self):
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


# Задание-5 “Дурак без козырей”

# Теперь немного сложнее: создадим имитацию одного хода в “Дурака без козырей”.
#     Создайте колоду из 52 карт. Перемешайте ее.
#     Первый игрок берет сверху 6 карт
#     Второй игрок берет сверху 6 карт.
#     Игрок-1 ходит:
#         игрок-1 выкладывает самую маленькую карту по значению
#         игрок-2 пытается бить карту, если у него есть такая же масть но значением больше.
#         Если игрок-2 не может побить карту, то он проигрывает.
#         Если игрок-2 бьет карту, то игрок-1 может подкинуть карту любого значения, которое есть на столе.
#     Выведите в консоль максимально наглядную визуализацию данного игрового хода.


deck = Deck()
deck.shuffle()
print(deck)

player1 = deck.draw(6)
player2 = deck.draw(6)

count_player1 = 0
count_player2 = 0

while len(player1) > 0:
    print("Карты игрока 1: ", end='')
    for card in player1:
        print(card, end=' ')
    print('')

    print("Карты игрока 2: ", end='')
    for card in player2:
        print(card, end=' ')
    print('')

    card1 = min(player1)
    print("Игрок1 ходит:", card1)
    player1.pop(player1.index(card1))

    flag_ = False
    for card in player2:
        if card.suit == card1.suit and card > card1:
            print("Игрок2 бьет:", card)
            last_card = card
            player2.pop(player2.index(last_card))
            flag_ = True
            break

    if not flag_:
        print("Игрок2 бить нечем!")
        count_player1 += 1
        try:
            player2.pop()
        except IndexError:
            break

    flag__ = False
    if flag_:
        flag_ = False
        for card in player1:
            if last_card.value == card.value:
                print("Игрок1 подкидывает:", card)
                last_card = card
                player1.pop(player1.index(last_card))
                flag__ = True
                break
        if not flag__:
            print("Игрок1 нету!")
            count_player2 += 1

    if flag__:
        flag__ = False
        for card in player2:
            if card.suit == last_card.suit and card > last_card:
                print("Игрок2 бьет:", card)
                last_card = card
                player2.pop(player2.index(last_card))
                flag_ = True
                break
        if not flag_:
            print("Игрок2 бить нечем!")
            count_player1 += 1
            player2.pop()

    if flag_:
        flag_ = False
        for card in player1:
            if last_card.value == card.value:
                print("Игрок1 подкидывает:", card)
                last_card = card
                player1.pop(player1.index(last_card))
                flag__ = True
                break
        if not flag__:
            print("Игрок1 нету!")
            count_player2 += 1

    print(f"Счет партии: {count_player1}:{count_player2}")

    if len(deck) >= 6 - len(player1) * 2:
        player1 += deck.draw(6 - len(player1))
        player2 += deck.draw(6 - len(player2))
    else:
        player1 += deck.draw(len(deck) // 2)
        player2 += deck.draw(len(deck) // 2)

print(f"Счет игры: {count_player1}:{count_player2}")
