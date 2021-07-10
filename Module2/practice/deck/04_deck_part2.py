  
    
    def more(self, other_card):
        masty = [Card.HEARTS,Card.DIAMONDS,Card.CLUBS,Card.SPADES]
        nominal = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        if nominal.index(self.value) > nominal.index(other_card.value):
            return True
        if  nominal.index(self.value) < nominal.index(other_card.value):
           return False
        if masty.index(self.suit) > masty.index(other_card.suit):
            return True
        return False
  
    def less(self, other_card):
        masty = [Card.HEARTS,Card.DIAMONDS,Card.CLUBS,Card.SPADES]
        nominal = ['2','3','4','5','6','7','8','9','10','J','Q','K','T']
        if nominal.index(self.value) < nominal.index(other_card.value):
            return True
        if  nominal.index(self.value) > nominal.index(other_card.value):
           return False
        if masty.index(self.suit) < masty.index(other_card.suit):
            return True
        return False
    
    
 
