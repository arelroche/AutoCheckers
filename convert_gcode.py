# Receive input from Ashis in array (ex. changes[i][j])
# i = change number
# j = 0 (pick/place), 1 (col. letter), 2 (row num.)

import serial
from openpyxl import load_workbook

def convert_gcode(moveArray, ser):
    
    wb = load_workbook('GCODE_CONSTANT.xlsx')
    sheet_ranges = wb['Sheet2']

    #disable endstop detection
    ser.write('M121\n')
    #set to absolute positioning
    ser.write('G90\n')

    for i in range(len(moveArray)):
        cell = moveArray[i][1] + str(moveArray[i][2])
        pos = sheet_ranges[cell].value
        
        #go to pos
        ser.write(pos + '\n')
        #z-down
        ser.write('G1 Z \n')#####

        if moveArray[i][0] == 'pick':
            #fan on
            ser.write('M106\n')
        else:
            #fan off
            ser.write('M107\n')
        
        #z-up
        ser.write('G1 Z \n')#####
    
    #go home (discard)
    ser.write(sheet_ranges['A11'].value)