# Начнем с создания карты
import random
class Card:
    def __init__(self, value: str, suit: str):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self) -> str:
        # TODO-1: метод возвращает строковое представление карты в виде: 10♥ и A♦
        if self.suit == "Hearts":
            icon = "\u2665"
        elif self.suit == "Diamonds":
            icon = "\u2666"
        elif self.suit == "Clubs":
            icon = "\u2663"
        elif self.suit == "Spades":
            icon = "\u2660"
        return f"{self.value}{icon}"

    def equal_suit(self, other_card: "Card") -> bool:
        # TODO-1: метод возвращает True - если масти карт равны или False - если нет
        return self.suit == other_card.suit


class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        values = ['2', '3', '4', '5', '6', '7',
                  '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.cards = []
        for suit in suits:
            for value in values:
                self.cards.append(Card(value, suit))

    def show(self) -> str:
        list_str_cards = []
        for card in self.cards:
            list_str_cards.append(card.to_str())
        return f"Deck: [{len(self.cards)}]" + ", ".join(list_str_cards)


# TODO-1: в список cards добавьте ВСЕ карты всех мастей

    def draw(self, x) -> list:
        # TODO-1: Принцип работы данного метода прописан в 00_task_deck.md
        out = self.cards[:x]
        del self.cards[:x]
        return out

    def shuffle(self) -> None:
        # TODO-2: Принцип работы данного метода прописан в 00_task_deck.md
        #   Подсказка: https://www.w3schools.com/python/ref_random_shuffle.asp
        random.shuffle(self.cards)
       


# Создаем колоду
deck = Deck()
# Выводим колоду в формате указанном в основном задании
print(deck.show())
# Тусуем колоду
deck.shuffle()
print("----------------------------------------")
print(deck.show())
# Возьмем 5 карт "в руку"
hand = deck.draw(5)
print("----------------------------------------")
# Выводим колоду, чтобы убедиться что 5 верхних карт отсутствуют
print(deck.show())
print("----------------------------------------")
# Выводим список карт "в руке"(список hand)
# print(...)
hand_to_show = []
for card in hand:
    hand_to_show.append(card.to_str())

print(f"Hand: [{len(hand)}]", ", ".join(hand_to_show))
