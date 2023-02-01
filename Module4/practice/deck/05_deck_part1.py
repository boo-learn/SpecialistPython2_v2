class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        icon = None
        if self.suit == "Hearts":
            icon = '\u2665'
        elif self.suit == "Diamonds":
            icon = '\u2666'
        elif self.suit == "Spades":
            icon = '\u2660'
        else:
            icon = '\u2663'
        return f'{self.value}{icon}'

    def equal_suit(self, other_card):

        if self.suit == other_card.suit:
            return True
        return False



class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.cards = []
        for value in values:
            for suit in suits:
                self.cards.append(Card(value, suit))

    def show(self):
        # TODO-2: Принцип работы данного метода прописан в 00_task_deck.md
       
        final_str = f'deck[{len(self.cards)}]'
        str_cards = []
        for card in self.cards:
            str_cards.append(card.to_str())
        return final_str + ", ".join(str_cards)


# Создаем колоду
deck = Deck()
# Выводим колоду в формате указанном в основном задании
print(deck.show())
