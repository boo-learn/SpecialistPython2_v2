# Начнем с создания карты
class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        if self.suit == "Hearts"  : g_suit = '\u2665'
        if self.suit == "Diamonds": g_suit = '\u2666'
        if self.suit == "Clubs"   : g_suit = '\u2663'
        if self.suit == "Spades"  : g_suit = '\u2660'
        return f"{self.value}{g_suit}"
        # TODO-1: метод возвращает строковое представление карты в виде: 10♥ и A♦
        ...

    def equal_suit(self, other_card):
        return self.suit == other_card.suit
        # TODO-1: метод возвращает True - если масти карт равны или False - если нет
        ...

class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.cards = []
        # TODO-1: конструктор добавляет в список self.cards все(52) карты
        for value in values:
            for c_suit in suits:
                card = Card(value, c_suit)
                self.cards.append(card.to_str())

    def show(self):
        c_list = ", ".join(self.cards)
        return f"cards {len(self.cards)}, { c_list}"
        # TODO-2: Принцип работы данного метода прописан в 00_task_deck.md
        ...

# Создаем колоду
deck = Deck()
# Выводим колоду в формате указанном в основном задании
print(deck.show())
