import random


class Card:
	def __init__(self, value, suit):
		self.value = value
		self.suit = suit
	
	def __str__(self):
		if self.suit == 'Hearts':
			return f"{self.value}♥"
		elif self.suit == 'Diamonds':
			return f"{self.value}♦"
		elif self.suit == 'Spades':
			return f"{self.value}♠"
		elif self.suit == 'Clubs':
			return f"{self.value}♣"

	def equal_suit(self, other_card):
		return self.suit == other_card.suit

	def __gt__(self, other_card):
		power = {'J':'11', 'Q':'12', 'K':'13', 'A':'14'}
		rewop = {'11':'J', '12':'Q', '13':'K', '14':'A'}
		self.value = power.setdefault(self.value, self.value)
		other_card.value = power.setdefault(other_card.value, other_card.value)
		if int(self.value) != int(other_card.value):
			answ = int(self.value) > int(other_card.value)
		else:
			answ = None
		self.value = rewop.setdefault(self.value, self.value)
		other_card.value = rewop.setdefault(other_card.value, other_card.value)
		return answ

	def __lt__(self, other_card):
		if (self > other_card) != None:
			return not self > other_card


class Deck:
	def __init__(self):
		cards = []
		values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
		suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
		self.last_index_card = None
		for suit in suits:
			for value in values:
				cards.append(Card(value, suit))
		self.cards = cards

	def __str__(self):
		cards_str = str(self.cards[0])
		for card in self.cards[1:]:
			cards_str += ',' + str(card)
		return f'deck[{len(self.cards)}]: {cards_str}'

	def __iter__(self): 
		return self

	def __next__(self):
		if self.last_index_card is None:
			self.last_index_card = 0
		else:
			self.last_index_card += 1
		if self.last_index_card >= len(self.cards):
			raise StopIteration
		return self.cards[self.last_index_card]

	def	__getitem__(self, index):
		return self.cards[index-1]

	def draw(self, x):
		cards_list = []
		for i in range(0, x):
			poppet = self.cards.pop(0)
			cards_list.append(poppet)
		return cards_list

	def shuffle(self):
		return random.shuffle(self.cards)


deck = Deck()
# Задачи - реализовать нативную работу с объектами:
# 1. Вывод колоды в терминал:
print(deck)  # вместо print(deck.show())

card1, card2 = deck.draw(2)
# 2. Вывод карты в терминал:
print(card1)  # вместо print(card1.to_str())

# 3. Сравнение карт:
if card1 > card2:
    print(f"{card1} больше {card2}")

# 4. Итерация по колоде:
for card in deck:
    print(card)

# 5. Просмотр карты в колоде по ее индексу:
print('lst', deck[6])
