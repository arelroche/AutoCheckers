import serial
from time import sleep

def ser_init():
	ser=serial.Serial(port='\\.\COM5', baudrate=250000, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=1)
	print(ser.name)
	return ser

def ser_arduino(ser):
	while True:
		print ser.read(1000)
		sleep(2)
		command = raw_input('"manual" or "automatic"? :')
		print "Sending %s" % command
		print ser.write(command)
		print ser.read(1000)
		sleep(2)




	# print ser.read(10000)
	# print ser.write('M121')
	# print ser.read(1000)
	# print ser.write('G91')
	# print ser.read(1000)
	# print ser.write('G1 X100')
	# print ser.read(1000)
	