# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 19:04:37 2016

@author: jc

Script permettant de controler de robot
"""


# Import phase ----------------------------------------------------------------

import sys
import serial

# Définition des variables ----------------------------------------------------
ser = serial.Serial('/dev/tty.usbserial', 9600)

was_dark = False


# Boucle ----------------------------------------------------------------------

while 1:
    line = ser.readline()
    if int(line) < 200 and not was_dark: # Adapt the value to your component
        print 'Its dark here, would you turn on the light ?'
        was_dark = True
    elif int(line) > 200 and was_dark:
        print 'Oh, it is light enough now.'
        was_dark = False