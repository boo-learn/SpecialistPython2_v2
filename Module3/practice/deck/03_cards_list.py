class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        suits = {
            "Diamonds": "\u2666",
            "Clubs": "\u2663",
            "Hearts": "\u2665",
            "Spades": "\u2660"}
        return f"{self.value}{suits.get(self.suit)}"

    def equal_suit(self, other_card):
        return self.suit == other_card.suit

values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
hearts_cards = []
# TODO-1: добавьте в список hearts_cards все червовые карты(от 2-ки до туза)
for value in values:
    card = Card(value, "Hearts")
    card = card.to_str()
    hearts_cards.append(card)

print(hearts_cards)

diamonds_cards = []
# TODO-2: добавьте в список diamonds_cards все бубновые карты(от туза до 2-ки)
for value in values:
    card = Card(value, "Diamonds")
    card = card.to_str()
    diamonds_cards.append(card)
diamonds_cards.reverse()
print(diamonds_cards)

# TODO-3: выведите все карты из списка hearts_cards в терминал через запятую в одну строку:
# Пример вывода: 2♥, 3♥, 4♥ ... A♥

print(hearts_cards, sep=", ")
# cards = [
#     Card("2", "Hearts"),
#     Card("3", "Hearts"),
#     Card("4", "Hearts"),
#     ...]
