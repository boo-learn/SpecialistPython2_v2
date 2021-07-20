class Card:
	def __init__(self, value, suit):
		self.value = value
		self.suit = suit
	
	def to_str(self):
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


hearts_cards = []
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
for value in values:
	hearts_cards.append(Card(value, 'Hearts'))


diamonds_cards = []
for value in values:
	diamonds_cards.append(Card(value, 'Diamonds'))


spades_cards = []
for value in values:
	spades_cards.append(Card(value, 'Spades'))


clubs_cards = []
for value in values:
	clubs_cards.append(Card(value, 'Clubs'))

cards = []


for card in (hearts_cards + diamonds_cards + spades_cards + clubs_cards):
	cards.append(card)


cards_str = cards[0].to_str()
for card in cards[1:]:
	cards_str += ',' + card.to_str()


print(cards_str)
