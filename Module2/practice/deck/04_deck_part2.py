    def more(self, card):
        values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        if values.index(self.value) > values.index(card.value):
            return True
        elif values.index(self.value) == values.index(card.value) and suits.index(self.suit) < suits.index(card.suit):
            return True
        else:
            return False

    def less(self, card):
        values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        if values.index(self.value) < values.index(card.value):
            return True
        elif values.index(self.value) == values.index(card.value) and suits.index(self.suit) > suits.index(card.suit):
            return True
        else:
            return False
