
# Начнем с создания карты
class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        st = ''
        # TODO-1: метод возвращает строковое представление карты в виде: 10♥ и A♦
        if self.suit == 'Hearts':
            st = '\u2665'
        elif self.suit == 'Diamonds':
            st = '\u2666'
        elif self.suit == 'Clubs':
            st = '\u2663'
        elif self.suit == 'Spades':
            st = '\u2660'

        return f'{self.value}{st}'

    def equal_suit(self, other_card):

            # TODO-1: метод возвращает True - если масти карт равны или False - если нет
        return True if other_card.suit == self.suit else False



# Создадим несколько карт
card1 = Card("10", "Hearts")
card2 = Card("A", "Diamonds")

# Выведем карты на экран в виде: 10♥ и A♦
print(card1.to_str())
print(card2.to_str())

'''
# Пример, вывод иконок мастей:
print('\u2661', '\u2665')
print('\u2662', '\u2666')
print('\u2667', '\u2663')
print('\u2664', '\u2660')
'''

if card1.equal_suit(card2):
    print(f"У карт: {card1.to_str()} и {card2.to_str()} одинаковые масти")
else:
    print(f"У карт: {card1.to_str()} и {card2.to_str()} разные масти")

#####################################

values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
hearts_cards = []
# TODO-1: добавьте в список hearts_cards все червовые карты(от 2-ки до туза)
for unit in values:
    hearts_cards.append(Card(unit, 'Heards'))


diamonds_cards = []
# TODO-2: добавьте в список diamonds_cards все бубновые карты(от туза до 2-ки)
for unit in values[::-1]:
    hearts_cards.append(Card(unit, 'Diamonds'))


# TODO-3: выведите все карты из списка hearts_cards в терминал через запятую в одну строку:
# Пример вывода: 2♥, 3♥, 4♥ ... A♥
for unit in hearts_cards:
    print(unit.to_str(), end=' ')

cards = [
    Card("2", "Hearts"),
    Card("3", "Hearts"),
    Card("4", "Hearts"),
    ...]

