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
# Выводим колоду в формате указанном в основном задании
print(deck.show(52))
# Тусуем колоду
deck.shuffle()
print(deck.show(52))

# Возьмем 5 карт "в руку"
hand = deck.draw(5)
# Выводим колоду, чтобы убедиться что 5 верхних карт отсутствуют
print(deck.show(52))
# Выводим список карт "в руке"(список hand)
visual_hand = []
for card in hand:
    visual_hand.append(card.to_str())
print(f'cards[{len(visual_hand)}], {",".join(visual_hand)}')
