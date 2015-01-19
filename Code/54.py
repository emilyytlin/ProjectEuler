from enum import Enum
import collections

class OrderedEnum(Enum):
	def __lt__(self, other):
		if self.__class__ is other.__class__:
			return self._value_ < other._value_
		return NotImplemented

class Rank(OrderedEnum):
	__ordered__ = 'high_card pair pair2 triple straight flush full_house four straight_flush'
	high_card = 1
	pair = 2
	pair2 = 3
	triple = 4
	straight = 5
	flush = 6
	full_house = 7
	four = 8
	straight_flush = 9

class Card:
	def __init__(self, value, suit):
		self.value = int(value)
		self.suit = suit
	def __lt__(self, other):
		return int(self.value) > int(other.value) #backwards sorting
	def __eq__(self, other):
		return int(self.value) == int(other.value)
	def __hash__(self):
		return hash(int(self.value))

def count_repeats(deck):
	relevant = []
	counter = collections.Counter(deck)
	counter = counter.most_common(5)
	card = Card(0, 0)
	for freq in counter:
		if freq[1] > 1:
			relevant.append((freq[0], freq[1]))
		elif freq[1] == 1:
			if int(card.value) < int(freq[0].value):
				card = freq[0]
	if len(relevant) > 1 and relevant[0][1] == relevant[1][1]:
		if relevant[0][0] > relevant[1][0]:
			temp = relevant[0]
			relevant[0] = relevant[1]
			relevant[1] = temp
	if card.value > 0:
		relevant.append((card, 1))
	return relevant

def is_straight(deck):
	value = deck[0].value+1
	for card in deck:
		if card.value == value-1:
			value -= 1
		else:
			return False
	return True

def is_flush(deck):
	suit = deck[0].suit
	for card in deck:
		if card.suit != suit:
			return False
	return True

def convert_value(n):
	if (n == 'T'):
		return 10
	elif (n == 'J'):
		return 11
	elif (n == 'Q'):
		return 12
	elif (n == 'K'):
		return 13
	elif (n == 'A'):
		return 14
	else: 
		return n

def get_rank(deck):
	flush = is_flush(deck)
	straight = is_straight(deck)
	repeats = count_repeats(deck)
	ranks = []
	if flush and straight:
		return [(Rank.straight_flush, deck[4].value)]
	if repeats[0][1] == 4:
		ranks.append((Rank.four, repeats[0][0].value))
	elif repeats[0][1] == 3 and repeats[1][1] == 2:
		ranks.append((Rank.full_house, repeats[0][0].value))
		ranks.append((Rank.full_house, repeats[1][0].value))
	if flush:
		ranks.append((Rank.flush, 0))
	if straight:
		ranks.append((Rank.straight, deck[4].value))
	if repeats[0][1] == 3 and repeats[1][1] != 2:
		ranks.append((Rank.triple, repeats[0][0].value))
	elif repeats[0][1] == 2 and repeats[1][1] == 2:
		ranks.append((Rank.pair2, repeats[0][0].value))
		ranks.append((Rank.pair2, repeats[1][0].value))
	elif repeats[0][1] == 2 and repeats[1][1] != 2:
		ranks.append((Rank.pair, repeats[0][0].value))
	if repeats[len(repeats)-1][1] == 1:
		ranks.append((Rank.high_card, repeats[len(repeats)-1][0].value))
	return ranks
		
def is_win(deck1, deck2):
	rank1 = get_rank(deck1)
	rank2 = get_rank(deck2)
	for i, rank in enumerate(rank1):
		if i >= len(rank2):
			return True
		if rank1[i][0] > rank2[i][0]:
			return True
		elif rank1[i][0] == rank2[i][0]:
			if rank1[i][1] > rank2[i][1]:
				return True
			elif rank1[i][1] == rank2[i][1]:
				continue
			else:
				return False
		else:
			return False

ans = 0
with open('54.txt', 'r') as f:
	decks = f.readlines()
	for hand in decks:
		hand = hand.split()
		converted_hand = []
		for card in hand:
			converted_hand.append(Card((convert_value(card[0])), card[1]))
		p1 = sorted(converted_hand[0:5])
		p2 = sorted(converted_hand[5:10])
		if is_win(p1, p2):
			ans += 1
print(ans)