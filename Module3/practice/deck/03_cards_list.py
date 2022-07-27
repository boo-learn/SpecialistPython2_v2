class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты
        self.suit_icons = {'Hearts': '\u2665', 'Diamonds': '\u2666', 'Clubs': '\u2663', 'Spades': '\u2660'}

    def to_str(self):
        # TODO-1: метод возвращает строковое представление карты в виде: 10♥ и A♦

        return f'{self.value}{self.suit_icons.get(self.suit)}'


    def equal_suit(self, other_card):
        # TODO-1: метод возвращает True - если масти карт равны или False - если нет
        return self.suit == other_card.suit


values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

# TODO-1: добавьте в список hearts_cards все червовые карты(от 2-ки до туза)
hearts_cards = []
for value in values:
    hearts_cards.append(Card(value, 'Hearts'))


# TODO-2: добавьте в список diamonds_cards все бубновые карты(от туза до 2-ки)
diamonds_cards = []
for value in values:
    diamonds_cards.append(Card(value, 'Diamonds'))

# TODO-3: выведите все карты из списка hearts_cards в терминал через запятую в одну строку:
# Пример вывода: 2♥, 3♥, 4♥ ... A♥
print(*list(card.to_str() for card in hearts_cards), sep=', ')

cards = [
    Card("2", "Hearts"),
    Card("3", "Hearts"),
    Card("4", "Hearts"),
    ...]
