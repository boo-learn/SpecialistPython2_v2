class Card:
        def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты
    def to_str(self):
        # Символы для отображения мастей
        suit_symbols = {"Hearts": "\u2665", "Diamonds": "\u2666",
                        "Clubs": "\u2663", "Spades": "\u2660"}
        # Строковое представление карты вида "значение масть"
        return self.value + suit_symbols[self.suit]
    def equal_suit(self, other_card):
        return self.suit == other_card.suit


values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
hearts_cards = []
for value in values:
    card = Card(value, "Hearts")
    hearts_cards.append(card)
diamonds_cards = []
for value in reversed(values):
    card = Card(value, "Diamonds")
cards_str = ", ".join([card.to_str() for card in hearts_cards])
print(cards_str)


cards = [
    Card("2", "Hearts"),
    Card("3", "Hearts"),
    Card("4", "Hearts"),
    ...]
