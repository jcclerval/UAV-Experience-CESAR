# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 10:09:02 2016

@author: jc
"""

#!/usr/bin/env python
# coding: utf-8

import socket

hote = "bord3l"
port = 15555

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((hote, port))


print "Connection on {}".format(port)
fermer = 1
while fermer:
    
    variable = raw_input("Entrez un texte : ")
    
    socket.send(variable)
    if variable == "":
        break

print "Close"
socket.close()
