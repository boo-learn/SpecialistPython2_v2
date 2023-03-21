class Card:
    # TODO-0: сюда копируем реализацию класса карты из предыдущего задания
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        # TODO-0: скопируйте реализацию метода из предыдущей задачи
        icons = {
            "Hearts": "\u2665",
            "Diamonds": "\u2666",
            "Spades": "\u2660",
            "Clubs": "\u2663"
        }
        return f"{self.value}{icons[self.suit]}"

    def equal_suit(self, other_card) -> bool:
        # TODO-1: метод возвращает True - если масти карт равны или False - если нет
        # if self.suit == other_card.suit:
        #     return True
        # else:
        #     return False
        return self.suit == other_card.suit

cards = []
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
# TODO-1: в список cards добавьте ВСЕ карты всех мастей
for suit in suits:
    #if suit in Card():
    for value in values:
        cards.append(Card(value, suit))
print(cards)

# TODO-2: Выведите карты в формате: cards[кол-во]2♥, 3♥, 4♥ ... A♥, 2♦, 3♦ ... A♦, ...
#  кол-во берем от размера списка cards
all_cards = []
for card in cards:
    all_cards.append(card.to_str())
print(f'cards {len(all_cards)} {", ".join(all_cards)}')
