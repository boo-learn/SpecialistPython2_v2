import random

class Card:
    HEARTS = "Hearts"
    DIAMONDS = "Diamonds"
    SPADES = "Spades"
    CLUBS = "Clubs"

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def to_str(self):
        icons = {
            "Hearts": '\u2665',
            "Diamonds": '\u2666',
            "Spades": '\u2663',
            "Clubs": '\u2660',
        }
        return f"{self.value}{icons[self.suit]}"

    def equal_suit(self, other_card):
        return self.suit == other_card.suit




class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        self.cards = []
        nominal = ['V','D','K','A']
        mast = [Card.HEARTS,Card.DIAMONDS,Card.SPADES,Card.CLUBS]
        for im in mast:
            for ic in range(2,10):
                self.cards.append(Card(ic,im))
            for ic in nominal:
                self.cards.append(Card(ic,im))

    def show(self):
        str = ''
        for each in self.cards:
           str= str +each.to_str()
        return str

    def draw(self, x):
        pos = 0
        a = []
        for each in range(x):
            a.append(self.cards.pop())
        return a


    def shuffle(self):
        scards = self.cards.copy()
        full = len(scards)-1;
        print(full)
        self.cards = []
        for i in range(0,full):
            idcardf = random.choice(range(0,len(scards)-1))
            self.cards.append(scards[idcardf])
            scards.pop(idcardf)


# Создаем колоду
deck = Deck()
# Выводим колоду в формате указанном в основном задании
print(deck.show())
# Тусуем колоду
deck.shuffle()
print(deck.show())

# Возьмем 5 карт "в руку"
hand = deck.draw(5)
# Выводим колоду, чтобы убедиться что 5 верхних карт отсутствуют
print(deck.show())
# Выводим список карт "в руке"(список hand)
for each in hand:
    print('hand: '+each.to_str())
    
