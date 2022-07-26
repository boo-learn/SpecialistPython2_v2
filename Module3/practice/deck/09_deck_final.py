import random


class Card:
    def __init__(self, value: str, suit: str):
        self.value = value
        self.suit = suit

    def __str__(self):
        suit_pic = {"Hearts": "\u2665", "Diamonds": "\u2666", "Clubs": "\u2663", "Spades": "\u2660"}
        return f"{self.value}{suit_pic.get(self.suit)}"

    def equal_suit(self, other):
        return self.suit == other.suit

    def __gt__(self, other):
        symbol_values = {"J": 11, "Q": 12, "K": 13, "A": 14}
        this_value = symbol_values.get(self.value) or int(self.value)
        other_value = symbol_values.get(other.value) or int(other.value)

        # Если значения не равны, значит сравниваем по значению
        if this_value != other_value:
            return this_value > other_value

        # Здесь значения равны, значит сравниваем масти
        suits_values = {"Spades": 1, "Clubs": 2, "Diamonds": 3, "Hearts": 4}
        this_suit_value = suits_values.get(self.suit)
        other_suit_value = suits_values.get(other.suit)

        return this_suit_value > other_suit_value

    def __lt__(self, other):
        return not self > other


class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        self.cards = []

        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        for st in suits:
            suit_cards = [Card(value, st) for value in values]
            self.cards.extend(suit_cards)

    def __str__(self):
        return f"deck[{len(self.cards)}]: {', '.join([str(card) for card in self.cards])}"

    def __iter__(self):
        return iter(self.cards)

    def __getitem__(self, item):
        return self.cards[item]

    def draw(self, x):
        if x > len(self.cards):
            raise ValueError("Нельзя взять в руку больше карт, чем осталось в колоде")

        return [self.cards.pop(0) for _ in range(x)]

    def shuffle(self):
        random.shuffle(self.cards)

    def shift(self, num_card):
        self.cards.extend([self.cards.pop(0) for _ in range(num_card)])


deck = Deck()
# 1. Вывод колоды в терминал:
print(deck)  # вместо print(deck.show())

card1, card2 = deck.draw(2)
# 2. Вывод карты в терминал:
print(card1)  # вместо print(card1.to_str())

# 3. Сравнение карт:
if card1 > card2:
    print(f"{card1} больше {card2}")

if card1 < card2:
    print(f"{card1} меньше {card2}")

# 4. Итерация по колоде:
for crd in deck:
    print(crd)

# 5. Просмотр карты в колоде по ее индексу:
print(deck[6])
