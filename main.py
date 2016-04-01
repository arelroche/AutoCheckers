import checker_cam as cam
import game_ai as game
import serial_comm as comm
import numpy as np

def main():
	#ser = comm.ser_init()	
	while True:
		state = raw_input('"manual" or "automatic"? :')
		
		if (state == "manual"):
			comm.ser_arduino(ser)

		if (state == "automatic"):
			computer_play()

def computer_play():
	board =  cam.take_picture(mirror=False)

	board_next = game.next_move(board)

	moves = game.moveparse(board, board_next)

	print moves

if __name__ == '__main__':
	main()