#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as io
io.setmode(io.BCM)

in1_pin = 4
in2_pin = 17

io.setup(in1_pin, io.OUT)
io.setup(in2_pin, io.OUT)

def set(property, value):
    try:        
        f = open("/sys/class/rpi-pwm/pwm0/" + property, 'w')
        f.write(value)
        f.close()     
    except:        
        print("Erreur durant l ecriture de: " + property + " valeur: " + value) 

set("delayed", "0")
set("mode", "pwm")
set("frequency", "500")
set("active", "1")

# clockwise signifie "sens horlogique" donc marche avant
def clockwise():
    io.output(in1_pin, True)
    io.output(in2_pin, False)

# clockwise signifie "sens anti-horlogique" donc marche arriere
def counter_clockwise():
    io.output(in1_pin, False)
    io.output(in2_pin, True)

# passer en marche avant
clockwise()

while True:
    # demander une saisie de commande a l'utilisateur
    cmd = raw_input("Commande, f/r 0..9, exemple f5 :")

    # la direction est f pour forward (avant) et r pour rearward (arrière)
    direction = cmd[0]
    if direction == "f":
        clockwise()
    else:
         counter_clockwise()

    # la vitesse 
    speed = int(cmd[1]) * 11
    set("duty", str(speed))
