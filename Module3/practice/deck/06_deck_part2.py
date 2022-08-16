import random


class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def __get_suit_symbol(self, suit):
        suits = {
            "Hearts": "\u2665",
            "Diamonds": "\u2666",
            "Spades": "\u2663",
            "Clubs": "\u2660"

        }
        return suits[suit]

    def to_str(self):
        # TODO-1: метод возвращает строковое представление карты в виде: 10♥ и A♦
        return f"{self.value}{self.__get_suit_symbol(self.suit)}"

    def equal_suit(self, other_card):
        # TODO-1: метод возвращает True - если масти карт равны или False - если нет
        return self.suit == other_card.suit


class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.cards = []
        for suit in suits:
            for value in values:
                self.cards.append(Card(value, suit))
        # TODO-1: конструктор добавляет в список self.cards все(52) карты

    def __get_list_cards(self):
        cards_list = []
        for card in self.cards:
            cards_list.append(card.to_str())
        return cards_list

    def show(self):
        # TODO-2: Принцип работы данного метода прописан в 00_task_deck.md
        cards_list = self.__get_list_cards()
        return f"cards[{len(self.cards)}]{' ,'.join(cards_list)}"

    def draw(self, x):
        cards_list = self.__get_list_cards()
        x_cards = cards_list[:x]
        self.cards = self.cards[x:]
        return x_cards

    def shuffle(self):
        # TODO-2: Принцип работы данного метода прописан в 00_task_deck.md
        #   Подсказка: https://www.w3schools.com/python/ref_random_shuffle.asp
        return random.shuffle(self.cards)


# Создаем колоду
deck = Deck()
# Выводим колоду в формате указанном в основном задании
print(deck.show())
# Тусуем колоду
deck.shuffle()
print(deck.show())
#
# Возьмем 5 карт "в руку"
hand = deck.draw(5)
# Выводим колоду, чтобы убедиться что 5 верхних карт отсутствуют
print(deck.show())
# Выводим список карт "в руке"(список hand)
# print(...)
