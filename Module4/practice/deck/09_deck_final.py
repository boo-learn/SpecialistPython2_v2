# Начнем с создания карты
import random
class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты
        self.cost_card = {
        '2':1,
        '3':2,
        '4':3,
        '5':4,
        '6':5,
        '7':6,
        '8':7,
        '9':8,
        '10':9,
        'J': 10,
        'Q': 11,
        'K': 12,
        'A': 13,
        }#стоимость карт из игры блэкджек

        self.cost_card_suit = {
            'Hearts': 1,
            'Diamonds': 2,
            'Spades': 3,
            'Clubs': 4,
        }
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

    def __gt__(self, other_card):
        if self.cost_card[self.value]==other_card.cost_card[other_card.value]:
            return self.cost_card_suit[self.value] > other_card.cost_card_suit[other_card.value]
        else:
            return self.cost_card[self.value]>other_card.cost_card[other_card.value]



    def __lt__(self, other_card):
        if self.cost_card[self.value] == other_card.cost_card[other_card.value]:
            return self.cost_card_suit[self.value] < other_card.cost_card_suit[other_card.value]
        else:
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

    def __str__(self, text:str = "Количество карт в колоде")->str:
        card_str = []
        text = text
        for card in self.cards:
            card_str.append(card.to_str())
        return f"{text} {len(self.cards)}: {', '.join(card_str)}"

    def __getitem__(self,num:int):
        return self.cards[num].to_str()


    def draw(self, x:int):
        card_in_hand=self.cards[:x]
        self.cards = self.cards[x:]
        return card_in_hand

    def shuffle(self):
        random.shuffle(self.cards)

    def shift(self, num_card:int):
        for i in range(num_card):
            self.cards.append(self.cards[0])
            self.cards.pop(0)



deck1 = Deck()

hand1 = deck1.draw(1)
hand2 = deck1.draw(1)

for card in deck1:
    print(card)
if hand1<hand2:
    print(deck1)
print(deck1[0])
