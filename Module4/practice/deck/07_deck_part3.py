from random import shuffle
# Начнем с создания карты
class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        # TODO-1: метод возвращает строковое представление карты в виде: 10♥ и A♦
        if self.suit == "Hearts":
            card_suit = '\u2665'
        elif self.suit == "Diamonds":
            card_suit = '\u2666'
        elif self.suit == "Clubs":
            card_suit = '\u2663'
        elif self.suit == "Spades":
            card_suit = '\u2660'
        return f'{self.value}{card_suit}'

    def equal_suit(self, other_card):
        # TODO-1: метод возвращает True - если масти карт равны или False - если нет
        if self.suit == other_card.suit:
            return True
        else:
            return False

    def more(self, other_card):
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        for value in values:
            if self.value > other_card.value in values:
                return True

    def less(self, other_card):
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        if self.value < other_card.value in values:
            return True




class Deck:
    def __init__(self, cards):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.cards = cards
        for suit in suits:
            for value in values:
                cards.append(Card(value, suit))
        # TODO-1: конструктор добавляет в список self.cards все(52) карты

    def show(self, value):
        # TODO-2: Принцип работы данного метода прописан в 00_task_deck.md
        card_show_list = []
        for card in self.cards:
            card_show_list.append(card.to_str())
        return f'cards[{len(card_show_list)}], {",".join(card_show_list[:value])}'


    def draw(self, x):
        # TODO-1: Принцип работы данного метода прописан в 00_task_deck.md
        hand_deck = cards[0:x]
        del(cards[0:x])
        return hand_deck



    def shuffle(self):
        # TODO-2: Принцип работы данного метода прописан в 00_task_deck.md
        #   Подсказка: https://www.w3schools.com/python/ref_random_shuffle.asp
        return shuffle(cards)


# Создаем колоду
cards = []
deck = Deck(cards)
# Тусуем колоду
deck.shuffle()
print(deck.show(52))
# Берем две карты из колоды
card1, card2 = deck.draw(2)

# Тестируем методы .less() и .more()
if card1.more(card2):
    print(f"{card1.to_str()} больше {card2.to_str()}")
elif card1.less(card2):
    print(f"{card1.to_str()} меньше {card2.to_str()}")
else:
    print(f"карта {card1.to_str()} равна карте {card2.to_str()}")
