class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        dict_symb = {'Diamonds': '\u2666', 'Hearts': '\u2665', 'Spades': '\u2660', 'Clubs': '\u2663'}
        return f'{self.value}{dict_symb.get(self.suit)}'

    def equal_suit(self, other_card):
        if self.to_str() == other_card.to_str():
            return True
        else:
            return False
