class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):

        res = f'{self.value}{self.to_suit()}'
        return res

    def to_suit(self):
        if self.suit == 'Diamonds':
            # print('\u2662', '\u2666')
            res = '\u2666'
        elif self.suit == 'Hearts':
            # print('\u2661', '\u2665')
            res = '\u2665'
        elif self.suit == 'Spades ':
            # print('\u2664', '\u2660')
            res = '\u2660'
        else: #Clubs
            # print('\u2667', '\u2663')
            res = '\u2663'

        return res

    def equal_suit(self, other_card):

        if self.suit == other_card.suit:
            res = True
        else:
            res = False

        return res


values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
hearts_cards = []
# TODO-1: добавьте в список hearts_cards все червовые карты(от 2-ки до туза)

for value in values:
    card1 = Card(value,'Hearts')
    hearts_cards.append(card1)


diamonds_cards = []
# TODO-2: добавьте в список diamonds_cards все бубновые карты(от туза до 2-ки)
values.reverse()
for value in values:
    card1 = Card(value,'Diamonds')
    diamonds_cards.append(card1)

# res = ''
# for card1 in diamonds_cards:
#     res = f'{res }{card1.to_str()} '
#
# print(res)

# TODO-3: выведите все карты из списка hearts_cards в терминал через запятую в одну строку:
# Пример вывода: 2♥, 3♥, 4♥ ... A♥
res = ''
for card1 in hearts_cards:
    res = f'{res }{card1.to_str()} '

print(res)

# cards = [
#     Card("2", "Hearts"),
#     Card("3", "Hearts"),
#     Card("4", "Hearts"),
#     ...]
