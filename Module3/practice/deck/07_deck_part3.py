class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты
        self.suit_icons = {'Hearts': '\u2665', 'Diamonds': '\u2666', 'Clubs': '\u2663', 'Spades': '\u2660'}

    def to_str(self):
        return f'{self.value}{self.suit_icons[self.suit]}'

    def equal_suit(self, other_card):
        return self.suit == other_card.suit

    # TODO-1: реализуем новые методы
    def more(self, other_card):
        values = {'2': 1 , '3': 2, '4' : 3, '5' : 4, '6' : 5, '7' : 6, '8' :7 , '9' : 8, '10' : 9, 'J' : 10, 'Q' : 11, 'K' : 12, 'A' : 13}
        suits = {'Hearts' : 4,'Diamonds' : 3,'Clubs' : 2,'Spades' : 1}
        
        if values[self.value] > values[other_card.value]:
            return values[self.value] > values[other_card.value]
        elif values[self.value] == values[other_card.value]:
            if suits[self.suit] > suits[other_card.suit]:
                return suits[self.suit] > suits[other_card.suit]
                

    def less(self, other_card):
        values = {'2': 1 , '3': 2, '4' : 3, '5' : 4, '6' : 5, '7' : 6, '8' :7 , '9' : 8, '10' : 9, 'J' : 10, 'Q' : 11, 'K' : 12, 'A' : 13}
        suits = {'Hearts' : 4,'Diamonds' : 3,'Clubs' : 2,'Spades' : 1}
        
        if values[self.value] < values[other_card.value]:
            return values[self.value] < values[other_card.value]
        elif values[self.value] == values[other_card.value]:
            if suits[self.suit] < suits[other_card.suit]:
                return suits[self.suit] < suits[other_card.suit]
                


class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.cards = []
        for suit in suits:
            for value in values:
                self.cards.append(Card(value, suit))
        # TODO-1: конструктор добавляет в список self.cards все(52) карты

    def show(self):
        # TODO-2: Принцип работы данного метода прописан в 00_task_deck.md
        ...
        return (f"cards[{len(self.cards)}]{', '.join([card.to_str() for card in self.cards])}")
    

    def draw(self, x):
        # TODO-1: Принцип работы данного метода прописан в 00_task_deck.md
        draw_5_card=[]
        for i in range(x):
            draw_5_card.append(self.cards[i])
            
        for i in range(x):
            self.cards.remove(draw_5_card[i])
        return draw_5_card
        

    def shuffle(self):
        # TODO-2: Принцип работы данного метода прописан в 00_task_deck.md
        #   Подсказка: https://www.w3schools.com/python/ref_random_shuffle.asp
        import random
        random.shuffle(self.cards)


# Создаем колоду
deck = Deck()
# Тусуем колоду
deck.shuffle()
print(deck.show())
# Берем две карты из колоды
card1, card2 = deck.draw(2)

# Тестируем методы .less() и .more()
if card1.more(card2):
    print(f"{card1.to_str()} больше {card2.to_str()}")
if card1.less(card2):
    print(f"{card1.to_str()} меньше {card2.to_str()}")
