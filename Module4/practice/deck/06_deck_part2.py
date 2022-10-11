import random

class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        suit_icon = {
            'Hearts': '\u2665',
            'Diamonds': '\u2666',
            'Clubs': '\u2663',
            'Spades': '\u2660',
        }
        return f"{self.value}{suit_icon[self.suit]}"

    def equal_suit(self, other_card):
        return self.suit == other_card.suit

class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.cards = []
        # TODO-1: конструктор добавляет в список self.cards все(52) карты
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        for suit in suits:
            for value in values:
                self.cards.append(Card(value, suit))

    def show(self):
        # TODO-2: Принцип работы данного метода прописан в 00_task_deck.md
        ...
        cards_str = []
        for card in self.cards:
            cards_str.append(card.to_str())
        return (f'cards[{len(self.cards)}]' + ', '.join(cards_str))


    def draw(self, x):
        # TODO-1: Принцип работы данного метода прописан в 00_task_deck.md
        pack = self.cards[:x]
        del self.cards[:x]
        return pack


    def shuffle(self):
        # TODO-2: Принцип работы данного метода прописан в 00_task_deck.md
        #   Подсказка: https://www.w3schools.com/python/ref_random_shuffle.asp
        random.shuffle(self.cards)



deck1 = Deck()
print(deck1.show())
deck1.draw(2)
print(deck1.show())
deck1.shuffle()
print(deck1.show())



