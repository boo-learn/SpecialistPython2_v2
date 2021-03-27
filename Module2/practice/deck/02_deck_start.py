class Deck:
    suits = [Card.DIAMONDS, Card.HEARTS, Card.SPADES, Card.CLUBS]
    cards_list = ["2", "3", "4", "5", "6", "7",  "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self):
        self.cards = []
        for suit in Deck.suits:
            for card in Deck.cards_list:
                self.cards.append(Card(Deck.suits[suit], Deck.cards_list[card]))

        return self.cards


    def show(self):


    def draw(self, x):


    def shuffle(self):
   
