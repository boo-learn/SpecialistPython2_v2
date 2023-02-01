class Card:
    # TODO-0: сюда копируем реализацию класса карты из предыдущего задания
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        suit_icons = {
            "Hearts": "\u2665",
            "Diamonds": "\u2666",
            "Clubs": "\u2663",
            "Spades": "\u2660"
        }
        return f"{self.value}{suit_icons[self.suit]}"


class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.cards = []
        # TODO-1: конструктор добавляет в список self.cards все(52) карты

        for suit in suits:
            for val in values:
                self.cards.append(Card(val, suit))

    def show(self):
        # TODO-2: Принцип работы данного метода прописан в 00_task_deck.md
        str_cards = []
        for card in self.cards:
            str_cards.append(card.to_str())

        return f"cards[{len(self.cards)}]" + ", ".join(str_cards)


# Создаем колоду
deck = Deck()
# Выводим колоду в формате указанном в основном задании
print(deck.show())
