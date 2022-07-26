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

class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.cards = []
        for suit in suits:
            for value in values:
                self.cards.append(Card(value, suit))
        # TODO-1: конструктор добавляет в список self.cards все(52) карты

    def show(self):
        print(f"cards[{len(self.cards)}] ", end="")
        for card in self.cards:
            print(card.to_str(), end=",")

# Создаем колоду
deck = Deck()
# Выводим колоду в формате указанном в основном задании
print(deck.show())
