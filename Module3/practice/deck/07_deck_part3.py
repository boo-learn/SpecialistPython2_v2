import random


class Card:
    def __init__(self, value: str, suit: str):
        self.value = value
        self.suit = suit

    def to_str(self):
        suit_pic = {"Hearts": "\u2665", "Diamonds": "\u2666", "Clubs": "\u2663", "Spades": "\u2660"}
        return f"{self.value}{suit_pic.get(self.suit)}"

    def equal_suit(self, other):
        return self.suit == other.suit

    def more(self, other_card):
        symbol_values = {"J": 11, "Q": 12, "K": 13, "A": 14}
        this_value = symbol_values.get(self.value) or int(self.value)
        other_value = symbol_values.get(other_card.value) or int(other_card.value)

        # Если значения не равны, значит сравниваем по значению
        if this_value != other_value:
            return this_value > other_value

        # Здесь значения равны, значит сравниваем масти
        suits_values = {"Spades": 1, "Clubs": 2, "Diamonds": 3, "Hearts": 4}
        this_suit_value = suits_values.get(self.suit)
        other_suit_value = suits_values.get(other_card.suit)

        return this_suit_value > other_suit_value

    def less(self, other_card):
        return not self.more(other_card)


class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        self.cards = []

        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        for st in suits:
            suit_cards = [Card(value, st) for value in values]
            self.cards.extend(suit_cards)

    def show(self):
        return f"deck[{len(self.cards)}]: {', '.join([card.to_str() for card in self.cards])}"

    def draw(self, x):
        if x > len(self.cards):
            raise ValueError("Нельзя взять в руку больше карт, чем осталось в колоде")

        return [self.cards.pop(i) for i in range(x)]

    def shuffle(self):
        random.shuffle(self.cards)


# Создаем колоду
deck = Deck()
# Тусуем колоду
deck.shuffle()
print(deck.show())
# Берем две карты из колоды
card1, card2 = deck.draw(2)

# Тестируем методы .less() и .more()
if card1.more(card2):
    print(f"{card1.to_str()} больше {card2.to_str()}")

if card1.less(card2):
    print(f"{card1.to_str()} меньше {card2.to_str()}")
