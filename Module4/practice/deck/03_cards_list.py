class Card:
    # TODO-0: сюда копируем реализацию класса карты из предыдущего задания
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def __str__(self):
        suit_icon = {
            'Diamonds': '\u2666',
            'Hearts':   '\u2665',
            'Spades':   '\u2664',
            'Clubs':    '\u2667'
        }
        return f'{self.value}{suit_icon[self.suit]}'

    def equal_suit(self, other_card):
        return self.suit == other_card.suit


values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
hearts_cards = []
# TODO-1: добавьте в список hearts_cards все червовые карты(от 2-ки до туза)
for value in values:
    hearts_cards.append(Card(value, 'Hearts'))

diamonds_cards = []
# TODO-2: добавьте в список diamonds_cards все бубновые карты(от туза до 2-ки)
for value in values[::-1]:
    diamonds_cards.append(Card(value, 'Diamonds'))

# TODO-3: выведите все карты из списка hearts_cards в терминал через запятую в одну строку:
# Пример вывода: 2♥, 3♥, 4♥ ... A♥
print(', '.join(map(str, hearts_cards)))
