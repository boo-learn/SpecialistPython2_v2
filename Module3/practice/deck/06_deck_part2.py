class Card:
    # TODO-0: сюда копируем реализацию класса карты из предыдущего задания
    ...


class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["Hearths", "Diamonds", "Spades", "Clubs"]
        self.cards = []
        # TODO-0: конструктор копируем из предыдущей задачи

    def show(self):
        # TODO-0: копируем из предыдущей задачи
        ...

    def draw(self, x):
        # TODO-1: Принцип работы данного метода прописан в 00_task_deck.md
        ...

    def shuffle(self):
        # TODO-2: Принцип работы данного метода прописан в 00_task_deck.md
        #   Подсказка: https://www.w3schools.com/python/ref_random_shuffle.asp
        ...


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
print(...)
