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
hearts_cards = []
diamonds_cards = []

for value in values:
    hearts_cards.append(Card(value, Card.HEARTS))
    diamonds_cards.append(Card(value, Card.DIAMONDS))

print(*[card.to_str() for card in hearts_cards], sep = ', ')
    
cards = [
    Card("2", "Hearts"),
    Card("3", "Hearts"),
    Card("4", "Hearts"),
    ...]
