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

        for i in range(x):
            self.cards.pop(0)

    def shuffle(self):
        random.shuffle(self.cards)

   # def shuffle(self):
# Создаем колоду
deck = Deck()
# Выводим колоду в формате указанном в основном задании
deck.show()
deck.draw(5)
deck.show()
deck.shuffle()
deck.show()
