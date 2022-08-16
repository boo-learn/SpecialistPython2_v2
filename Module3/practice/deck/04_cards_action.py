class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def __get_suit_symbol(self, suit):
        suits = {
            "Hearts": "\u2665",
            "Diamonds": "\u2666",
            "Spades": "\u2663",
            "Clubs": "\u2660"

        }
        return suits[suit]

    def to_str(self):
        # TODO-1: метод возвращает строковое представление карты в виде: 10♥ и A♦
        return f"{self.value}{self.__get_suit_symbol(self.suit)}"

    def equal_suit(self, other_card):
        # TODO-1: метод возвращает True - если масти карт равны или False - если нет
        return self.suit == other_card.suit


cards = []
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
# TODO-1: в список cards добавьте ВСЕ карты всех мастей

for suit in suits:
    for value in values:
        cards.append(Card(value, suit))

def get_cards(cards):
    cards_list = []
    for card in cards:
        cards_list.append(card.to_str())
    print(f'cards[{len(cards)}]', ' ,'.join(cards_list))

get_cards(cards)

# TODO-2: Выведите карты в формате: cards[кол-во]2♥, 3♥, 4♥ ... A♥, 2♦, 3♦ ... A♦, ...
#  кол-во берем от размера списка cards
