Моё решение:
class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def to_str(self):
        suit_d = {"Hearts": '\u2665', "Diamonds": '\u2666', "Spades": '\u2663', "Clubs": '\u2660'}
        return f"{self.value}{suit_d[self.suit]}"

    def equal_suit(self, other_card):
        return self.suit == other_card.suit


class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.cards = []
        for suit_card in suits:
            for value_card in values:
                card = Card(value_card, suit_card)
                self.cards.append(card)

    def show(self):
        in_deck = []
        for card in self.cards:
            in_deck.append(f'{card.to_str()}')
        return f"deck[{len(self.cards)}]: {', '.join(in_deck)}"



# Создаем колоду
deck = Deck()
# Выводим колоду в формате указанном в основном задании
print(deck.show())
