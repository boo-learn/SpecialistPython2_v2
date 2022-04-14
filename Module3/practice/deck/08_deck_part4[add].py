import random

class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        dict_1 = {"Hearts": '\u2665', "Diamonds": '\u2666', "Clubs": '\u2663', "Spades": '\u2660'}
        return f"{self.value}{dict_1[self.suit]}"

    def equal_suit(self, other_card):
        return self.suit == other_card.suit

    def more(self, other_card):
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        if (values.index(self.value)>values.index(other_card.value)):
            return True
        elif (values.index(self.value)==values.index(other_card.value) and suits.index(self.suit)<suits.index(other_card.suit)):
            return True
        else:
            return False


    def less(self, other_card):
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        if (values.index(self.value)<values.index(other_card.value)):
            return True
        elif (values.index(self.value)==values.index(other_card.value) and suits.index(self.suit)>suits.index(other_card.suit)):
            return True
        else:
            return False


class Deck:
    def __init__(self):
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.cards = []
        for i in range(len(suits)):
            for value in values:
                self.cards.append(Card(value, suits[i]))

    def show(self):
        cards_str = list()

        for card in self.cards:
            cards_str.append(card.to_str())

        return (f"cards:[{len(self.cards)}] " + ", ".join(cards_str))


    def draw(self, x):
        hand=[]
        hand=self.cards[ :x]
        self.cards=self.cards[x: ]
        return hand

    def shuffle(self):
        random.shuffle(self.cards)

    def shift(self, num_card):
        shift_cards = []
        shift_cards = self.cards[:num_card]
        self.cards = self.cards[num_card:]
        self.cards+=shift_cards


# Создаем колоду
deck = Deck()
# Тусуем колоду
deck.shuffle()
print(deck.show())
# Сдвигаем 10 карт
deck.shift(10)
print(deck.show())
