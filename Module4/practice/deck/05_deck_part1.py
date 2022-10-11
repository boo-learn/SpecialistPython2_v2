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
    def __init__(self,cards):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.cards = cards
        # TODO-1: конструктор добавляет в список self.cards все(52) карты

    def show(self, value):
        # TODO-2: Принцип работы данного метода прописан в 00_task_deck.md
        card_show_list = []
        for card in self.cards:
            card_show_list.append(card.to_str())
        return card_show_list[:value]



values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
cards = []
for value in values:
    card = Card(value,'Hearts')
    cards.append(card)
    card = Card(value, 'Diamonds')
    cards.append(card)
    card = Card(value, 'Spades')
    cards.append(card)
    card = Card(value, 'Clubs')
    cards.append(card)

# Создаем колоду
deck = Deck(cards)
# Выводим колоду в формате указанном в основном задании
print(deck.show(5))
