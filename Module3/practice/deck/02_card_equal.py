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


# Создадим несколько карт
card1 = Card("10", Card.HEARTS)
card2 = Card("A", Card.DIAMONDS)


# Проверим, одинаковые ли масти у карт
if card1.equal_suit(card2):
    print(f"У карт: {card1.to_str()} и {card2.to_str()} одинаковые масти")
else:
    print(f"У карт: {card1.to_str()} и {card2.to_str()} разные масти")
