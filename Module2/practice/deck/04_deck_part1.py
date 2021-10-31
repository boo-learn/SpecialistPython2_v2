
class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        icon_suits = {'Hearts': '\u2661', 'Diamonds': '\u2662', 'Clubs': '\u2667', 'Spades': '\u2664'}
        return f'{self.value}{icon_suits[self.suit]}'

    def equal_suit(self, other_card):
        return self.suit == other_card.suit


# Задание: Теперь создадим колоду из 52-ух карт и реализуем все методы
class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        self.cards = []

    def show(self):
        cards_str = f'deck[{len(self.cards)}]: '
        cards_str += ', '.join(card.to_str() for card in self.cards)
        return cards_str

    def draw(self, x):
        draw = 
        while x != 0:
            card = self.cards[0]
            
        pass

    def shuffle(self):
        import random
        random.shuffle(self.cards)
        return self.cards

def new_deck():
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    cards = []
    for suit in suits:
        for value in values:
            card = Card(value, suit)
            cards.append(card)
    return cards
# Создаем колоду
deck = Deck()
deck.cards = new_deck()
#print(deck.cards)

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
