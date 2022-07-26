# Начнем с создания карты
class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты
        self.__suits = {"Hearts": "\u2665", "Diamonds": "\u2666", "Spades": "\u2660", "Clubs": "\u2663"}

    def to_str(self):
        return f"{self.value}{self.__suits.get(self.suit)}"

    def equal_suit(self, other_card):
        return self.suit == other_card.suit


values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

hearts_cards = []
for value in values:
    hearts_cards.append(Card(value, "Hearts"))
# TODO-1: добавьте в список hearts_cards все червовые карты(от 2-ки до туза)

diamonds_cards = []
for value in reversed(values):
    diamonds_cards.append(Card(value, "Diamonds"))
# TODO-2: добавьте в список diamonds_cards все бубновые карты(от туза до 2-ки)

# TODO-3: выведите все карты из списка hearts_cards в терминал через запятую в одну строку:
for i in hearts_cards:
    print(i.to_str(), end=',')
