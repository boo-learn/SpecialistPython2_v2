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

        if self.equal_suit(other_card):
            return Deck.values.index(self.value) > Deck.values.index(other_card.value)
        else:
            return Deck.suits.index(self.suit) < Deck.suits.index(other_card.suit)

    def less(self, other_card):
        return not self.more(other_card)

    def __cmp__(self,other):
        if  self.suit == other.suit and self.value == other.value:
            return 0

    def __lt__(self,other):
       return not self.more(other)

    def __gt__(self, other):
        return self.more(other)

    def __str__(self):
        return self.to_str()

class Deck:
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ["Hearts", "Diamonds", "Spades", "Clubs"]

    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card

        # TODO-1: конструктор добавляет в список self.cards все(52) карты
        self.cards = [Card(val, suit_val) for suit_val in Deck.suits for val in Deck.values]

        self.n = len(self.cards)
        self.i = 0

    def show(self):
        # TODO-2: Принцип работы данного метода прописан в 00_task_deck.md

        return f"cards[{len(self.cards)}]" + ','.join([card.to_str() for card in self.cards])
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

    def __str__(self):
        return self.show()

    def __iter__(self):
        self.n = len(self.cards)
        return self

    def __next__(self):
        if self.i < self.n :
           self.i += 1;
           return self.cards[self.i-1]

        raise StopIteration

    def __getitem__(self, key):
        return self.cards[key]


deck = Deck()
# TODO-final: реализовать нативную работу с объектами:
# 1. Вывод колоды в терминал:
print(deck)  # вместо print(deck.show())

card1, card2 = deck.draw(2)
# 2. Вывод карты в терминал:
print(card1)  # вместо print(card1.to_str())

# 3. Сравнение карт:
if card1 > card2:
    print(f"{card1} больше {card2}")
else:
    print(f"{card1} меньше {card2}")

# 4. Итерация по колоде:
for card in deck:
    print(card,end =' ')

# 5. Просмотр карты в колоде по ее индексу:
print("\n",deck[6])
