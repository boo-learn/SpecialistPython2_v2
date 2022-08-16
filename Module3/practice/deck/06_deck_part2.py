import random

class Card:
    DIAMONDS = 'Diamonds'
    HEARTS = 'Hearts'
    SPADES = 'Spades'
    CLUBS = 'Clubs'
        
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        suits = { 
            Card.DIAMONDS : '\u2666',
            Card.HEARTS : '\u2665',
            Card.SPADES : '\u2660',
            Card.CLUBS : '\u2663'
            }
        return self.value + suits[self.suit]

    def equal_suit(self, other_card):
        if self.suit == other_card.suit:
            return True
        else:
            return False

class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.cards = [Card(value, suit) for suit in suits for value in values]

    def show(self):
        print(f"Deck[{len(self.cards)}]: ", end = '')
        print(*[card.to_str() for card in self.cards], sep = ', ')

    def draw(self, x):
        drawed_cards = self.cards[:x]
        self.cards = self.cards[x:]
        return drawed_cards

    def shuffle(self):
        random.shuffle(self.cards)



# Создаем колоду
deck = Deck()
# Выводим колоду в формате указанном в основном задании
deck.show()
# Тусуем колоду
deck.shuffle()
deck.show()

# Возьмем 5 карт "в руку"
hand = deck.draw(5)
# Выводим колоду, чтобы убедиться что 5 верхних карт отсутствуют
deck.show()
# Выводим список карт "в руке"(список hand)
print(f"hand[{len(hand)}]:" + ' '.join([card.to_str() for card in hand]))
