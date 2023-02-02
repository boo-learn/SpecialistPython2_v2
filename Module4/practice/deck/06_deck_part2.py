import random

class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        suit_icons = {
            "Hearts": "\u2661",
            "Diamonds": "\u2662",
            "Spades": "\u2664",
            "Clubs": "\u2667"
        }
        return f"{self.value}{suit_icons[self.suit]}"

    def equal_suit(self, other_card):
        return self.suit == other_card.suit


class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.cards = []
        for suit in suits:
            for val in values:
                self.cards.append(Card(val, suit))

    def show(self):
        cards_list = []
        for card in self.cards:
            cards_list.append(card.to_str())
        return str(f"deck[{len(cards_list)}]" + ",".join(cards_list))

    def draw(self, x):
        for i in range(x):
            self.cards.pop(len(self.cards)-1)


    def shuffle(self):
        random.shuffle(self.cards)
        # TODO-2: Принцип работы данного метода прописан в 00_task_deck.md
        #   Подсказка: https://www.w3schools.com/python/ref_random_shuffle.asp
        ...


# Создаем колоду
deck = Deck()
# Выводим колоду в формате указанном в основном задании
print(deck.show())
# Тусуем колоду
deck.shuffle()
print(deck.show())

# Возьмем 5 карт "в руку"
hand = deck.draw(5)
# Выводим колоду, чтобы убедиться что 5 верхних карт отсутствуют
print(deck.show())
# Выводим список карт "в руке"(список hand)
for card in deck.cards:
    print(card.to_str())
