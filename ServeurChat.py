# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 10:51:22 2016

@author: jc
"""

import socket


socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('', 15555))

while True:
        socket.listen(7)
        client, address = socket.accept()
        print "{} connected".format( address )
        response = ""
        while(response != "quit"):
            response = client.recv(255)
            if response != "":
                print response
            client.close()
            if response == 'quit':
                break
        client.close()
        socket.close()
        print('Connexion terminée')

print "Close"
client.close()
