# Начнем с создания карты
import random


class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты
        self.suit_dict = {
            'Hearts': '\u2665',
            'Diamonds': '\u2666',
            'Spades': '\u2660',
            'Clubs': '\u2663'
        }

    def to_str(self):
        return self.value + self.suit_dict.get(self.suit)

    def equal_suit(self, other_card):
        # TODO-1: метод возвращает True - если масти карт равны или False - если нет
        return self.suit == other_card.suit


class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.cards = []
        # TODO-1: конструктор добавляет в список self.cards все(52) карты
        self.cards = [Card(value=value, suit=suit) for value in values for suit in suits]

    def show(self):
        return f"cards[{len(self.cards)}]{', '.join([card.to_str() for card in self.cards])}"

    def draw(self, x):
        # TODO-1: Принцип работы данного метода прописан в 00_task_deck.md
        self.x = x
        x_list = []
        for card in self.cards[:x]:
            x_list.append(card.to_str())
            self.cards.remove(card)
        return x_list

    def shuffle(self):
        random.shuffle(self.cards)


# Создаем колоду
deck = Deck()
# Выводим колоду в формате указанном в основном задании
print(deck.show())
# Тусуем колоду
deck.shuffle()
print(deck.show())

# Возьмем 5 карт "в руку"
hand = deck.draw(5)
# Выводим колоду, чтобы убедиться что 5 верхних карт отсутствуют
print(deck.show())
# Выводим список карт "в руке"(список hand)
print(f"cards {', '.join([card for card in hand])}")
print(f"cards[{len(hand)}]{', '.join([card for card in hand])}")
