class Card:
    # TODO-0: сюда копируем реализацию класса карты из предыдущего задания
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):        
        card_suits = {'Diamonds':'\u2666' ,'Hearts':'\u2665' , 'Spades':'\u2663' , 'Clubs':'\u2660'}
        return f'{self.value}{card_suits[self.suit]}'

    def equal_suit(self, other_card):
        # TODO-1: метод возвращает True - если масти карт равны или False - если нет
        return self.suit == other_card.suit


values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
hearts_cards = []
for value in values:
    value = Card(value, 'Hearts')
    hearts_cards.append(value)

diamonds_cards = []
for value in values:
    value = Card(value, 'Diamonds')
    diamonds_cards.append(value)

# TODO-3: выведите все карты из списка hearts_cards в терминал через запятую в одну строку:
# Пример вывода: 2♥, 3♥, 4♥ ... A♥
for heart_card in hearts_cards:
    print(heart_card.to_str(), end=' ')
print()
for diamond_card in diamonds_cards:
    print(diamond_card.to_str(), end=' ')

cards = [
    Card("2", "Hearts"),
    Card("3", "Hearts"),
    Card("4", "Hearts"),
    ...]
