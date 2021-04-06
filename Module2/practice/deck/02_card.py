class Card:
    def __init__(self, value, suit):
        value=[2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A]
        suit=[Diamonds, Hearts, Spades, Clubs]
        self.value=random.choice(value)
        self.suit=random.choice(suit)

    def to_str(self):
        #.to_str() возвращает строковое представление карты в виде строки, формата:4♦
        pic = {'Diamonds': '\u2666', 'Hearts': '\u2665','Spades':'\u2660','Clubs':'\u2663'}
        print (Card.value,pic[Card.suit])и")
