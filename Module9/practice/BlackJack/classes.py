
# Возьмите классы Deck и Card с GIST'а второго занятия и доработайте их
import random


class Card:
    HEARTS = "Hearts"
    DIAMONDS = "Diamonds"
    SPADES = "Spades"
    CLUBS = "Clubs"

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.points = Card.set_points(value)

    def __str__(self):
        icons = {
            "Hearts": '\u2665',
            "Diamonds": '\u2666',
            "Spades": '\u2663',
            "Clubs": '\u2660',
        }
        return f"{self.value}{icons[self.suit]}"

    @staticmethod
    def set_points(value):
        return Deck.points[value]

    def equal_suit(self, other_card):
        return self.suit == other_card.suit

    def __gt__(self, other_card):  # >
        if Deck.values.index(self.value) == Deck.values.index(other_card.value):
            return Deck.suits.index(self.suit) > Deck.suits.index(other_card.suit)
        else:
            return Deck.values.index(self.value) > Deck.values.index(other_card.value)

    def __lt__(self, other_card):  # <
        if Deck.values.index(self.value) == Deck.values.index(other_card.value):
            return Deck.suits.index(self.suit) < Deck.suits.index(other_card.suit)
        else:
            return Deck.values.index(self.value) < Deck.values.index(other_card.value)


# card1.more(card2)

class Deck:
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    points = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
              "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11}
    suits = [Card.CLUBS, Card.SPADES, Card.DIAMONDS, Card.HEARTS]

    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        self.cards = []
        #          0    1    2    3 ...
        self.last_card_index = -1
        for suit in Deck.suits:
            for value in Deck.values:
                card = Card(value, suit)
                self.cards.append(card)

    def __str__(self):
        s = f'deck[{len(self.cards)}]:'
        # str(card) --> card.__str__()
        for card in self.cards:
            s = s + str(card) + ","
        return s

    def __iter__(self):
        self.last_card_index = -1
        return self

    def __next__(self):
        self.last_card_index += 1
        if self.last_card_index >= len(self.cards):
            raise StopIteration
        return self.cards[self.last_card_index]

    def draw(self, x):
        cards = []
        for _ in range(x):
            cards.append(self.cards.pop(0))
        return cards

    def shuffle(self):
        random.shuffle(self.cards)

    def sum_points(cards):
#          """
#          Напишите отдельную функцию для нахождения суммы очков всех карт в списке
#          :param cards: список карт(рука игрока или диллера)
#          :return: сумму очков
#          """
#          # Совет: храните кол-во очков за карту внутри класса Колоды(колода "знает", сколько дает очков каждая карта)
        summa = 0
        for card in cards:
            summa += cards.points
        return summa
        
        if summa > 21:
            summa = 0
            for card in cards:
                if card.value == "A":
                    summa += 1
                else:
                    summa += 11
        return summa
        
                
card = Deck()
print(card.points)




