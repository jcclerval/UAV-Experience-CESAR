# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 10:09:02 2016

@author: jc
"""

#!/usr/bin/env python
# coding: utf-8
import socket
import serial

# Creation du Socket ----------------------------------------------------------
Sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
Sock.bind(('', 15550))

# Creation du Serial ----------------------------------------------------------
ser = serial.Serial('/dev/ttyACM0',9600)


# On est a l'ecoute d'une seule et unique connexion ---------------------------
Sock.listen(1)

# Le script se stoppe ici jusqu'a ce qu'il y ait connexion --------------------
client, adresse = Sock.accept()                                                # accepte les connexions de l'exterieur
print "L'adresse",adresse,"vient de se connecter au serveur !"
while 1:
    RequeteDuClient = client.recv(255)                                         # on recoit 255 caracteres grand max
    if not RequeteDuClient:                                                    # si on ne recoit plus rien
        break                                                                  # on break la boucle (sinon les bips vont se repeter)
    print RequeteDuClient,"\a"                                                 # affiche les donnees envoyees, suivi d'un bip sonore

    if (RequeteDuClient =='quit'):
        break

    if (RequeteDuClient == "avant"):
    	ser.write(str("z"))
        
    if (RequeteDuClient == "arriere"):
        ser.write(str("s"))

    if (RequeteDuClient == "gauche"):
        ser.write(str("q"))

    if (RequeteDuClient == "droit"):
        ser.write(str("d"))
 
    if (RequeteDuClient == "stop"):
	ser.write(str("u"))    
    
    
client.close()
Sock.close()
print('Fin de la connexion')
