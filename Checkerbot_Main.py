import serial

def ser_init:
	ser=serial.Serial(port='\\.\COM5', baudrate=250000, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=1)
	print(ser.name)
print ser.read(10000)
print ser.write('M119')
print ser.read(10000)
print ser.write('M121')
print ser.read(1000)
print ser.write('G91')
print ser.read(1000)
print ser.write('G1 X100')
print ser.read(1000)
ser.close()