# Начнем с создания карты
class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        if self.suit == "Hearts"  : g_suit = '\u2665'
        if self.suit == "Diamonds": g_suit = '\u2666'
        if self.suit == "Clubs"   : g_suit = '\u2663'
        if self.suit == "Spades"  : g_suit = '\u2660'
        return f"{self.value}{g_suit}"
        # TODO-1: метод возвращает строковое представление карты в виде: 10♥ и A♦
        ...

    def equal_suit(self, other_card):
        return self.suit == other_card.suit
        # TODO-1: метод возвращает True - если масти карт равны или False - если нет
        ...


values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
hearts_cards = []
# TODO-1: добавьте в список hearts_cards все червовые карты(от 2-ки до туза)
diamonds_cards = []
# TODO-2: добавьте в список diamonds_cards все бубновые карты(от туза до 2-ки)

for value in values:
    hearts_cards.append(Card(value, 'Hearts'))
    diamonds_cards.append(Card(value, 'Diamonds'))

# TODO-3: выведите все карты из списка hearts_cards в терминал через запятую в одну строку:
# Пример вывода: 2♥, 3♥, 4♥ ... A♥
cards_str = []
for card in hearts_cards:
    cards_str.append(card.to_str())
print(", ".join(cards_str))

cards_str = []
for card in diamonds_cards:
    cards_str.append(card.to_str())
print(", ".join(cards_str))
#####################################################################################
cards = []
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
# TODO-1: в список cards добавьте ВСЕ карты всех мастей
for value in values:
    for c_suit in suits:
        card = Card(value, c_suit)
        cards.append(card.to_str())
print("cards [",len(cards) , "] ",  ", ".join(cards))
# TODO-2: Выведите карты в формате: cards[кол-во]2♥, 3♥, 4♥ ... A♥, 2♦, 3♦ ... A♦, ...
#  кол-во берем от размера списка cards



