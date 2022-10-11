# Начнем с создания карты
import random
class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты
        self.cost_card = {
        '2':2,
        '3':3,
        '4':4,
        '5':5,
        '6':6,
        '7':7,
        '8':8,
        '9':9,
        '10':10,
        'J': 10,
        'Q': 10,
        'K': 10,
        'A': 11,
        }#стоимость карт из игры блэкджек

    def to_str(self):
        suit_icon = {
        'Hearts':'\u2665',
        'Diamonds':'\u2666',
        'Clubs':'\u2663',
        'Spades':'\u2660',
        }

        return f"{self.value}{suit_icon[self.suit]}"
        # TODO-1: метод возвращает строковое представление карты в виде: 10♥ и A♦

    def equal_suit(self, card1):
        if card1.suit==self.suit:
            return True
        else:
            return False

    def more(self, other_card):
        return self.cost_card[self.value]>other_card.cost_card[other_card.value]

    def less(self, other_card):
        return self.cost_card[self.value] < other_card.cost_card[other_card.value]

class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.cards = []
        for svit in suits:
            for value in values:
                self.cards.append(Card(value,svit))
        # TODO-1: конструктор добавляет в список self.cards все(52) карты

    def show(self, text:str = "Количество карт в колоде")->str:
        card_str = []
        text = text
        for card in self.cards:
            card_str.append(card.to_str())
        return f"{text} {len(self.cards)}: {', '.join(card_str)}"

    def draw(self, x:int):
        card_in_hand=Deck()
        card_in_hand.cards.clear()
        for i in range(x):
            card_in_hand.cards.append(self.cards[i])
            self.cards.pop(0)
        return card_in_hand

    def shuffle(self):
        random.shuffle(self.cards)

deck1 = Deck()
deck1.shuffle()
hand=deck1.draw(2)
print(hand.show("Карт в руке"))
print(hand.cards[0].more(hand.cards[1]))
print(hand.cards[0].less(hand.cards[1]))
print(deck1.show())
