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
    points_digits = ('2', '3', '4', '5', '6', '7', '8', '9', '10')
    points_ppl = ('J', 'Q', 'K')

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

    def __init__(self, new_cards=[]) -> []:
        self.cards = []
        self.points = 0
        if new_cards is None:
            return self.cards
        return self.cards.extend(new_cards)

    # метод take наследуется

    def give(self, card: Card = None) -> []:
        if card in self.cards:
            self.cards.remove(card)
            return self.cards
        else:
            return None

    def beat(self, other_card: Card = None) -> []:
        for card in self.cards:
            if card.suit == other_card.suit:
                if card > other_card:
                    self.cards.remove(card)
                    return card
        return []

    def sum_points(self):
        sum = 0
        for card in self.cards:
            if card.value in self.points_digits:
                sum += int(card.value)
                continue
            if card.value in self.points_ppl:
                sum += 10
                continue
            if card.value == 'A':
                if sum > 21:
                    sum += 1
                    continue
                sum += 11
                continue
        return sum


if __name__ == "__main__":
    print("Deck module")

