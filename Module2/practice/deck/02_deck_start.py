class Card:
    DIAMONDS = "Diamonds"
    SPADES = "Spades"
    HEARTS = "Hearts"
    CLUBS = "Clubs"
    suits_symbols = {DIAMONDS: '\u2665',
                     SPADES: '\u2666',
                     HEARTS: '\u2663',
                     CLUBS: '\u2660'}


    def __init__(self, value, type):
        self.value = value
        self.type = type

    def to_str(self):
        return f"{self.value} {Card.suits_symbols[self.type]}"
