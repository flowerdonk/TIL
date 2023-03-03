import random

def making_card_list() -> list:
	card_list = []

	for shape in ["spade", "heart", "diamond", "clover"]:

		for number in ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]:

			card_list.append((shape, number))

	return card_list


trump_card_list = making_card_list()

count1, count2 = 0, 0
while count1 < 6 and count2 < 6:
    p1 = random.choice(trump_card_list)
    p2 = random.choice(trump_card_list)

    trump_card_list - p1
    trump_card_list - p2

    if p1[0] == "spade":
        if