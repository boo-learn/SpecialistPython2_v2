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


values = [char for char in range(2, 11)] + ['J', 'Q', 'K', 'A']
hearts_cards = [Card(value, 'Hearts') for value in values]
diamond_cards = [Card(value, 'Diamonds') for value in values]
for card in hearts_cards:
    print(card.to_str(), end=", ")


