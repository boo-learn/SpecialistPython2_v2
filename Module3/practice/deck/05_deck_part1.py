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

class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.cards = []
        # TODO-1: конструктор добавляет в список self.cards все(52) карты
        for value in values:
            for suit in suits:
                card = Card(value, suit)
                if card not in self.cards:
                    self.cards.append(card)

    def show(self):
        # TODO-2: Принцип работы данного метода прописан в 00_task_deck.md
        ...
        deck_cards = []
        for card in self.cards:
            card = card.to_str()
            deck_cards.append(card)
        return f'deck{[len(deck_cards)]}: {", ".join(deck_cards)}'

# Создаем колоду
deck = Deck()
# Выводим колоду в формате указанном в основном задании
print(deck.show())
