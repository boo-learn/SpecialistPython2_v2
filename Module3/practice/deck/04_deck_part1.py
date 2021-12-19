class Card:
    pass
    # TODO: сюда копируем реализацию класса карты из предыдущего задания


# Задание: Теперь создадим колоду из 52-ух карт и реализуем все методы
class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        self.cards = []

    def show(self):
        # Принцип работы данного метода прописан в 00_task_deck.md
        pass

    def draw(self, x):
        # Принцип работы данного метода прописан в 00_task_deck.md
        pass

    def shuffle(self):
        # Обратите внимание на: https://www.w3schools.com/python/ref_random_shuffle.asp
        pass


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
