class Card:

    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        # TODO-0: скопируйте реализацию метода из предыдущей задачи
        suit_value = {
            "Diamonds": '\u2662',
            "Hearts": '\u2661',
            "Spades": '\u2664',
            "Clubs": '\u2667'
        }
        return f"{self.value}{suit_value[self.suit]}"

    def equal_suit(self, other_card):
        # TODO-1: метод возвращает True - если масти карт равны или False - если нет
        if self.suit == other_card.suit:
            return True
        else:
            return False


values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
hearts_cards = []
diamonds_cards = []
# TODO-1: добавьте в список hearts_cards все червовые карты(от 2-ки до туза)
# TODO-2: добавьте в список diamonds_cards все бубновые карты(от туза до 2-ки)
for value in values:
    hearts_cards.append(Card(value, "Hearts"))
    diamonds_cards.append(Card(value, "Diamonds"))

# TODO-3: выведите все карты из списка hearts_cards в терминал через запятую в одну строку:
# Пример вывода: 2♥, 3♥, 4♥ ... A♥
cards_in_line = ""
for card in hearts_cards:
    cards_in_line += card.to_str() + ", "

print(cards_in_line[:len(cards_in_line) - 2])
