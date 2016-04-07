import sys
sys.path.insert(0, 'AutoCheckers')

import checker_cam as cam
import game_ai as game
import serial_comm as comm
import numpy as np
from convert_gcode import convert_gcode as move
import testCheckers as ai

def main():
	#ser = comm.ser_init()
	ser = None

	while True:
		state = raw_input('"manual" or "auto"? :')
		
		if (state == "manual"):
			comm.ser_arduino(ser)

		elif (state == "auto"):
			computer_play(ser)
		else:
			print "Hmm, try again."

def computer_play(ser):
	
	while True:

		#board =  cam.take_picture(mirror=False)

		#### code for new board goes here ####
		#moveArray = robotexec(board)

		moves = ai.ai_move()
		print moves

		moves = game.moveparse(moves)

		#move(ser,moves)
		#board_next = np.genfromtxt('test_next.txt', dtype=str)

		#moves = game.boardparse(board, board_next)

		print moves
		
		move(ser,moves)

		print "Your turn."

		next = raw_input('Enter any command for the computer to continue')




if __name__ == '__main__':
	main()