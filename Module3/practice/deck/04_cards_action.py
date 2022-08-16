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



values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
cards = [Card(value, suit) for suit in suits for value in values]

print(f"cards[{len(cards)}]: ", end = '')
print(*[card.to_str() for card in cards], sep = ', ')

# TODO-2: Выведите карты в формате: cards[кол-во]2♥, 3♥, 4♥ ... A♥, 2♦, 3♦ ... A♦, ...
#  кол-во берем от размера списка cards
