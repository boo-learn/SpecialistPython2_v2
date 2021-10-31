class Card:              #сюда копируем реализацию класса карты из предыдущего задания
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        icon_suits = {'Hearts': '\u2661', 'Diamonds': '\u2662', 'Clubs': '\u2667', 'Spades': '\u2664'}
        return f'{self.value}{icon_suits[self.suit]}'




values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
cards = []

hearts_cards = []
for value in values:
    card = Card(value, 'Hearts')
    hearts_cards.append(card)
    cards.append(card)

diamonds_cards = []
for value in values:
    card = Card(value, 'Diamonds')
    diamonds_cards.append(card)
    cards.append(card)

clubs_cards = []
for value in values:
    card = Card(value, 'Clubs')
    clubs_cards.append(card)
    cards.append(card)

spades_cards = []
for value in values:
    card = Card(value, 'Spades')
    spades_cards.append(card)
    cards.append(card)

cards_str = ''
for card in cards:
    cards_str += card.to_str() + ','

print(f"Кол-во карт:{len(cards)}", cards_str)
