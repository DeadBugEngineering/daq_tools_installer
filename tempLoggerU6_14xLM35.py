# -*- coding: utf-8 -*-
"""
Logging of up to 14 LM35 temperature sensors connected to AIN[0..13] on a Labjack U6.
"""
import sys
import select
import os
import csv
import numpy
from matplotlib import pyplot as plt
import datetime
import u6
import time
from pathlib import Path
home = str(Path.home())

# edit the names of each LM35 sensor here to make the CSV-file more readable.
tempA0 = 'LM35A0'
tempA1 = 'LM35A1'
tempA2 = 'LM35A2'
tempA3 = 'LM35A3'
tempA4 = 'LM35A4'
tempA5 = 'LM35A5'
tempA6 = 'LM35A6'
tempA7 = 'LM35A7'
tempA8 = 'LM35A8'
tempA9 = 'LM35A9'
tempA10 = 'LM35A10'
tempA11 = 'LM35A11'
tempA12 = 'LM35A12'
tempA13 = 'LM35A13'

lj = u6.U6()
lj.getCalibrationData()

def conv2temp(LM35_out):
    return round(LM35_out * 100.0, 2)

try:
    begin = datetime.datetime.now()

    filename = home+'/rawData/tempLog/' + str(begin.year) + '_' + str(begin.month) + '_' + str(begin.day) + '_' + str(begin.hour) + '_' + str(begin.minute) + '_' + str(begin.microsecond)
    fo = open(filename + '.csv', 'w')
    fo.write('time_sec, '+tempA0+', '+tempA1+', '+tempA2+', '+tempA3+', '+tempA4+', '+tempA5+', '+tempA6+', '+tempA7+', '+tempA8+', '+tempA9+', '+tempA10+', '+tempA11+', '+tempA12+', '+tempA13+'\n')
    fo.close()

    currentDataset = ''

    while True:
        now = datetime.datetime.now()
        t_delta = now - begin
        temp0 = conv2temp(lj.getAIN(0, resolutionIndex=12, gainIndex=0 ))
        temp1 = conv2temp(lj.getAIN(1, resolutionIndex=12, gainIndex=0 ))    
        temp2 = conv2temp(lj.getAIN(2, resolutionIndex=12, gainIndex=0 ))
        temp3 = conv2temp(lj.getAIN(3, resolutionIndex=12, gainIndex=0 ))    
        temp4 = conv2temp(lj.getAIN(4, resolutionIndex=12, gainIndex=0 ))
        temp5 = conv2temp(lj.getAIN(5, resolutionIndex=12, gainIndex=0 ))    
        temp6 = conv2temp(lj.getAIN(6, resolutionIndex=12, gainIndex=0 ))
        temp7 = conv2temp(lj.getAIN(7, resolutionIndex=12, gainIndex=0 ))  
        temp8 = conv2temp(lj.getAIN(8, resolutionIndex=12, gainIndex=0 ))
        temp9 = conv2temp(lj.getAIN(9, resolutionIndex=12, gainIndex=0 ))    
        temp10 = conv2temp(lj.getAIN(10, resolutionIndex=12, gainIndex=0 ))
        temp11 = conv2temp(lj.getAIN(11, resolutionIndex=12, gainIndex=0 ))  
        temp12 = conv2temp(lj.getAIN(12, resolutionIndex=12, gainIndex=0 ))
        temp13 = conv2temp(lj.getAIN(13, resolutionIndex=12, gainIndex=0 ))    

        #os.system('cls' if os.name == 'nt' else 'clear')
        fo = open(filename + '.csv', 'a')
        currentDataset = str(t_delta.total_seconds()) + ', ' + str(temp0) + ', ' + str(temp1) + ', ' + str(temp2) + ', ' + str(temp3) + ', ' + str(temp4) + ', ' + str(temp5) + ', ' + str(temp6) + ', ' + str(temp7) + ', ' + str(temp8) + ', ' + str(temp9) + ', ' + str(temp10) + ', ' + str(temp11) + ', ' + str(temp12) + ', ' + str(temp13) + '\n'
        fo.write(currentDataset)
        fo.close()
        print (currentDataset)
        print ("ctrl + c to exit\n")
        time.sleep(1)    # approx waiting time between samples

finally:
    lj.close()
