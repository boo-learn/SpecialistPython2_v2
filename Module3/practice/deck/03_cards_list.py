# Начнем с создания карты
class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты
    def __repr__(self): 
        return self.to_str()
    def to_str(self):
        symbols = {
            "Hearts":   "\u2665",
            "Diamonds": "\u2666",
            "Spades":   "\u2663",
            "Clubs":    "\u2660"
        }
        return f"{self.value}{symbols[self.suit]}"

    def equal_suit(self, other_card):
        # TODO-1: метод возвращает True - если масти карт равны или False - если нет
        return self.suit==other_card.suit


values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
hearts_cards = []
# TODO-1: добавьте в список hearts_cards все червовые карты(от 2-ки до туза)
for val in values:
    hearts_cards.append(Card(val,"Hearts"))

diamonds_cards = []
# TODO-2: добавьте в список diamonds_cards все бубновые карты(от туза до 2-ки)
for val in values:
    diamonds_cards.append(Card(val,"Diamonds"))

# TODO-3: выведите все карты из списка hearts_cards в терминал через запятую в одну строку:
# Пример вывода: 2♥, 3♥, 4♥ ... A♥
print(hearts_cards)
print(diamonds_cards)
