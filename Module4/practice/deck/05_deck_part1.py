class Card:
    # TODO-0: сюда копируем реализацию класса карты из предыдущего задания
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self) -> str:
        sign = self.suit.replace("Hearts", '\u2661').replace("Diamonds", '\u2662').replace("Spades", '\u2660').replace("Clubs", '\u2663')
        return f"{self.value} {sign}"

    def equal_suit(self, other_card) -> bool:
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
                self.cards.append(card)


    def show(self) -> str:
        # TODO-2: Принцип работы данного метода прописан в 00_task_deck.md
        str = ''
        for card in self.cards:
            str = str + card.to_str() + ', '
        return f"deck[{len(self.cards)}]: {str[:-2]}"



# Создаем колоду
deck = Deck()
# Выводим колоду в формате указанном в основном задании
print(deck.show())
