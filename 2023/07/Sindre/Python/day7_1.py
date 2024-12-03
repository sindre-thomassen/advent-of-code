from enum import Enum


FILE = "../input.txt"

with open(FILE) as file:
	lines = file.readlines()
	lines = [(line.split(' ')[0], int(line.split(' ')[1])) for line in lines]

CARD_ORDER = list("AKQT98765432J")[::-1]


class Hand(Enum):
	FIVE_OF_A_KIND = 1
	FOUR_OF_A_KIND = 2
	FULL_HOUSE = 3
	THREE_OF_A_KIND = 4
	TWO_PAIRS = 5
	PAIR = 6
	HIGH_CARD = 7


def get_hand(hand):
	cards = {}

	hand = list(hand)
	for card in hand:
		if card in cards.keys():
			cards[card] += 1
		else:
			cards[card] = 1

	amounts = list(cards.values())

	if 5 in amounts:
		return Hand.FIVE_OF_A_KIND
	elif 4 in amounts:
		return Hand.FOUR_OF_A_KIND
	elif 3 in amounts and 2 in amounts:
		return Hand.FULL_HOUSE
	elif 3 in amounts:
		return Hand.THREE_OF_A_KIND
	elif amounts.count(2) == 2:
		return Hand.TWO_PAIRS
	elif 2 in amounts:
		return Hand.PAIR
	else:
		return Hand.HIGH_CARD


def sort_convert(string):
	res = ""
	for letter in string:
		res += hex(CARD_ORDER.index(letter)+1)[-1]

	return res

HANDS = dict([(hand, []) for hand in Hand])


total = 1

for hand, val in lines:
	t = get_hand(hand)
	HANDS[t].append((hand, val))

for hand_type in Hand:
	HANDS[hand_type] = sorted(HANDS[hand_type], key=lambda x: sort_convert(x[0]))

all_hands = []
for hand_type in Hand:
	all_hands =  HANDS[hand_type] + all_hands

total = 0
for i, hand in enumerate(all_hands):
	total += (i+1)*hand[1]


print("Total score:", total)