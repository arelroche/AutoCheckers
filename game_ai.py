import numpy as np
from StringIO import StringIO

def next_move(board):
	board_next = np.chararray((10,10))
	board_next = board
	np.savetxt('board_next.txt', board_next, delimiter=" ", fmt ="%s")
	
	board_next = np.genfromtxt('test_next.txt', dtype=str)
	
	for num in range(10):
		for letter in ('ABCDEFGHIJ'):
			print board_next[num][ord(letter)-65],
		print
	print('-------------------')

	return board_next

def moveparse(action):
	moves =[]
	current_action = action 
	current_action.source = (10 - current_action.source[0], 10 - current_action.source[1])
	current_action.destination = (10 - current_action.destination[0], 10 - current_action.destination[1])
	
	while current_action != None:
		if current_action.type == "MOVE":
			moves.append(("pick", chr(current_action.source[1]+65), current_action.source[0]))
			moves.append(("place", chr(current_action.destination[1]+65), current_action.destination[0]))

		if current_action.type == "CAPTURE":
			moves.append(("pick", chr(current_action.source[1]+65), current_action.source[0]))
			moves.append(("place", chr(current_action.destination[1]+65), current_action.destination[0]))
			remove = [chr((current_action.source[1]+current_action.destination[1])/2 + 65), (current_action.source[0]  + current_action.destination[0])/2]
			moves.append(("pick", remove[0], remove[1]))
			moves.append(("discard", 0, 0))

		current_action = current_action.next
	print moves
	return moves	


def boardparse(board, board_next):
	#board = np.genfromtxt("test.txt", dtype=str)

	moves = "No change detected"
	changes = 0
	x_pick = 0
	x_place = 0
	o_pick = 0
	o_place = 0

	change = []

	for num in range(10):
		for letter in ('ABCDEFGHIJ'):
			old = board[num, ord(letter)-65]
			new = board_next[num, ord(letter)-65]
			if (old != new):
				if (old == "x" or new == "x"):
					changes +=1
					moves = " %d new moves have been made!" % changes
					if (new == "."):
						change.append(("pick", letter, num+1))
						x_pick+=1
					else:
						change.append(("place", letter, num+1))
						x_place+=1
	if (x_pick>x_place):
		change.append(("discard", 0, 0))
	if (x_place > 1):
		if (change[0][0] == "place"):
			temp = change [0]
			change[0] = change[1]
			change[1] = temp

	change_len = len(change)

	for num in range(10):
		for letter in ('ABCDEFGHIJ'):
			old = board[num, ord(letter)-65]
			new = board_next[num, ord(letter)-65]
			if (old != new):
				if (old == "o" or new == "o"):
					changes += 1
					moves = " %d new moves have been made!" % changes
					if (new == "."):
						change.append(("pick", letter, num+1))
						o_pick+=1
					else:
						change.append(("place", letter, num+1))
						o_place+=1
	if (o_pick>o_place):
		change.append(("discard", 0, 0))

	if (o_place > 1):
		if change[change_len][0] == "place":
			temp = change [0]
			change[0] = change[1]
			change[1] = temp

	print moves
	return change
