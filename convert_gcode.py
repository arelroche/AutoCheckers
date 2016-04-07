# Receive input from Ashis in array (ex. changes[i][j])
# i = change number
# j = 0 (pick/place), 1 (col. letter), 2 (row num.)

import serial
from openpyxl import load_workbook
import serial_comm as comm
from time import sleep

def convert_gcode(ser, moveArray):
    
    wb = load_workbook('GCODE_CONSTANT.xlsx')
    sheet_ranges = wb['Sheet2']

    #disable endstop detection
    #ser.write('M121\n')
    #set to absolute positioning
    ser.write('G90\n')
    ser.read(200)

    for i in range(len(moveArray)):

        if moveArray[i][0] =="discard":
            discard = sheet_ranges['A11'].value
            discard.encode('ascii')
            discard = str(discard)
            comm.ser_command(ser, discard)
            comm.ser_command(ser, 'M107')
            continue

        print "%s at %s%s" %(moveArray[i][0], moveArray[i][1], moveArray[i][2])

        cell = moveArray[i][1] + str(moveArray[i][2])
        pos = sheet_ranges[cell].value
        pos.encode('ascii')
        pos = str(pos)
        print "pos is: %s" % pos
        
        #go to pos
        comm.ser_command(ser, pos)
        #z-down
        #ser.write('G1 Z \n')
        ser.read(200)

        if moveArray[i][0] == 'pick':
            #fan on
            comm.ser_command(ser, 'M106')
            comm.ser_command(ser, 'G1 Z-10')
            sleep(2)
            comm.ser_command(ser, 'G1 Z10')
        else:
            #fan off
            comm.ser_command(ser, 'M107')
            comm.ser_command(ser, 'G1 Z-10')
            sleep(2)
            comm.ser_command(ser, 'G1 Z10')
        
        #z-up
        #ser.write('G1 Z \n')#####
        sleep(1)
    
    #go home (discard)
    home = sheet_ranges['A11'].value
    home.encode('ascii')
    home = str(home)
    comm.ser_command(ser, home)