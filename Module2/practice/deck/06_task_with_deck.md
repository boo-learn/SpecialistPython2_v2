## Задания: с колодой карт


### Вступление

Вы создали свой класс колоды карт. Пришло время проверить его работу.

**Примечание**: если какие-то задания не получается выполнить, используя имеющийся функционал, то расширьте его, доработав/изменив/добавив необходимые методы.


### Задания


#### Задание-1

Создайте колоду из 52 карт. Перемешайте ее. Вытяните две карты сверху. Сравните эти карты и выведите сообщение формата: “карта A♦ больше J♣”


#### Задание-2

Создайте колоду из 52 карт. Перемешайте ее. Вытяните 10 карт сверху и посчитайте карт какой/каких мастей среди вытянутых карт оказалось больше всего?


#### Задание-3

Создайте колоду из 52 карт. Перемешайте ее. Вытяните одну карту сверху. Снова перемешайте колоду и вытяните еще одну. Если вторая карта меньше первой, повторите “перемешать + вытянуть”, до тех пор, пока не вытяните карту больше предыдущей карты. В качестве результата выведи все вытягиваемые карты в консоль.

'''
import random
from collections import Counter


class Card:

    HEARTS = "Hearts"
    DIAMONDS = "Diamonds"
    SPADES = "Spades"
    CLUBS = "Clubs"
    VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    SUITS_RANK = ["Spades", "Clubs", "Diamonds", "Hearts"]

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        icons = {
            "Hearts": '\u2665',
            "Diamonds": '\u2666',
            "Spades": '\u2663',
            "Clubs": '\u2660',
        }
        return f"{self.value}{icons[self.suit]}"

    def __repr__(self):
        icons = {
            "Hearts": '\u2665',
            "Diamonds": '\u2666',
            "Spades": '\u2663',
            "Clubs": '\u2660',
        }
        return f"{self.value}{icons[self.suit]}"

    def equal_suit(self, other_card):
        return self.suit == other_card.suit

    def __gt__(self, other_card):
        if self.value != other_card.value:
            return Card.VALUES.index(self.value) > Card.VALUES.index(other_card.value)
        else:
            return Card.SUITS_RANK.index(self.suit) > Card.SUITS_RANK.index(other_card.suit)

    def __lt__(self, other_card):
        if self.value != other_card.value:
            return Card.VALUES.index(self.value) < Card.VALUES.index(other_card.value)
        else:
            return Card.SUITS_RANK.index(self.suit) < Card.SUITS_RANK.index(other_card.suit)


class Deck:
    def __init__(self):
        self.cards = []
        self.create_deck()

    def create_deck(self):
        res = list()
        for suit in [Card.HEARTS, Card.DIAMONDS, Card.SPADES, Card.CLUBS]:
            for value in Card.VALUES:
                res.append(Card(value, suit))
        self.cards = res

    def __str__(self):
        to_show = [card.__str__() for card in self.cards]
        return f'deck[{len(self.cards)}]: {", ".join(to_show)}'

    def draw(self, number):
        to_show = self.cards[:number]
        self.cards = self.cards[number:]
        return to_show

    def shuffle(self):
        random.shuffle(self.cards)

    def __getitem__(self, key):
        return self.cards[key]

    def __iter__(self):
        return iter(self.cards)

# task 1

print('task1\n')
deck = Deck()
deck.shuffle()
card1, card2 = deck.draw(2)
if card1 < card2:
    print(f'карта {card1} меньше {card2}')
else:
    print(f'карта {card1} больше {card2}')


# task 2
deck = Deck()
deck.shuffle()
cards = deck.draw(10)
suits = Counter([card.suit for card in cards]).items()
max_suit = sorted(suits, key=lambda x: x[1])[-1][0]

print('*'* 30)
print('task2\n')
print(f'В колоде оказалось больше всего карт масти {max_suit}')


# task 3
deck = Deck()
deck.shuffle()
card1 = deck.draw(1)[0]
deck.shuffle()
card2 = deck.draw(1)[0]
trials = [card2]
while card2 < card1:
    card2 = deck.draw(1)[0]
    trials.append(card2)

print('*'* 30)
print('task3\n')
print(f'Карта {card2} больше {card1}')
print(f'Первая вытянутая карта - {card1}')
print(f'Остальные вытянутые карты: {", ".join([str(i) for i in trials])}')

'''


#### Задание-4

Создайте две колоды, в каждой должно быть 36 карт(старшинство карт начинается с 6-ки). Перемешайте их.

Вытягивайте карты парами - одну из первой колоды, вторую из второй.

Если карта из первой колоды окажется больше(старше), то записываем 1:0 (условно начисляем победное очко первой колоде), если карты одинаковые, то не учитываем очко никуда.

Выведите итоговый счет, сравнив попарно все карты в колодах.


#### Задание-5 “Дурак без козырей”

Теперь немного сложнее: создадим имитацию одного хода в “Дурака без козырей”.



1. Создайте колоду из 52 карт. Перемешайте ее.
2. Первый игрок берет сверху 6 карт
3. Второй игрок берет сверху 6 карт.
4. Игрок-1 ходит:
    1. игрок-1 выкладывает самую маленькую карту по значению
    2. игрок-2 пытается бить карту, если у него есть такая же масть но значением больше. 
    3. Если игрок-2 не может побить карту, то он проигрывает.
    4. Если игрок-2 бьет карту, то игрок-1 может подкинуть карту любого значения, которое есть на столе.
5. Выведите в консоль максимально наглядную визуализацию данного игрового хода.


#### Задание-6 “Игра в две колоды”

Создайте две колоды по 52 карты. Перемешайте их вместе - в итоге получится одна колода из 104 карт. Выбросите/вытяните половину карт. Узнайте, какой/каких мастей в колоде осталось больше всего?
