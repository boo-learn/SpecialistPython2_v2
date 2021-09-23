import random
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

    #реализуем новые методы
    def more(self, other_card): #возвращает True, если карта у которой вызван метод больше, чем карта которую передали в качестве параметра
        # При равенстве значений, сравниваем масти
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
        return (values.index(self.value) > values.index(other_card.value)) or \
               (values.index(self.value) == values.index(other_card.value) and suits.index(self.suit) > suits.index(other_card.suit))

    def less(self, other_card): #проверяет является ли карта младше, чем карта в параметре
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
        return (values.index(self.value) < values.index(other_card.value)) or \
               (values.index(self.value) == values.index(other_card.value) and suits.index(self.suit) < suits.index(other_card.suit))

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
        # возвращает x первых карт из колоды в виде списка, эти карты убираются из колоды.
        # Уточнение: первую карту в списке считаем верхней картой колоды
        '''срезы'''
        cards = []
        for _ in range(x):
            card = self.cards.pop(0)
            cards.append(card)
        return cards

    def shuffle(self):
        # Обратите внимание на: https://www.w3schools.com/python/ref_random_shuffle.asp
        # перемешивает колоду, располагая карты в случайном порядке.
        random.shuffle(self.cards)

# Создаем колоду
deck = Deck()
deck.shuffle()
print(deck.show())
# Берем две карты из колоды
card1, card2 = deck.draw(2)

# Тестируем методы .less() и .more()
if card1.more(card2):
    print(f"{card1.to_str()} больше {card2.to_str()}")
if card1.less(card2):
    print(f"{card1.to_str()} меньше {card2.to_str()}")
