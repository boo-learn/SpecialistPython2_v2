
# Задание: Теперь создадим колоду из 52-ух карт и реализуем все методы
class Deck:
    def __init__(self):

        self.cards = []
        values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

        for value in values:
            for suit in suits:
                deck_card = Card(value, suit)
                self.cards.append(deck_card)

    def show(self):
        print(f" cards [{len(self.cards)}]", end="")
        for card in self.cards:
            print(f" {card.to_str()}", end=", ")

    def draw(self, x):
            # Принцип работы данного метода прописан в 00_task_deck.md
            pass

    def shuffle(self):
        random.shuffle(self.cards)

