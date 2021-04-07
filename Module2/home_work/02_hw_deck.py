# Закончите все Задания: с колодой карт из файла practice/06_task_with_deck.md

# Закончите все Задания: с колодой карт из файла practice/06_task_with_deck.md
import random


class Card:
    HEARTS = "Hearts"
    DIAMONDS = "Diamonds"
    SPADES = "Spades"
    CLUBS = "Clubs"
    ICONS = {
        HEARTS: "♥",
        DIAMONDS: "♦",
        SPADES: "♠",
        CLUBS: "♣"
    }

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return f"{self.value}{Card.ICONS[self.suit]}"

    def to_str(self):
        return f"{self.value}{Card.ICONS[self.suit]}"

    def equal_suit(self, other_card):
        return self.suit == other_card.suit

    def __gt__(self, other_card):
        if Deck.VALUES.index(self.value) == Deck.VALUES.index(other_card.value):
            return Deck.SUITS.index(self.suit) > Deck.SUITS.index(other_card.suit)
        else:
            return Deck.VALUES.index(self.value) > Deck.VALUES.index(other_card.value)

    def __lt__(self, other_card):
        if Deck.VALUES.index(self.value) == Deck.VALUES.index(other_card.value):
            return Deck.SUITS.index(self.suit) < Deck.SUITS.index(other_card.suit)
        else:
            return Deck.VALUES.index(self.value) < Deck.VALUES.index(other_card.value)


class Deck:
    SUITS = [Card.SPADES, Card.CLUBS, Card.DIAMONDS, Card.HEARTS]
    VALUES = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self):
        self.card_index = 0
        self.cards = []
        for value in Deck.VALUES:
            for suit in Deck.SUITS:
                self.cards.append(Card(value, suit))

    def show(self):
        return f'deck[{len(self.cards)}]:' + ', '.join([card.to_str() for card in self.cards])

    def __str__(self):
        return f'deck[{len(self.cards)}]:' + ', '.join([card.to_str() for card in self.cards])

    def draw(self, count):
        cards_in_hand = self.cards[:count]
        self.cards = self.cards[count:]
        return cards_in_hand

    def shuffle(self):
        random.shuffle(self.cards)

    def __len__(self):
        return len(self.cards)

    def __iter__(self):
        self.card_index = 0
        return self

    def __next__(self):
        card = self.cards[self.card_index]
        self.card_index += 1
        if self.card_index >= len(self.cards):
            raise StopIteration
        return card


# Задание-4
# Создайте две колоды, в каждой должно быть 36 карт(старшинство карт начинается с 6-ки). Перемешайте их.
# Вытягивайте карты парами - одну из первой колоды, вторую из второй.
# Если карта из первой колоды окажется больше(старше), то записываем 1:0 (условно начисляем победное очко первой колоде),
# если карты одинаковые, то не учитываем очко никуда.
# Выведите итоговый счет, сравнив попарно все карты в колодах.

deck1 = Deck()
deck1.shuffle()
deck2 = Deck()
deck2.shuffle()
print(deck1)
print(deck2)

count_deck1 = 0
count_deck2 = 0
count = 0

while count < len(Deck.VALUES) * len(Deck.SUITS):
    card_deck1, = deck1.draw(1)
    card_deck2, = deck2.draw(1)
    if card_deck1 > card_deck2:
        count_deck1 += 1
    elif card_deck1 < card_deck2:
        count_deck2 += 1
    count += 1

print(f'Итоковый счет: {count_deck1}:{count_deck2}')
print('-' * 80)
