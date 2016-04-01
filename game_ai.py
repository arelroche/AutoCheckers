import numpy as np
from StringIO import StringIO

def next_move(board):
	board_next = np.chararray((10,10))
	board_next = board
	np.savetxt('board_next.txt', board_next, delimiter=" ", fmt ="%s")
	
	test = open('test_next.txt', 'r')
	board_next = np.genfromtxt(StringIO(test))
	# with open("test_next.txt") as f:
	# 	content = f.read()
	# print list(content)
	
	board_next = np.genfromtxt('test_next.txt', dtype=str)
	
	for num in range(10):
		for letter in ('ABCDEFGHIJ'):
			print board_next[num][ord(letter)-65],
		print
	print('-------------------')

	return board_next

def moveparse(board, board_next):
	moves = "No change detected"
	changes = 0
	change = []

	for num in range(10):
		for letter in ('ABCDEFGHIJ'):
			old = board[num, ord(letter)-65]
			new = board_next[num, ord(letter)-65]
			if (old != new):
				moves = "new moves have been made!"
				if (new == "."):
					change.append(("pick", letter, num))
				else:
					change.append(("place", letter, num))
	print moves
	return change
