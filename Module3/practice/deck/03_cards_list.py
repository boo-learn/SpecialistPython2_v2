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


values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
hearts_cards = []
# TODO-1: добавьте в список hearts_cards все червовые карты(от 2-ки до туза)

diamonds_cards = []
# TODO-2: добавьте в список diamonds_cards все бубновые карты(от туза до 2-ки)

# TODO-3: выведите все карты из списка hearts_cards в терминал через запятую в одну строку:
# Пример вывода: 2♥, 3♥, 4♥ ... A♥

for value in values:
    card = Card(value, "Hearts")
    hearts_cards.append(card.to_str())


for value in values:
    card = Card(value, "Diamonds")
    diamonds_cards.append(card.to_str())

print(', '.join(hearts_cards))
