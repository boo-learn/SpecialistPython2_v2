class Card:
        def __init__(self, value, suit):
            self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
            self.suit = suit  # Масть карты
        def to_str(self):
            suit_d = {"Hearts": '\u2665', "Diamonds": '\u2666', "Spades": '\u2663', "Clubs": '\u2660'}
            return (f"{self.value}{suit_d[self.suit]}")

values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
hearts_cards = []
for card in values:
    card = Card(card, "Hearts")
    hearts_cards.append(card.to_str())
print(hearts_cards)
# TODO-1: добавьте в список hearts_cards все червовые карты(от 2-ки до туза)

diamonds_cards = []
for card in values:
    card = Card(card, "Diamonds")
    diamonds_cards.append(card.to_str())
print(diamonds_cards)

# TODO-2: добавьте в список diamonds_cards все бубновые карты(от туза до 2-ки)

# TODO-3: выведите все карты из списка hearts_cards в терминал через запятую в одну строку:
# Пример вывода: 2♥, 3♥, 4♥ ... A♥


cards = [
    Card("2", "Hearts"),
    Card("3", "Hearts"),
    Card("4", "Hearts"),
    ...]
