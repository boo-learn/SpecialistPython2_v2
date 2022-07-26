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

    def __repr__(self):
        return self.to_str()

    def __gt__(self, other_card):
        return self.more(other_card)

    def __lt__(self, other_card):
        return self.less(other_card)


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

    def __repr__(self):
        return self.show()

    def __iter__(self):
        for card in self.cards:
            yield card

    def __getitem__(self, i):
        return self.cards[i]


deck = Deck()
deck.shuffle()
# TODO-final: реализовать нативную работу с объектами:
# 1. Вывод колоды в терминал:
print(deck)  # вместо print(deck.show())

card1, card2 = deck.draw(2)
# 2. Вывод карты в терминал:
print(card1, card2)  # вместо print(card1.to_str())

# 3. Сравнение карт:
if card1 > card2:
    print(f"{card1} больше {card2}")
if card1 < card2:
    print(f"{card1} меньше {card2}")

# 4. Итерация по колоде:
for card in deck:
    print(card, end=', ')
print()
# 5. Просмотр карты в колоде по ее индексу:
print(deck[6])
