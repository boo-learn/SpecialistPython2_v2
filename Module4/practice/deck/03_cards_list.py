class Card:
    # TODO-0: сюда копируем реализацию класса карты из предыдущего задания
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self) -> str:
        sign = self.suit.replace("Hearts", '\u2661').replace("Diamonds", '\u2662').replace("Spades", '\u2660').replace("Clubs", '\u2663')
        return f"{self.value} {sign}"

    def equal_suit(self, other_card) -> int:
        if self.suit == other_card.suit:
            return 1
        else:
            return 0


values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
hearts_cards = []
# TODO-1: добавьте в список hearts_cards все червовые карты(от 2-ки до туза)

for value in values:
    card = Card(value, 'Hearts')
    hearts_cards.append(card)

diamonds_cards = []
# TODO-2: добавьте в список diamonds_cards все бубновые карты(от туза до 2-ки)

for value in reversed(values):
    card = Card(value, 'Diamonds')
    diamonds_cards.append(card)

# TODO-3: выведите все карты из списка hearts_cards в терминал через запятую в одну строку:
# Пример вывода: 2♥, 3♥, 4♥ ... A♥

str = ''
for card in hearts_cards:
    str = str + card.to_str() + ', '
print(str[:-2])
    


cards = [
    Card("2", "Hearts"),
    Card("3", "Hearts"),
    Card("4", "Hearts")]
