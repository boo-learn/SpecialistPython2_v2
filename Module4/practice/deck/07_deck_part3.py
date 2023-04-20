import random
class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        # Символы для отображения мастей
        suit_symbols = {"Hearts": "\u2665", "Diamonds": "\u2666",
                        "Clubs": "\u2663", "Spades": "\u2660"}
        # Строковое представление карты вида "значение масть"
        return self.value + suit_symbols[self.suit]

    def equal_suit(self, other_card):
        # TODO-1: метод возвращает True - если масти карт равны или False - если нет
        return self.suit == other_card.suit
    def more(self, other_card):
        values = {"2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7,
                  "9": 8, "10": 9, "J": 10, "Q": 11, "K": 12, "A": 13}
        return values[self.value] > values[other_card.value]

    def less(self, other_card):
        values = {"2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7,
                  "9": 8, "10": 9, "J": 10, "Q": 11, "K": 12, "A": 13}
        return values[self.value] < values[other_card.value]


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

    def show(self):
        cards_str = []
        for card in self.cards:
            cards_str.append(card.to_str())
        return f"cards[{len(self.cards)}]:" + ", ".join(cards_str)

    def draw(self, x):
        # TODO-1: Принцип работы данного метода прописан в 00_task_deck.md
        if x > len(self.cards):
            return None
        hand = []
        for i in range(x):
            hand.append(self.cards.pop(0))
        return hand

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
