class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        # TODO-1: метод возвращает строковое представление карты в виде: 10♥ и A♦
        suits_dct = {
            "Diamonds": '\u2666',
            "Hearts": '\u2665',
            "Spades": '\u2664',
            "Clubs": '\u2667'
        }
        return self.value+suits_dct[self.suit]

    def equal_suit(self, other_card):
        # TODO-1: метод возвращает True - если масти карт равны или False - если нет
        if self.suit == other_card.suit:
            return True
        else:
            return False

values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
hearts_cards = []
# TODO-1: добавьте в список hearts_cards все червовые карты(от 2-ки до туза)
for value in values:
    cards = Card(value, "Hearts")
    hearts_cards.append(cards)

diamonds_cards = []
# TODO-2: добавьте в список diamonds_cards все бубновые карты(от туза до 2-ки)
for value in values:
    cards = Card(value, "Hearts")
    diamonds_cards.insert(0, cards.to_str())

# TODO-3: выведите все карты из списка hearts_cards в терминал через запятую в одну строку:
# Пример вывода: 2♥, 3♥, 4♥ ... A♥
for hearts_card in hearts_cards:
    print(hearts_card.to_str(), end=" ")

cards = [
    Card("2", "Hearts"),
    Card("3", "Hearts"),
    Card("4", "Hearts"),
    ...]
