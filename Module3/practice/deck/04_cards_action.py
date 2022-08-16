class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        if self.suit == "Hearts":
            return f"\u2665 {self.value} "
        elif self.suit == "Diamonds":
            return f"\u2666 {self.value} "
        elif self.suit == "Spades":
            return f"\u2664{self.value} "
        elif self.suit == "Clubs":
            return f"\u2667{self.value} "

    def equal_suit(self, other_card):
        if self.suit == other_card:
            return True
        else:
            return False


# Создадим несколько карт
card1 = Card("10", "Hearts")
card2 = Card("A", "Diamonds")

# Выведем карты на экран в виде: 10♥ и A♦
print(card1.to_str())
print(card2.to_str())

# Пример, вывод иконок мастей:
# print('\u2661', '\u2665')
# print('\u2662', '\u2666')
# print('\u2667', '\u2663')
# print('\u2664', '\u2660')
if card1.equal_suit(card2):
    print(f"У карт: {card1.to_str()} и {card2.to_str()} одинаковые масти")
else:
    print(f"У карт: {card1.to_str()} и {card2.to_str()} разные масти")

    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
hearts_cards = []
diamonds_cards = []
spades_cards = []
clubs_cards = []
    # TODO-1: добавьте в список hearts_cards все червовые карты(от 2-ки до туза)
for val1 in values:
    hearts_cards.append(Card(val1, "Hearts"))
for val1 in values:
    diamonds_cards.append(Card(val1, "Diamonds"))
for val1 in values:
    spades_cards.append(Card(val1, "Spades"))
for val1 in values:
    clubs_cards.append(Card(val1, "Clubs"))

    # TODO-2: добавьте в список diamonds_cards все бубновые карты(от туза до 2-ки)

    # TODO-3: выведите все карты из списка hearts_cards в терминал через запятую в одну строку:
    # Пример вывода: 2♥, 3♥, 4♥ ... A♥
for card in hearts_cards:
    print(card.to_str(), ',', end=' ')

print(' ')

for card in clubs_cards:
    print(card.to_str(), ',', end=' ')


#cards = [hearts_cards, diamonds_cards, spades_cards, clubs_cards]
cards = []
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
# TODO-1: в список cards добавьте ВСЕ карты всех мастей

# TODO-2: Выведите карты в формате: cards[кол-во]2♥, 3♥, 4♥ ... A♥, 2♦, 3♦ ... A♦, ...
#  кол-во берем от размера списка cards

print(' ')
print(' ')

for val1 in values:
    cards.append(Card(val1, "Hearts"))
for val1 in values:
    cards.append(Card(val1, "Diamonds"))
for val1 in values:
    cards.append(Card(val1, "Spades"))
for val1 in values:
    cards.append(Card(val1, "Clubs"))
print('cards[', len(cards), ']')
for card in cards:
    print(card.to_str(), ',', end=' ')
