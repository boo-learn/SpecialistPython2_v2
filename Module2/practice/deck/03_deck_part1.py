class Card:
    pass
    # TODO: сюда копируем реализацию класса карты из предыдущего задания

# С коприровала из ответов
# Задание: Теперь создадим колоду из 52-ух карт и реализуем все методы
class Deck:
    def __init__(self):
        values = ["2", "3", "4", "10", "J", "Q", "K", "A"]
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.cards = []
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        for suit in suits:
            for value in values:
                card = Card(value, suit)
                self.cards.append(card)

    def show(self):
        deck_str = f"deck[{len(self.cards)}]"
        for card in self.cards:
            deck_str += card.to_str() + ","
        return deck_str

#my turn - моя работа 
    def draw(self, x):
        print(self.cards.pop())

#import random
    def shuffle(self):
        random.shuffle(cards)

