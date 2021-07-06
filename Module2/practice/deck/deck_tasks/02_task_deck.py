# Сюда отправляем решение второй задачи с колодой
import random


class Card:
    HEARTS = "Hearts"
    DIAMONDS = "Diamonds"
    CLUBS = "Clubs"
    SPADES = "Spades"

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def to_str(self):
        icons = {
            "Hearts": '\u2665',
            "Diamonds": '\u2666',
            "Clubs": '\u2663',
            "Spades": '\u2660',
        }
        return f"{self.value}{icons[self.suit]}"

    def equal_suit(self, other_card):
        return self.suit == other_card.suit

    def more(self, other_card):
        value_index_self = Deck.values.index(self.value)
        value_index_other = Deck.values.index(other_card.value)
        if value_index_self == value_index_other:
            suit_index_self = Deck.suits.index(self.suit)
            suit_index_other = Deck.suits.index(other_card.suit)
            return suit_index_self > suit_index_other
        return value_index_self > value_index_other

    def less(self, other_card):
        value_index_self = Deck.values.index(self.value)
        value_index_other = Deck.values.index(other_card.value)
        if value_index_self == value_index_other:
            suit_index_self = Deck.suits.index(self.suit)
            suit_index_other = Deck.suits.index(other_card.suit)
            return suit_index_self < suit_index_other
        return value_index_self < value_index_other


class Deck:
    values = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
    suits = ("Spades", "Clubs", "Diamonds", "Hearts")

    def __init__(self):
        self.cards = []
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        for suit in Deck.suits:
            for value in Deck.values:
                card = Card(value, suit)
                self.cards.append(card)

    def show(self):
        deck_str = f"deck[{len(self.cards)}]"
        for card in self.cards:
            deck_str += card.to_str() + ","
        return deck_str

    def draw(self, x):
        cards_draw = self.cards[0:x]
        self.cards = self.cards[x:]
        return cards_draw

    def shuffle(self):
        random.shuffle(self.cards)


deck = Deck()
deck.shuffle()
print(deck.show())
cards_draw = Deck()
cards_draw = deck.draw(10)

# print(cards_draw)  как тут нормально вывести
heart_num = 0
diamond_num = 0
clubs_num = 0
spades_num = 0
for card in cards_draw:
    if card.suit == 'Hearts':
        heart_num += 1
    elif card.suit == 'Diamonds':
        diamond_num += 1
    elif card.suit == 'Clubs':
        clubs_num += 1
    else:
        spades_num += 1

cards_count = {
                'Hearts': heart_num,
                'Diamonds': diamond_num,
                'Çlubs': clubs_num,
                'Spades': spades_num
}
print('Среди вытянутых наибольшее количество:')
max_number = max(cards_count.values())
for suit, number in cards_count.items():
    if number == max_number:
         print(suit, end = ' ')
