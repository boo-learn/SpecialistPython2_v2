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
        if other_card.suit == self.suit:
            return True
        return False

list_of_cards_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
hearts_cards = [Card(_, suit='Hearts') for _ in list_of_cards_values]

print(hearts_cards[1].suit, hearts_cards[12].value)
# TODO-1: добавьте в список hearts_cards все червовые карты(от 2-ки до туза)

diamonds_cards = [Card(_, suit='Diamonds') for _ in reversed(list_of_cards_values)]
# TODO-2: добавьте в список diamonds_cards все бубновые карты(от туза до 2-ки)

# TODO-3: выведите все карты из списка hearts_cards в терминал через запятую в одну строку:
for _ in hearts_cards:
    print(f'{_.to_str()}', end=', ')
# Пример вывода: 2♥, 3♥, 4♥ ... A♥
