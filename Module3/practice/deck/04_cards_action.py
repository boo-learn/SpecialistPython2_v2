# Начнем с создания карты
class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        suits = {'Diamonds':'\u2666','Hearts':'\u2665','Spades':'\u2660','Clubs':'\u2663'}
        return f'{self.value}{suits[self.suit]}'

    def equal_suit(self, other_card):
        return self.suit == other_card.suit


# Создадим несколько карт
card1 = Card("10", "Hearts")
card2 = Card("A", "Diamonds")

# Выведем карты на экран в виде: 10♥ и A♦
print(card1.to_str())
print(card2.to_str())

if card1.equal_suit(card2):
    print(f"У карт: {card1.to_str()} и {card2.to_str()} одинаковые масти")
else:
    print(f"У карт: {card1.to_str()} и {card2.to_str()} разные масти")
hearts_cards = []
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

# TODO-1: добавьте в список hearts_cards все червовые карты(от 2-ки до туза)
hearts_cards=[Card(val, "Hearts") for val in values]

diamonds_cards = []
# TODO-2: добавьте в список diamonds_cards все бубновые карты(от туза до 2-ки)
for val in reversed(values):
    diamonds_cards.append([Card(val, "Diamonds")])

# TODO-3: выведите все карты из списка hearts_cards в терминал через запятую в одну строку:
# for card in hearts_cards:
#     print (card.to_str(), end=",")


values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ["Hearts", "Diamonds", "Spades", "Clubs"]

# TODO-1: в список cards добавьте ВСЕ карты всех мастей
cards = [Card(val, suit) for val in values for suit in suits]
print(f'cards[{len(cards)}]:', end=' ')
for card in cards:
    print (card.to_str(), end=",")
# TODO-2: Выведите карты в формате: cards[кол-во]2♥, 3♥, 4♥ ... A♥, 2♦, 3♦ ... A♦, ...
#  кол-во берем от размера списка cards
