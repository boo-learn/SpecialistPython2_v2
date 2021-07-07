import random


class Card:
    suits = ("Hearts", "Diamonds", "Spades", "Clubs")
    values = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
    icons = {"Hearts": '\u2665', "Diamonds": '\u2666', "Spades": '\u2660', "Clubs": '\u2663'}

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return f"{self.value}{Card.icons[self.suit]}"

    def __repr__(self):
        return self.__str__()

    def equal_suit(self, other_card):
        if self.suit == other_card.suit:
            return True
        else:
            return False

    def __gt__(self, other_card) -> bool:
        """
        Если у карты больше(старше) значение, то она больше(старше). При равенстве значений, сравниваем масти. Старшинство мастей определяем следующее: ♥>♦>♣>♠
        :param other_card: вторая карта для сравнения
        :return: возвращает результат сравнения
        """
        if self.values.index(self.value) == self.values.index(other_card.value):
            return self.suits.index(self.suit) > self.suits.index(other_card.suit)
        else:
            return self.values.index(self.value) > self.values.index(other_card.value)

    def __lt__(self, other_card):
        """
        проверяет является ли карта младше, чем карта в параметре. При равенстве значений, сравниваем масти. Старшинство мастей определяем следующее: ♥>♦>♣>♠
        :param other_card: вторая карта для сравнения
        :return: возвращает результат сравнения
        """
        if self.values.index(self.value) == self.values.index(other_card.value):
            return self.suits.index(self.suit) < self.suits.index(other_card.suit)
        else:
            return self.values.index(self.value) < self.values.index(other_card.value)


class Deck:
    """
    Колода карт, при создании состоит из 52-ух карт
    """
    NAME = "Deck"
    HEARTS = "Hearts"
    DIAMONDS = "Diamonds"
    SPADES = "Spades"
    CLUBS = "Clubs"
    suits = ("Hearts", "Diamonds", "Spades", "Clubs")
    values13 = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
    values9 = ('6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')

    def __init__(self, val=52):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        if val == 36:
            self.values = Deck.values9
        else:
            self.values = Deck.values13

        self.cards = []
        for suit in Deck.suits:
            for value in self.values:
                self.cards.append(Card(value, suit))

    def __str__(self) -> str:
        """
        Отображает все карты колоды в формате: deck[12]: 3♥, 4♦, A♣, …
        :return: Возвращает строку с картами колоды в формате: deck[12]: 3♥, 4♦, A♣, …
        """
        s = f'{self.NAME}[{len(self.cards)}]: '
        for card in self.cards:
            s += str(card) + ', '
        return s[:-2]

    def __iter__(self):
        """
        итератор для контейнера
        :return: возвращает итератор для контейнера
        """
        self.cur = -1
        return self

    def __next__(self) -> Card:
        """
        следующий элемент итератора для контейнера
        :return: возвращает следующий элемент итератора для контейнера
        """
        if self.cur < len(self.cards) - 1:
            self.cur += 1
            return self.cards[self.cur]
        else:
            raise StopIteration

    def __getitem__(self, key) -> Card:
        """
        доступ карту колоды по индексу
        :param key: значение индекса
        :return: возвращает карту по индексу
        """
        return self.cards[key]

    def draw(self, per_hand: int) -> []:
        """
        возвращает per_hand первых карт из колоды в виде списка, эти карты убираются из колоды. Уточнение: первую карту
        в списке считаем верхней картой колоды
        :param per_hand: количество карт, который выдаются из колоды
        :return: Возврщает список per_hand верхних карт колоды
        """
        hand = []
        if len(self.cards) > 0:
            for i in range(per_hand):
                hand.append(self.cards[0])
                self.cards.pop(0)
        return hand

    def shuffle(self):
        """
        перемешивает колоду, располагая карты в случайном порядке.
        :return:
        """
        return random.shuffle(self.cards)

    def take(self, new_cards=None):
        """
        Добавляет в колоду произвольное количество карт
        :param new_cards: список новых карт
        :return: Возвращает новую колоду
        """
        if new_cards is None:
            return self.cards
        return self.cards.extend(new_cards)


class Hand(Deck):
    NAME = "Hand"

    def __init__(self, new_cards=None):
        self.cards = []
        if new_cards is None:
            return self.cards
        return self.cards.extend(new_cards)

    def take(self, new_cards=None):
        if new_cards is None:
            return self.cards
        return self.cards.extend(new_cards)

    def give(self, card: Card = None):
        if card in self.cards:
            self.cards.remove(card)
            return self.cards
        else:
            return None

    def beat(self, other_card: Card = None):
        for card in self.cards:
            if card.suit == other_card.suit:
                if card > other_card:
                    self.cards.remove(card)
                    return card
        return None


