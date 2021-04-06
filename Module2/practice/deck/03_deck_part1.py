class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        self.cards = []
        value=['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suit=['Hearts', 'Diamonds', 'Spades', 'Clubs']
        for s in suit:
            for v in value:
                self.cards.append(Card (v,s))
        
    def show(self):


    def draw(self, x):
#метод .draw(x) - возвращает x первых карт из колоды в виде списка, эти карты убираются из колоды. 
#Уточнение: первую карту в списке считаем верхней картой колоды
        draw=[]
        for i in range (0,x):
            draw.append(Card[i])
            del self.cards[i]
        return draw
