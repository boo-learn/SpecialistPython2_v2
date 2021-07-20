class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    # Выводит значение в юникод формате
    def to_str(self):
        icons = {'Hearts': '\u2665',
                'Diamonds': '\u2666',
                'Clubs': '\u2663',
                'Spades': '\u2660'}
        return f'{self.value}{icons[self.suit]}'

    def equal_suit(self, other_card):
        return other_card.suit == self.suit

list_of_cards_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
list_of_suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
cards = [Card(values, suit=suits) for suits in list_of_suits for values in list_of_cards_values]
# TODO-1: в список cards добавьте ВСЕ карты всех мастей

# TODO-2: Выведите карты в формате: cards[кол-во]2♥, 3♥, 4♥ ... A♥, 2♦, 3♦ ... A♦, ....
# result = f'cards[{str(len(cards))}]'
# for card in cards:
#     if card == cards[0]:
#         result += card.to_str()
#     else:
#         result += ', ' + card.to_str()

list_of_cards = []
for card in cards:
    list_of_cards.append(card.to_str())

print(f'{result}', end='')
print(*list_of_cards, sep=', ')
