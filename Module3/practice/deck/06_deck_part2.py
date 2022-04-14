import random

class Card:
    # TODO-0: сюда копируем реализацию класса карты из предыдущего задания
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        suit_d = {"Hearts": '\u2665', "Diamonds": '\u2666', "Spades": '\u2663', "Clubs": '\u2660'}
        return f"{self.value}{suit_d[self.suit]}"

    def equal_suit(self, other_card):
        return self.suit == other_card.suit

class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.cards = []
        # TODO-0: конструктор копируем из предыдущей задачи
        for suit in suits:
            for value in values:
                self.cards.append(Card(value, suit))

    def show(self):
        # TODO-0: копируем из предыдущей задачи
        cards_str = []
        for card in self.cards:
            cards_str.append(card.to_str())
        return f"Cards [{len(cards_str)}]: {', '.join(cards_str)}"

    def draw(self, x):
        # TODO-1: Принцип работы данного метода прописан в 00_task_deck.md
        cards_del = []
        for i in range(x):
            card_del = self.cards.pop(0)
            cards_del.append(card_del.to_str())
        return cards_del


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

# Возьмем 5 карт "в руку"
hand = deck.draw(5)
# Выводим колоду, чтобы убедиться что 5 верхних карт отсутствуют
print(deck.show())
# Выводим список карт "в руке"(список hand)
print(hand)
