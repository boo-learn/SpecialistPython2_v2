# Возьмите классы Deck и Card с GIST'а второго занятия и доработайте их
from practice.BlackJack.deckmodule import Deck, Hand

#class Hand(Deck):
#     NAME = "Hand"
# 
#     def __init__(self, new_cards=[]) -> []:
#         self.cards = []
#         self.points = 0
#         if new_cards is None:
#             return self.cards
#         return self.cards.extend(new_cards)
# 
#     # метод take наследуется
# 
#     def give(self, card: Card = None) -> []:
#         if card in self.cards:
#             self.cards.remove(card)
#             return self.cards
#         else:
#             return None
# 
#     def beat(self, other_card: Card = None) -> []:
#         for card in self.cards:
#             if card.suit == other_card.suit:
#                 if card > other_card:
#                     self.cards.remove(card)
#                     return card
#         return []
# 
#     def sum_points(self):
#         sum = 0
#         for card in self.cards:
#             if card.value in self.points_digits:
#                 sum += int(card.value)
#                 continue
#             if card.value in self.points_ppl:
#                 sum += 10
#                 continue
#             if card.value == 'A':
#                 if sum > 21:
#                     sum += 1
#                     continue
#                 sum += 11
#                 continue
#         return sum


player_money = 100  # Деньги игрока
rate_value = 10  # Размер ставки
deck = Deck()
deck.shuffle()


while True:
    print("\n *** New game ***")
    # 0. Игрок делает ставку
    player_money -= rate_value
    if player_money < 0:
        print("Денег нет, но вы держитесь")
        break
    # 1. В начале игры перемешиваем колоду
    # 2. Игроку выдаем две карты
    # player_cards = ...
    player = Hand(deck.draw(2))
    print("player", player)
    # 3. Дилер берет одну карту
    # dealer_cards = ...
    dealer = Hand(deck.draw(1))
    print("dealer", dealer)
    # 4. Отображаем в консоли карты игрока и дилера
    # 5. Проверяем нет ли у игрока блэкджека (21 очко)
    player.sum_points()
    if player.sum_points() == 21:
        # Выплачиваем выигрышь 3 и 2
        player_money += rate_value * 1.5
        print("Black Jack!!! Игрок победил")
        continue
        # Заканчиваем игру
    # Если нет блэкджека, то
    while True:  # Игрок добирает карты пока не скажет "достаточно" или не сделает перебор (>21)
        player_choice = input("еще(1)/достаточно(0): ")
        if player_choice == "1":
            # Раздаем еще одну карту
            player.take(deck.draw(1))
            print("player", player)
            # Если перебор (>21), заканчиваем добор
            if player.sum_points() > 21:
                print(f"Перебор: {player.sum_points()} очков")
                break
        if player_choice == "0":
            # Заканчиваем добирать карты
            break

    # Если у игрока не 21(блэкджек) и нет перебора, то
    if player.sum_points() <= 21:
        print("Диллер добирает карты")
        while True:  # дилер начинает набирать карты.
            dealer.take(deck.draw(1))
            print("dealer", dealer)
            if dealer.sum_points() < 17:
                continue
            break
        if dealer.sum_points() > 21:
            print(f"Dealer Перебор: {dealer.sum_points()} очков")
            break

    # Выясняем кто набрал больше очков. Выплачиваем/забираем ставку
    if 21 >= player.sum_points() > dealer.sum_points():
        print("Player win!")
    else:
        print("Dealer win!")
