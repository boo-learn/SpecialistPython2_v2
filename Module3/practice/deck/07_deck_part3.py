# Начнем с создания карты
class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты
        self.checksuit={ "Hearts":   4,   "Diamonds": 3,  "Spades":   2,  "Clubs":    1    }
        self.checkvalue={ "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13, "A": 14  }
    def __repr__(self): 
        return self.to_str()
    def to_str(self):
        symbols = {  "Hearts":   "\u2665",    "Diamonds": "\u2666",   "Spades":   "\u2663",  "Clubs":    "\u2660"    }
        return f"{self.value}{symbols[self.suit]}"

    def equal_suit(self, other_card):
        # TODO-1: метод возвращает True - если масти карт равны или False - если нет
        return self.suit==other_card.suit
    # TODO-1: реализуем новые методы
    def more(self, other_card):
        if self.checkvalue[self.value]==self.checkvalue[other_card.value]: #♥>♦>♣>♠
            return int(self.checksuit[self.suit])>int(self.checksuit[other_card.suit])
        else:
            return int(self.checkvalue[self.value])>int(self.checkvalue[other_card.value])
            # Пример, вывод иконок мастей:
            # print('\u2661', '\u2665') #Hearts	    Червы
            # print('\u2662', '\u2666') #Diamonds    Бубны
            # print('\u2667', '\u2663') #Clubs       Трефы
            # print('\u2664', '\u2660') #Spades	    Пики

    def less(self, other_card):
        if self.checkvalue[self.value]==self.checkvalue[other_card.value]: #♥>♦>♣>♠
            return int(self.checksuit[self.suit])<int(self.checksuit[other_card.suit])
        else:
            return int(self.checkvalue[self.value])<int(self.checkvalue[other_card.value])

class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.cards = []
        # TODO-1: конструктор добавляет в список self.cards все(52) карты
        for val in values:
            for suit in suits:
                self.cards.append(Card(val,suit))
    def show(self):
        # TODO-2: Принцип работы данного метода прописан в 00_task_deck.md
        cards_list = []
        for card in self.cards:
            cards_list.append(card.to_str())
        print(f"cards[{len(self.cards)}]{' ,'.join(cards_list)}")

    def draw(self, x):
        # TODO-1: Принцип работы данного метода прописан в 00_task_deck.md
        hand=[]
        for index, card in enumerate(self.cards): 
            if index>=x:
                break
            #или    card=self.cards.pop(0) # 
            #       hand.append(card)
            hand.append(card)
            self.cards.remove(card)

        return hand
    def shuffle(self):
        # TODO-2: Принцип работы данного метода прописан в 00_task_deck.md
        #   Подсказка: https://www.w3schools.com/python/ref_random_shuffle.asp
        import random
        random.shuffle(self.cards)

# Создаем колоду
deck = Deck()
# Тусуем колоду
deck.shuffle()
deck.show()
# Берем две карты из колоды
card1, card2 = deck.draw(2)

# Тестируем методы .less() и .more()
if card1.more(card2):
    print(f"{card1.to_str()} больше {card2.to_str()}")
if card1.less(card2):
    print(f"{card1.to_str()} меньше {card2.to_str()}")
