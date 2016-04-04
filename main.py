import checker_cam as cam
import game_ai as game
import serial_comm as comm
import numpy as np
import convert_gcode as gcode

def main():
	ser = comm.ser_init()	
	while True:
		state = raw_input('"manual" or "auto"? :')
		
		if (state == "manual"):
			comm.ser_arduino(ser)

		elif (state == "auto"):
			computer_play()
		else:
			print "Hmm, try again."

def computer_play():
	board =  cam.take_picture(mirror=False)

	board_next = game.next_move(board)

	moves = game.moveparse(board, board_next)

	print moves

	gcode.convert_gcode(moves, ser)

if __name__ == '__main__':
	main()
