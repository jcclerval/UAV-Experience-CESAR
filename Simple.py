# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 16:17:05 2016

@author: jc
"""

import socket                                                                  # on importe le module
Sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)                        # on cree notre socket

 
# definition des informations -------------------------------------------------
Host = '10.16.155.25'
Port = 15550

 
# on se connecte sur le serveur avec les informations ci-dessus
# assurez-vous d'avoir mis en marche le serveur !
Sock.connect((Host,Port))

 
# On est connecte, on fait une boucle infinie d'inputs pour l'envoi des messages :
while 1:
        msg = raw_input('>> ')  # on rentre des donnees
        Sock.send(msg) # on envoie ces donnees
 
# regardez ce qui se passe du cote serveur.
 