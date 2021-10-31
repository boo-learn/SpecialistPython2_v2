class Card:
    pass
    # TODO: сюда копируем реализацию класса карты из предыдущего задания


cards = []
# TODO-1: в список cards добавьте ВСЕ карты всех мастей

# TODO-2: Выведите карты в формате: cards[кол-во]2♥, 3♥, 4♥ ... A♥, 2♦, 3♦ ... A♦, ....
icon_suits = ('\u2661',  '\u2662',  '\u2667',  '\u2664')
ranks = ('2','3','4','5','6','7','8','9','10','T','J','Q','K','A')

for i in icon_suits:
    for j in ranks:
        cards.append(j+i)
print(*cards,sep=',')
