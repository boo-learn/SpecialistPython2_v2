import random

class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        dict_1 = {"Hearts": '\u2665', "Diamonds": '\u2666', "Clubs": '\u2663', "Spades": '\u2660'}
        return f"{self.value}{dict_1[self.suit]}"

    def equal_suit(self, other_card):
        return self.suit == other_card.suit


class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.cards = []
        # TODO-1: конструктор добавляет в список self.cards все(52) карты
        for i in range(len(suits)):
            for value in values:
                self.cards.append(Card(value, suits[i]))

    def show(self):
        # TODO-2: Принцип работы данного метода прописан в 00_task_deck.md
        cards_str = list()

        for card in self.cards:
            cards_str.append(card.to_str())

        return (f"cards:[{len(self.cards)}] " + ", ".join(cards_str))


    def draw(self, x):
        # TODO-1: Принцип работы данного метода прописан в 00_task_deck.md
        hand=list()
        for i in range(x):
            hand.append(self.cards[i])
        for i in range(x):
            del self.cards[0]
        return hand

    def shuffle(self):
        # TODO-2: Принцип работы данного метода прописан в 00_task_deck.md
        #   Подсказка: https://www.w3schools.com/python/ref_random_shuffle.asp
        random.shuffle(self.cards)



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
cards_strinhand=list()
for card in hand:
    cards_strinhand.append(card.to_str())

print(f"карты в руке:" + ", ".join(cards_strinhand))
# print(...)