print('Задание-1')
# # Создайте колоду из 52 карт. Перемешайте ее. Вытяните две карты сверху.
# # Сравните эти карты и выведите сообщение формата: “карта A♦ больше J♣”
deck1 = Deck()
deck1.shuffle()
card1, card2 = deck1.draw(2)
if card1 > card2:
    print(f"Карта {card1} больше {card2}")

print('Задание-2')
# # Создайте колоду из 52 карт. Перемешайте ее. Вытяните 10 карт сверху и посчитайте карт какой/каких мастей
# # среди вытянутых карт оказалось больше всего?
deck2 = Deck()
deck2.shuffle()
cards = deck2.draw(10)
print(cards)
suits_cnt = {"Hearts": 0, "Diamonds": 0, "Spades": 0, "Clubs": 0}
# suits_cnt = {}
max_cnt = 0
for card in cards:
    suits_cnt[card.suit] += 1
    if max_cnt < suits_cnt[card.suit]:
        max_cnt = suits_cnt[card.suit]

for suit in suits_cnt:
    if suits_cnt[suit] == max_cnt:
        print(f"{suit}({Card.icons[suit]}): {max_cnt}")

print('Задание-3')
# Создайте колоду из 52 карт. Перемешайте ее. Вытяните одну карту сверху. Снова перемешайте колоду и вытяните еще одну.
# Если вторая карта меньше первой, повторите “перемешать + вытянуть”, до тех пор, пока не вытяните карту больше
# предыдущей карты. В качестве результата выведи все вытягиваемые карты в консоль.
deck3 = Deck()
deck3.shuffle()
card1 = deck3.draw(1)
print(card1)
while True:
    deck3.shuffle()
    card2 = deck3.draw(1)
    if card1 < card2:
        print(f"{card1} < {card2}: break")
        break
    print(f"{card1} > {card2}: continue")
    card1 = card2

print('Задание-4')
# Создайте две колоды, в каждой должно быть 36 карт(старшинство карт начинается с 6-ки). Перемешайте их.
# Вытягивайте карты парами - одну из первой колоды, вторую из второй.
# Если карта из первой колоды окажется больше(старше), то записываем 1:0 (условно начисляем победное очко первой
# колоде), если карты одинаковые, то не учитываем очко никуда.
# Выведите итоговый счет, сравнив попарно все карты в колодах.
deck4 = Deck(36)
deck4.shuffle()
deck5 = Deck(36)
deck5.shuffle()
result = [0, 0]
for i in range(len(deck4.cards)):
    if deck4[i] > deck5[i]:
        result[0] += 1
    if deck4[i] < deck5[i]:
        result[1] += 1
print(f"Счет deck4: {result[0]} - deck5: {result[1]}")

print('Задание-5 “Дурак без козырей”')
# Теперь немного сложнее: создадим имитацию одного хода в “Дурака без козырей”.
# Создайте колоду из 52 карт. Перемешайте ее.
# Первый игрок берет сверху 6 карт
# Второй игрок берет сверху 6 карт.
# Игрок-1 ходит:
# игрок-1 выкладывает самую маленькую карту по значению
# игрок-2 пытается бить карту, если у него есть такая же масть но значением больше.
# Если игрок-2 не может побить карту, то он проигрывает.
# Если игрок-2 бьет карту, то игрок-1 может подкинуть карту любого значения, которое есть на столе.
# Выведите в консоль максимально наглядную визуализацию данного игрового хода.
deck6 = Deck()
deck6.shuffle()
hand1 = Hand(deck6.draw(6))
hand2 = Hand(deck6.draw(6))
print(hand1)
print(hand2)

while True:
    if len(hand1.cards) < 1:
        print(f"Draw")
        break
    h1 = min(hand1)
    hand1.give(h1)
    print(f"hand1: {h1} - ", end="")
    h2 = hand2.beat(h1)
    if h2 is None:
        print(f"hand2 lose")
        break
    else:
        print(f"hand2: {h2}")


print('Задание-6 “Игра в две колоды”')
# Создайте две колоды по 52 карты. Перемешайте их вместе - в итоге получится одна колода из 104 карт.
# Выбросите/вытяните половину карт. Узнайте, какой/каких мастей в колоде осталось больше всего?
deck7 = Deck()
deck8 = Deck()
deck7.take(deck8.cards)
deck7.shuffle()
deck7.draw(52)
print(deck7)

suits_cnt = {"Hearts": 0, "Diamonds": 0, "Spades": 0, "Clubs": 0}
max_cnt = 0
for card in deck7.cards:
    suits_cnt[card.suit] += 1
    if max_cnt < suits_cnt[card.suit]:
        max_cnt = suits_cnt[card.suit]

for suit in suits_cnt:
    if suits_cnt[suit] == max_cnt:
        print(f"{suit}({Card.icons[suit]}): {max_cnt}")
