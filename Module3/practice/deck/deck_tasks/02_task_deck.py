from deck_total import Card, Deck
 
# TODO: Создайте колоду из 52 карт. Перемешайте ее. Вытяните 10 карт сверху
#   и посчитайте карт какой/каких мастей среди вытянутых карт оказалось больше всего?
 
deck = Deck()
deck.shuffle()
# TODO-final: реализовать нативную работу с объектами:
# 1. Вывод колоды в терминал:
print(deck)  # вместо print(deck.show())
 
hand=deck.draw(10)
print(hand)
 
suit_count={} 
 
for card in hand: # разбросаем количество по мастям
    val=suit_count.get(card.suit,0) # берем старое занчение, если нет, то =0
    suit_count.update({card.suit:(val+1)}) # и увеличиваем на 1 
 
print(suit_count)
max_val=0
 
for key,val in suit_count.items(): 
    if val>max_val:
        max_val=val  # вычислим максимум выпадения макстей
 
max_suit=[]
for key,val in suit_count.items(): 
    if val==max_val:
        max_suit.append(key) # найдем масть или масти с максимальным количеством выпаданием
 
print(len(max_suit),"масть или масти с максимальным количеством выпаданием",max_suit)
# универсальный вариант не зависящий от количества мастей
