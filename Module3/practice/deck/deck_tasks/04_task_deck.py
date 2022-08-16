import random


class Card:
    DIAMONDS = "Diamonds"
    HEARTS = "Hearts"
    SPADES = "Spades"
    CLUBS = "Clubs"

    checksuit = {"Hearts": 4, "Diamonds": 3, "Spades": 2, "Clubs": 1}
    checkvalue = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
                  "J": 11, "Q": 12, "K": 13, "A": 14}

    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def __str__(self):
        symbols = {
            "Hearts": "\u2665",
            "Diamonds": "\u2666",
            "Spades": "\u2663",
            "Clubs": "\u2660"
        }
        return f"{self.value}{symbols[self.suit]}"

    def equal_suit(self, other_card): #==
        return self.suit == other_card.suit

    def __gt__(self, other_card): # >
        if Card.checkvalue[self.value] == Card.checkvalue[other_card.value]:  # ♥>♦>♣>♠
            return Card.checksuit[self.suit] > Card.checksuit[other_card.suit]
        else:
            return Card.checkvalue[self.value] > Card.checkvalue[other_card.value]

    def __lt__(self, other_card): # <
        return not self > other_card

class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        values = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.cards = []
        for suit in suits:
            for value in values:
                self.cards.append(Card(value, suit))

    def __str__(self):
        cards_list = []
        for card in self.cards:
            cards_list.append(str(card))
        return f"cards[{len(self.cards)}]:{', '.join(cards_list)}"

    def draw(self, x):
        take_cards = self.cards[:x]
        self.cards = self.cards[x:]
        return take_cards

    def shuffle(self):
        random.shuffle(self.cards)

    def __getitem__(self, index):
        return self.cards[index]

deck1 = Deck()
deck2 = Deck()
deck1.shuffle()
deck2.shuffle()

deck1_score = 0
deck2_score = 0

while deck1.cards:
    card1 = deck1.draw(1)[0]
    card2 = deck2.draw(1)[0]
    if card1 > card2:
        deck1_score += 1
    elif card1 < card2: 
        deck2_score += 1

print(f"Итоговый счёт  {deck1_score} : {deck2_score}")
