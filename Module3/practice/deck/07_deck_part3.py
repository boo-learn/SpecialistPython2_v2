import random


class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        symbols = {
            "Hearts": "\u2665",
            "Diamonds": "\u2666",
            "Spades": "\u2663",
            "Clubs": "\u2660"
        }
        return f"{self.value}{symbols[self.suit]}"

    def equal_suit(self, other_card):
        return self.suit == other_card.suit

    def more(self, other_card):
        allval = {'2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, '10': 9, 'J': 10, 'Q': 11, 'K': 12, 'A': 13}
        if allval.get(self.value) > allval.get(other_card.value):
            return True

    def less(self, other_card):

        allval = {'2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, '10': 9, 'J': 10, 'Q': 11, 'K': 12, 'A': 13}
        if allval.get(self.value) < allval.get(other_card.value):
            return True


class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.cards = []
        for suit in suits:
            for value in values:
                self.cards.append(Card(value, suit))

    def show(self):
        cards_list = []
        for card in self.cards:
            cards_list.append(card.to_str())
        print(f"cards[{len(self.cards)}]{' ,'.join(cards_list)}")

    def draw(self, x):
        # TODO-1: Принцип работы данного метода прописан в 00_task_deck.md
        take_cards = self.cards[:x]
        self.cards = self.cards[:x]
        # for i in range(x):
           # self.cards.pop(0)
        return take_cards

    def shuffle(self):
        random.shuffle(self.cards)


   # def shuffle(self):
# Создаем колоду
deck = Deck()
# Выводим колоду в формате указанном в основном задании
deck.show()
# Тусуем колоду
deck.shuffle()
deck.show()

# Возьмем 5 карт "в руку"
hand = deck.draw(5)
# Выводим колоду, чтобы убедиться что 5 верхних карт отсутствуют
deck.show()
for card in hand:
    print(card.to_str())


card1, card2 = deck.draw(2)
if card1.more(card2):
    print(f"{card1.to_str()} больше {card2.to_str()}")
if card1.less(card2):
    print(f"{card1.to_str()} меньше {card2.to_str()}")
