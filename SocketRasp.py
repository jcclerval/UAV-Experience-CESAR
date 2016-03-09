# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 10:09:02 2016

@author: jc
"""

#!/usr/bin/env python
# coding: utf-8

import socket # on importe le module
Sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # on cree notre socket
 
# definition des informations :
Host = 'bord3l'
Port = 234
 
# on se connecte sur le serveur avec les informations ci-dessus
# assurez-vous d'avoir mis en marche le serveur !
Sock.connect((Host,Port))
 
# On est connecte, on fait une boucle infinie d'inputs pour l'envoi des messages :
while 1:
        msg = raw_input('>> ')  # on rentre des donnees
        Sock.send(msg) # on envoie ces donnees
 
# regardez ce qui se passe du cote serveur.
