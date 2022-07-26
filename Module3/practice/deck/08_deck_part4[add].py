import random


class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты
        self.suit_rang = {"Hearts": 3, "Diamonds": 2, "Spades": 0, "Clubs": 1}
        self.value_rang = {"2": 0, "3": 1, "4": 2, "5": 3, "6": 4, "7": 5, "8": 6, "9": 7, "10": 8, "J": 9, "Q": 10,
                           "K": 11, "A": 12}

    def to_str(self):
        suit_to_pic = {"Hearts": '\u2665', "Diamonds": '\u2666', "Spades": '\u2664', "Clubs": '\u2667'}
        return f"{self.value}{suit_to_pic[self.suit]}"

    def equal_suit(self, other_card):
        return self.suit == other_card.suit

    def equal_value(self, other_card):
        return self.value == other_card.value

    def more(self, other_card):
        if self.equal_value(other_card):
            return self.suit_rang[self.suit] > self.suit_rang[other_card.suit]
        else:
            return self.value_rang[self.value] > self.value_rang[other_card.value]

    def less(self, other_card):
        if self.equal_value(other_card):
            return self.suit_rang[self.suit] < self.suit_rang[other_card.suit]
        else:
            return self.value_rang[self.value] < self.value_rang[other_card.value]


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
        return f"deck[{len(self.cards)}]:{', '.join([card.to_str() for card in self.cards])}"

    def draw(self, x):
        result = []
        for _ in range(x):
            result.append(self.cards.pop(0))
        return result

    def shuffle(self):
        random.shuffle(self.cards)

    def shift(self, num_card):
        self.cards.extend(self.draw(num_card))


# Создаем колоду
deck = Deck()
# Тусуем колоду
deck.shuffle()
print(deck.show())
# Сдвигаем 10 карт
deck.shift(10)
print(deck.show())
