class Card:
    # TODO-0: сюда копируем реализацию класса карты из предыдущего задания
    ...
def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        suit_icon = {
            'Hearts': '\u2665',
            'Diamonds': '\u2666',
            'Clubs': '\u2663',
            'Spades': '\u2660'
        }
        return f"{self.value}{suit_icon[self.suit]}"

    def equal_suit(self, other_card):
        return self.suit == other_card.suit

class Deck:
    d suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.cards = []
        # TODO-1: конструктор добавляет в список self.cards все(52) карты
        for suit in suits:
            for value in values:
                self.cards.append(Card(value,suit))

    def show(self):
        # TODO-2: Принцип работы данного метода прописан в 00_task_deck.md
        ...
        cards_str = []
        for card in self.cards:
            cards_str.append(card.to_str())
        return f'cards[{len(self.cards)}]' + ', '.join(cards_str)

# Создаем колоду
deck = Deck()
# Выводим колоду в формате указанном в основном задании
print(deck.show())
