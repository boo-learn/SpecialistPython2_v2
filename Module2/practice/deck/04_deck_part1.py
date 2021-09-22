class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        symbols = {
            'Hearts': '\u2665',
            'Diamonds': '\u2666',
            'Clubs': '\u2663',
            'Spades': '\u2660'
        }
        return f'{self.value}{symbols[self.suit]}'

    def equal_suit(self, other_card):  # проверяет, одинаковые ли масти у карт
        return self.suit == other_card.suit

# Задание: Теперь создадим колоду из 52-ух карт и реализуем все методы
class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        self.cards = []
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        for suit in suits:
            for value in values:
                card = Card(value, suit)
                self.cards.append(card)

    def show(self):
        # Принцип работы данного метода прописан в 00_task_deck.md отображает все карты колоды в формате:
        # deck[12]: 3♥, 4♦, A♣, …
        cards_str = ", ".join([card.to_str() for card in self.cards])
        return f'deck[{len(self.cards)}]{cards_str}'
    
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
