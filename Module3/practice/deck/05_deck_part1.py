class Card:
    def __init__(self, value: str, suit: str):
        self.value = value
        self.suit = suit

    def to_str(self):
        suit_pic = {"Hearts": "\u2665", "Diamonds": "\u2666", "Clubs": "\u2663", "Spades": "\u2660"}
        return f"{self.value}{suit_pic.get(self.suit)}"

    def equal_suit(self, other):
        return self.suit == other.suit


class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        self.cards = []

        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        for st in suits:
            suit_cards = [Card(value, st) for value in values]
            self.cards.extend(suit_cards)

    def show(self):
        return f"deck[{len(self.cards)}]: {', '.join([card.to_str() for card in self.cards])}"


# Создаем колоду
deck = Deck()
# Выводим колоду в формате указанном в основном задании
print(deck.show())
