# Начнем с создания карты
import random


class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        # TODO-1: метод возвращает строковое представление карты в виде: 10♥ и A♦
        return f'{self.value}{self.__suit_icon_mapping[self.suit]}'

    __suit_icon_mapping = {
        'Diamonds': '\u2666',
        'Hearts': '\u2665',
        'Spades': '\u2660',
        'Clubs': '\u2663'
    }

    def equal_suit(self, other_card) -> bool:
        # TODO-1: метод возвращает True - если масти карт равны или False - если нет
        return self.suit == other_card.suit

    # TODO-1: реализуем новые методы
    __suit_value_mapping = {
        'Spades': 0,
        'Clubs': 1,
        'Diamonds': 2,
        'Hearts': 4
    }
    __suit_mapping = {
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 14
    }

    def more(self, other_card):
        if self.value == other_card.value:
            return self.__suit_value_mapping[self.suit] > self.__suit_value_mapping[other_card.suit]
        else:
            return self.__suit_mapping[self.value] > self.__suit_mapping[other_card.value]

    def less(self, other_card):
        if self.value == other_card.value:
            return self.__suit_value_mapping[self.suit] < self.__suit_value_mapping[other_card.suit]
        else:
            return self.__suit_mapping[self.value] < self.__suit_mapping[other_card.value]


class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.cards = []
        # TODO-1: конструктор добавляет в список self.cards все(52) карты
        for suit in suits:
            for value in values:
                self.cards.append(Card(value, suit))

    def show(self) -> str:
        # TODO-2: Принцип работы данного метода прописан в 00_task_deck.md
        cards_str = []
        for card in self.cards:
            cards_str.append(card.to_str())
        return f"cards[{len(self.cards)}]:" + ", ".join(cards_str)

    def draw(self, x) -> list:
        # TODO-1: Принцип работы данного метода прописан в 00_task_deck.md
        hand_deck = self.cards[:x]
        self.cards = self.cards[x:]
        return hand_deck

    def shuffle(self):
        # TODO-2: Принцип работы данного метода прописан в 00_task_deck.md
        #   Подсказка: https://www.w3schools.com/python/ref_random_shuffle.asp
        random.shuffle(self.cards)


# Создаем колоду
deck = Deck()
# Тусуем колоду
deck.shuffle()
print(deck.show())
# Берем две карты из колоды
card1, card2 = deck.draw(2)

# Тестируем методы .less() и .more()
if card1.more(card2):
    print(f"{card1.to_str()} больше {card2.to_str()}")
if card1.less(card2):
    print(f"{card1.to_str()} меньше {card2.to_str()}")
