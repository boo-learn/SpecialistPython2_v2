class Card:
    pass
    # TODO: сюда копируем реализацию класса карты из предыдущего задания


# Задание: Теперь создадим колоду из 52-ух карт и реализуем все методы
class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        self.cards = []

    def show(self):
        pass

    def draw(self, x):
        counter = x
        small_deck = []
        for i in range (counter):
            rand_card = random.randint(0, len(self.cards))
            small_deck.append(self.cards.pop(rand_card))
        deck_str_hand = f"deck[{len(small_deck)}]"
        for card in small_deck:
            deck_str_hand += card.to_str() + ","
        return deck_str_hand

    def shuffle(self):
        random.shuffle(self.cards)
    # По невнимательности не совсем корректно вычитал задание, но, тем не менее отправлю
    # берем из перемешенной колоды 5 любых карт
    
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
print(deck.draw(5))
