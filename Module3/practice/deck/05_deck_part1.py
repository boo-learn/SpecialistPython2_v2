# Начнем с создания карты
class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты
        self.suit_dict = {"Hearts": '\u2665', "Diamonds": '\u2666', "Spades": '\u2660', "Clubs": '\u2663'}

    def to_str(self):
        return f"{self.value}{self.suit_dict[self.suit]}"

    def equal_suit(self, other_card):
        return self.suit == other_card.suit

class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]

        # TODO-1: конструктор добавляет в список self.cards все(52) карты
        self.cards = [Card(val, suit_val) for suit_val in suits for val in values]


    def show(self):
        # TODO-2: Принцип работы данного метода прописан в 00_task_deck.md
        #print(f"cards[{len(self.cards)}]", ','.join([card.to_str() for card in self.cards]))
        print(','.join([card.to_str() for card in self.cards]))

# Создаем колоду
deck = Deck()
# Выводим колоду в формате указанном в основном задании
deck.show()
