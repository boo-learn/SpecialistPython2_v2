import random


class Card:
    suits = ("Hearts", "Diamonds", "Spades", "Clubs")
    values = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        icons = {"Hearts": '\u2665', "Diamonds": '\u2666', "Spades": '\u2660', "Clubs": '\u2663'}
        return f"{self.value}{icons[self.suit]}"

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
    cur = 0
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        suits = ("Hearts", "Diamonds", "Spades", "Clubs")
        values = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
        self.cards = []
        for suit in suits:
            for value in values:
                self.cards.append(Card(value, suit))

    def __str__(self) -> str:
        """
        Отображает все карты колоды в формате: deck[12]: 3♥, 4♦, A♣, …
        :return: Возвращает строку с картами колоды в формате: deck[12]: 3♥, 4♦, A♣, …
        """
        s = f'deck[{len(self.cards)}]: '
        for card in self.cards:
            s += str(card) + ', '
        return s[:-2]

    def __iter__(self):
        self.cur = 0
        return self

    def __next__(self):
        if self.cur < len(self.cards):
            self.cur += 1
            return self.cards[self.cur-1]
        else:
            raise StopIteration

    def __getitem__(self, key):
        return self.cards[key]

    def draw(self, per_hand: int) -> []:
        """
        возвращает per_hand первых карт из колоды в виде списка, эти карты убираются из колоды. Уточнение: первую карту в списке считаем верхней картой колоды
        :param per_hand: количество карт, который выдаются из колоды
        :return: Возврщает список per_hand верхних карт колоды
        """
        hand = []
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


deck = Deck()
# Задачи - реализовать нативную работу с объектами:
# 1. Вывод колоды в терминал:
print(deck)  # вместо print(deck.show())

card1, card2 = deck.draw(2)
# 2. Вывод карты в терминал:
print(card1)  # вместо print(card1.to_str())

# 3. Сравнение карт:
if card1 > card2:
    print(f"{card1} больше {card2}")

# 4. Итерация по колоде:
for card in deck:
    print(card)

# Просмотр карты в колоде по ее индексу:
print(deck[6])
