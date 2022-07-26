import random


class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты
        self.suit_dict = {"Hearts": '\u2665', "Diamonds": '\u2666', "Spades": '\u2660', "Clubs": '\u2663'}

    #   self.ordered_suits = ["Hearts", "Diamonds","Clubs","Spades",]

    def to_str(self):
        return f"{self.value}{self.suit_dict[self.suit]}"

    def equal_suit(self, other_card):
        return self.suit == other_card.suit

    def more(self, other_card):
        print(Deck.suits.index(self.suit), " ", Deck.suits.index(other_card.suit))

        if self.equal_suit(other_card):
            return self.ordered_values.index(self.value) > self.ordered_values.index(other_card.value)
        else:
            return Deck.suits.index(self.suit) < Deck.suits.index(other_card.suit)

    def less(self, other_card):
        return not self.more(other_card)


class Deck:
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ["Hearts", "Diamonds", "Spades", "Clubs"]

    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card

        # TODO-1: конструктор добавляет в список self.cards все(52) карты
        self.cards = [Card(val, suit_val) for suit_val in Deck.suits for val in Deck.values]

    def show(self):
        # TODO-2: Принцип работы данного метода прописан в 00_task_deck.md

        return f"cards[{len(self.cards)}]", ','.join([card.to_str() for card in self.cards])
        # return ','.join([crd.to_str() for crd in self.cards])
        # return f"cards[{len(self.cards)}]" + ','.join([crd.to_str() for crd in self.cards])

    def draw(self, x):
        # TODO-1: Принцип работы данного метода прописан в 00_task_deck.md
        res_list = []
        for idx in range(x):
            res_list.append(self.cards.pop(0))
        return res_list

    def shuffle(self):
        random.shuffle(self.cards)

    def shift(self, num_card):
        # TODO-1: реализуем новый метод "сдвиг"
        #  Принцип работы: перемещает num_card с верха колоды под низ
        part = self.draw(num_card)
        self.cards = self.cards + part


# Создаем колоду
deck = Deck()
# Тусуем колоду
deck.shuffle()
print(deck.show())
# Сдвигаем 10 карт
deck.shift(5)
print(deck.show())
