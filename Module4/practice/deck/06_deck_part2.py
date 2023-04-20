from random import shuffle

class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        # TODO-1: метод возвращает строковое представление карты в виде: 10♥ и A♦
        translator = {'Hearts': '\u2665', 'Diamonds': '\u2666', 'Spades': '\u2660', 'Clubs': '\u2663'}
        return(f'{self.value}{translator.get(self.suit)}')

    def equal_suit(self, other_card) -> bool:
        # TODO-1: метод возвращает True - если масти карт равны или False - если нет
        return self.suit == other_card.suit


class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.cards = []
        # TODO-1: конструктор добавляет в список self.cards все(52) карты
        for suit in suits:
            for value in values:
                self.cards.append(Card(value=value, suit=suit))

    def show(self):
        # TODO-2: Принцип работы данного метода прописан в 00_task_deck.md
        cards_left = [card.to_str() for card in self.cards]
        return f'cards[{len(cards_left)}]: {", ".join(cards_left)}'

    def draw(self, x):
        # TODO-1: Принцип работы данного метода прописан в 00_task_deck.md
        x_cards = self.cards[:x]
        del self.cards[:x]
        return x_cards

    def shuffle(self):
        # TODO-2: Принцип работы данного метода прописан в 00_task_deck.md
        #   Подсказка: https://www.w3schools.com/python/ref_random_shuffle.asp
        shuffle(self.cards)

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
# # Выводим список карт "в руке"(список hand)
print(hand)
