import random

class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        icons = {
            "Hearts": '\u2665',
            "Diamonds": "\u2666",
            "Spades": "\u2660",
            "Clubs": "\u2663"
        }
        return f"{self.value}{icons[self.suit]}"
    
    def more(self, other_card):
        suits_weight = {
            "Hearts": '3',
            "Diamonds": "2",
            "Spades": "1",
            "Clubs": "0"
        }
        if self.value > other_card.value:
            return True
    
        if self.value == other_card.value:
            print(suits_weight[self.suit], suits_weight[other_card.suit])
            if suits_weight[self.suit] > suits_weight[other_card.suit]:
                return True
            
        return False
    
    def less(self, other_card):
        if not self.more(other_card):
            return True

        

    def equal_suit(self, other_card):
        return self.suit == other_card.suit

class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.cards = []
        for suit in suits:
            for value in values:
                self.cards.append(Card(value, suit))

    def show(self):
        all_cards = []
        for card in self.cards:
            all_cards.append(card.to_str())
        return f'cards[{len(all_cards)}] {", ".join(all_cards)}'
    
    def draw(self, x):
        hand_cards = self.cards[:x]
        self.cards = self.cards[x:]
        return hand_cards

    def shuffle(self):
        random.shuffle(self.cards)


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
