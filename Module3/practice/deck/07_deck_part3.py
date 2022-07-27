class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты
        self.suit_icons = {'Hearts': '\u2665', 'Diamonds': '\u2666', 'Clubs': '\u2663', 'Spades': '\u2660'}
        self.suit_value = {'Hearts': 4, 'Diamonds': 3, 'Clubs': 2, 'Spades': 1}
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.value_dict = {v: k for k, v in enumerate(values)}

    def to_str(self):
        # TODO-1: метод возвращает строковое представление карты в виде: 10♥ и A♦
        return f'{self.value}{self.suit_icons.get(self.suit)}'


    def equal_suit(self, other_card):
        # TODO-1: метод возвращает True - если масти карт равны или False - если нет
        return self.suit == other_card.suit

    def more(self, other_card):
        if self.value_dict.get(self.value) > other_card.value_dict.get(other_card.value):
            return True
        elif self.value_dict.get(self.value) == other_card.value_dict.get(other_card.value) and self.suit_value.get(self.suit) > other_card.suit_value.get(other_card.suit):
            return True
        else:
            return False

    def less(self, other_card):
        if self.value_dict.get(self.value) < other_card.value_dict.get(other_card.value):
            return True
        elif self.value_dict.get(self.value) == other_card.value_dict.get(other_card.value) and self.suit_value.get(self.suit) < other_card.suit_value.get(other_card.suit):
            return True
        else:
            return False

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
        # TODO-2: Принцип работы данного метода прописан в 00_task_deck.md
        return f'deck[{len(self.cards)}]: {", ".join([card.to_str() for card in self.cards])}'

    def draw(self, x):
        # TODO-1: Принцип работы данного метода прописан в 00_task_deck.md
        self.hand = []

        for card in self.cards[:x]:
            self.hand.append(card)
            self.cards.remove(card)

        return self.hand

    def shuffle(self):
        # TODO-2: Принцип работы данного метода прописан в 00_task_deck.md
        #   Подсказка: https://www.w3schools.com/python/ref_random_shuffle.asp
        import random
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
