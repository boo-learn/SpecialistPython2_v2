
# Возьмите классы Deck и Card с GIST'а второго занятия и доработайте их
import random

class Card:
    
    HEARTS = "Hearts"
    DIAMONDS = "Diamonds"
    SPADES = "Spades"
    CLUBS = "Clubs"
    VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', 'AP']
    RANK = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '10', '10', '10', '1', '10']
    SUITS_RANKS = ["Spades", "Clubs", "Diamonds", "Hearts"]

    def __init__(self, value, suit, rank):
        self.value = value
        self.suit = suit
        self.rank = rank

    def to_str(self):
        icons = {
            "Hearts": '\u2665',
            "Diamonds": '\u2666',
            "Spades": '\u2663',
            "Clubs": '\u2660',
        }
        return f"{self.value}{icons[self.suit]}"

    def equal_suit(self, other_card):
        return self.suit == other_card.suit
    
    def more(self, other_card):
        if self.value != other_card.value:
            return Card.RANK.index(self.value) > Card.RANK.index(other_card.value)
        else:
            return Card.SUITS_RANKS.index(self.suit) > Card.SUITS_RANKS.index(other_card.suit)

    def less(self, other_card):
        if self.value != other_card.value:
            return Card.RANK.index(self.value) < Card.RANK.index(other_card.value)
        else:
            return Card.SUITS_RANKS.index(self.suit) < Card.SUITS_RANKS.index(other_card.suit)


# card1 = Card("10", Card.HEARTS)
# card2 = Card("A", Card.DIAMONDS)
# 
# if card1.equal_suit(card2):
#     print(f'У карт: {card1.to_str()} и {card2.to_str()} одинаковые масти')
# else:
#     print(f'У карт: {card1.to_str()} и {card2.to_str()} разные масти')

# Задание: Теперь создадим колоду из 52-ух карт и реализуем все методы
class Deck:
    pass
    # TODO: сюда копируем реализацию класса колоды из предыдущего задания
    def __init__(self):
        self.cards = []
        self.create_deck()

    def create_deck(self):
        res = list()
        for suit in [Card.HEARTS, Card.DIAMONDS, Card.SPADES, Card.CLUBS]:
            for value in Card.VALUES:
                res.append(Card(value, suit))
        self.cards = res

    def show(self):
        to_show = [card.to_str() for card in self.cards]
        return f'deck[{len(self.cards)}]: {", ".join(to_show)}'

    def draw(self, number):
        to_show = self.cards[:number]
        self.cards = self.cards[number:]
        return to_show

    def shuffle(self):
        random.shuffle(self.cards)

    # TODO: сюда копируем реализацию класса карты из предыдущего задания
    #  реализуем новые методы



# deck = Deck()
# print(deck.show())
# deck.shuffle()
# print(deck.show())

deck = Deck()
deck.shuffle()
# print(deck.show())
# Берем две карты из колоды
card1, card2 = deck.draw(2)

# Тестируем методы .less() и .more()
if card1.more(card2):
    print(f"{card1.to_str()} больше {card2.to_str()}")
if card1.less(card2):
    print(f"{card1.to_str()} меньше {card2.to_str()}")


# 
# # _________________________
# 
# player_money = 100  # Деньги игрока
# rate_value = 10  # Размер ставки
# 
# deck = Deck()
# 
# 
# def sum_points(cards):
#     """
#     Напишите отдельную функцию для нахождения суммы очков всех карт в списке
#     :param cards: список карт(рука игрока или диллера)
#     :return: сумму очков
#     """
#     # Совет: храните кол-во очков за карту внутри класса Колоды(колода "знает", сколько дает очков каждая карта)
# 
#     #  Сначала считаем сумму карт, считая ТУЗ за 11-очков
#     sum_points = ...
#     # Если сумма > 21, то перечитываем сумму, считая ТУЗ за 1(единицу)
#     if sum_points > 21:
#         ...
# 
#     return sum_points
# 
# 
# while True:
#     # 0. Игрок делает ставку
#     player_money -= rate_value
#     # 1. В начале игры перемешиваем колоду
#     # 2. Игроку выдаем две карты
#     player_cards = ...
#     # 3. Дилер берет одну карту
#     dealer_cards = ...
#     # 4. Отображаем в консоли карты игрока и дилера
#     # 5. Проверяем нет ли у игрока блэкджека (21 очко)
#     if sum_points(player_cards) == 21:
#         # Выплачиваем выигрышь 3 и 2
#         player_money += rate_value * 1.5
#         print("Black Jack!!! Игрок победил")
#         # Заканчиваем игру
#     # Если нет блэкджека, то
#     while True:  # Игрок добирает карты пока не скажет "достаточно" или не сделает перебор (>21)
#         player_choice = input("еще(1)/достаточно(0): ")
#         if player_choice == "1":
#             # Раздаем еще одну карту
#             # Если перебор (>21), заканчиваем добор
#             if sum_points(player_cards) > 21:
#                 print(f"Перебор: {sum_points(player_cards)} очков")
#                 ...
#                 break
#         if player_choice == "0":
#             # Заканчиваем добирать карты
#             break
# 
#     # Если у игрока не 21(блэкджек) и нет перебора, то
#     if ...:
#         print("Диллер добирает карты")
#         while True:  # дилер начинает набирать карты.
#             ...  # Смотри подробные правила добора дилера в задании
# 
#     # Выясняем кто набрал больше очков. Выплачиваем/забираем ставку
#     if sum_points(player_cards) > sum_points(dealer_cards):
#         ...
#     else:
#         ...
