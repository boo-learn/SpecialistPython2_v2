# Создайте колоду из 52 карт. Перемешайте ее. Вытяните 10 карт сверху
# и посчитайте карт какой/каких мастей среди вытянутых карт оказалось больше всего?
from deck_total import Deck

deck = Deck()
deck.shuffle()
hand_cards = deck.draw(10)
suits_count = {}
for hand_card in hand_cards:
    if hand_card.suit in suits_count.keys():
        suits_count[hand_card.suit] += 1
    else:
        suits_count.update({hand_card.suit: 1})
suits_count = sorted(suits_count.items(), key=lambda item: item[1])
max_suit = suits_count.pop()
res_str = f'Больше всего выпало карт: \n{max_suit[0]} - {max_suit[1]} шт.'
for el in suits_count:
    if el[1] == max_suit[1]:
        res_str += f'\n{el[0]} - {el[1]} шт.'
print(res_str)
