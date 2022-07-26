# Начнем с создания карты
import random


class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты
        self.suit_dict = {
            'Hearts': '\u2665',
            'Diamonds': '\u2666',
            'Spades': '\u2660',
            'Clubs': '\u2663'
        }


    def to_str(self):
        return self.value + self.suit_dict.get(self.suit)

    def equal_suit(self, other_card):
        # TODO-1: метод возвращает True - если масти карт равны или False - если нет
        return self.suit == other_card.suit

    def more(self, other_card):
        if Deck.values.index(self.value) == Deck.values.index(other_card.value):
            return Deck.suits.index(self.suit) > Deck.suits.index(other_card.suit)
        return Deck.values.index(self.value) > Deck.values.index(other_card.value)

    def equal(self,other_card):
        return self.value == other_card.value and self.suit == other_card.suit

    def less(self, other_card):
        return not self.more(other_card) and not self.equal(other_card)


class Deck:
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ["Spades", "Clubs", "Diamonds", "Hearts"]
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card

        self.cards = []
        # TODO-1: конструктор добавляет в список self.cards все(52) карты
        self.cards = [Card(value=value, suit=suit) for value in self.values for suit in self.suits]

    def show(self):
        return f"cards[{len(self.cards)}]{', '.join([card.to_str() for card in self.cards])}"

    def draw(self, x):
        # TODO-1: Принцип работы данного метода прописан в 00_task_deck.md
        self.x = x
        x_list = []
        for card in self.cards[:x]:
            x_list.append(card.to_str())
            self.cards.remove(card)
        return x_list

    def shuffle(self):
        random.shuffle(self.cards)


# Создаем колоду
deck = Deck()
# Тусуем колоду
deck.shuffle()
print(deck.show())
# Берем две карты из колоды
card1, card2 = deck.draw(2)
card1 = Card('10', 'Hearts')
card2 = Card('10', 'Hearts')

# Тестируем методы .less() и .more()
if card1.more(card2):
    print(f"{card1.to_str()} больше {card2.to_str()}")
if card1.less(card2):
    print(f"{card1.to_str()} меньше {card2.to_str()}")
