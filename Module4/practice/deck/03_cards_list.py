class Card:
    # TODO-0: сюда копируем реализацию класса карты из предыдущего задания
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        # TODO-0: скопируйте реализацию метода из предыдущей задачи
        card_suits = {'Diamonds': '\u2666', 'Hearts': '\u2665', 'Spades': '\u2663', 'Clubs': '\u2660'}
        return f"{self.value}{card_suits[self.suit]}"

    def equal_suit(self, other_card):
        # TODO-1: метод возвращает True - если масти карт равны или False - если нет
        return self.suit == other_card.suit



values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
# cards = [
#     Card("2", "Hearts"),
#     Card("3", "Diamonds"),
#     Card("4", "Hearts"),
#     Card("5", "Diamonds"),
#     Card("6", "Hearts"),
#     Card("7", "Hearts"),
#     Card("8", "Diamonds"),
#     Card("9", "Hearts"),
#     Card("10", "Hearts"),
#     Card("J", "Diamonds"),
#     Card("Q", "Hearts"),
#     Card("K", "Diamonds"),
#     Card("A", "Hearts"),
#     ]

hearts_cards = []
diamonds_cards = []
# TODO-1: добавьте в список hearts_cards все червовые карты(от 2-ки до туза)
for card in values:
    hearts_cards.append(Card(card, 'Hearts'))
    diamonds_cards.append(Card(card, 'Diamonds'))
# TODO-2: добавьте в список diamonds_cards все бубновые карты(от туза до 2-ки)
diamonds_cards.reverse()
# TODO-3: выведите все карты из списка hearts_cards в терминал через запятую в одну строку:
# Пример вывода: 2♥, 3♥, 4♥ ... A♥
for heart_card in hearts_cards:
    print(heart_card.to_str(), end = ' ')
print()
for diamond_card in diamonds_cards:
    print(diamond_card.to_str(), end = ' ') 



