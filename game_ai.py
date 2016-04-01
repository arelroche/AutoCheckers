import numpy as np

def next_move(board):
	np.savetxt('board_next.txt', board, delimiter=" ", fmt ="%s")
	return board

def moveparse(board, board_next):
	moves = np.zeros((2,2))
	return moves
