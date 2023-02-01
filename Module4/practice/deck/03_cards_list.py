class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        # TODO-1: метод возвращает строковое представление карты в виде: 10♥ и A♦
        if self.suit == 'Hearts':
            self.suit_new = '\u2661'
        elif self.suit == 'Diamonds':
            self.suit_new = '\u2662'
        elif self.suit == 'Spades':
            self.suit_new = '\u2664'
        elif self.suit == 'Clubs':
            self.suit_new = '\u2667'
        return self.value + self.suit_new

    def equal_suit(self, other_card):
        if self.suit == other_card.suit:
            return True
        else:
            return False


values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
hearts_cards = []
# TODO-1: добавьте в список hearts_cards все червовые карты(от 2-ки до туза)
for val in values:
    hearts_cards.append(Card(val, 'Hearts'))


diamonds_cards = []
# TODO-2: добавьте в список diamonds_cards все бубновые карты(от туза до 2-ки)
for val in values[::-1]:
    diamonds_cards.append(Card(val, 'Diamonds'))

# TODO-3: выведите все карты из списка hearts_cards в терминал через запятую в одну строку:
# Пример вывода: 2♥, 3♥, 4♥ ... A♥
for card in hearts_cards:
    print(card.to_str())

cards = [
    Card("2", "Hearts"),
    Card("3", "Hearts"),
    Card("4", "Hearts"),
    ...]
