class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        symbols = {
            "Spades": "\u2660",
            "Hearts": "\u2665",
            "Diamonds": "\u2666",
            "Clubs": "\u2663"
        }
        return f"{self.value}{symbols[self.suit]}"

    def equal_suit(self, other_card):
        return self.suit == other_card.suit


values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']     # Список значений карт
suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']       # Список мастей карт


# Задание: Теперь создадим колоду из 52-ух карт и реализуем все методы
class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']  # Список значений карт
        suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']  # Список мастей карт
        self.cards = []
        for value in values:
            for suit in suits:
                self.cards.append(Card(value, suit))

    def show(self):
        # Принцип работы данного метода прописан в 00_task_deck.md
        cards_str = ', '.join([card.to_str() for card in self.cards])
        return f"cards[{len(self.cards)}] {cards_str}"

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
