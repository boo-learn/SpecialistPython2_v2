class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        dict_1 = {"Hearts": '\u2665', "Diamonds": '\u2666', "Clubs": '\u2663', "Spades": '\u2660'}
        return f"{self.value}{dict_1[self.suit]}"

    def equal_suit(self, other_card):
        return self.suit == other_card.suit


values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
hearts_cards = []

# TODO-1: добавьте в список hearts_cards все червовые карты(от 2-ки до туза)
for value in values:
    hearts_cards.append(Card(value, "Hearts"))

diamonds_cards = []
# TODO-2: добавьте в список diamonds_cards все бубновые карты(от туза до 2-ки)
for value in values:
    diamonds_cards.append((value, "Diamonds"))

# TODO-3: выведите все карты из списка hearts_cards в терминал через запятую в одну строку:
# Пример вывода: 2♥, 3♥, 4♥ ... A♥

for card in hearts_cards:
    print(f"{card.to_str()}", end=(', '))

cards = [
    Card("2", "Hearts"),
    Card("3", "Hearts"),
    Card("4", "Hearts"),
    ...]
