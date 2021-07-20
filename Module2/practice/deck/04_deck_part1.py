import random
# Начнем с создания карты
class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        icons = {'Hearts': '\u2665', 'Diamonds': '\u2666', 'Clubs': '\u2663', 'Spades': '\u2660'}
        return f'{self.value}{icons[self.suit]}'

    def equal_suit(self, other_card):
        return self.suit == other_card.suit
# Задание: Теперь создадим колоду из 52-ух карт и реализуем все методы

class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        values = [char for char in range(2, 11)] + ['J', 'Q', 'K', 'A']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.cards = []
        for suit in suits:
            for value in values:
                card = Card(value, suit)
                self.cards.append(card)

    def show(self):
        # Принцип работы данного метода прописан в 00_task_deck.md
        cards_str = f'deck[{len(self.cards)}]{self.cards[0].to_str()}'
        for card in self.cards[1:]:
            cards_str += ', ' + card.to_str()
        return cards_str

    def draw(self, x):
        hand = self.cards[:x]
        self.cards = self.cards[x:]
        return hand
        # Принцип работы данного метода прописан в 00_task_deck.md

    def shuffle(self):
        # Обратите внимание на: https://www.w3schools.com/python/ref_random_shuffle.asp
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
