# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 10:51:22 2016

@author: jc
"""
import socket
Sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.bind(('', 234))
# On est a l'ecoute d'une seule et unique connexion :
Sock.listen(1)
 
# Le script se stoppe ici jusqu'a ce qu'il y ait connexion :
client, adresse = Sock.accept() # accepte les connexions de l'exterieur
print "L'adresse",adresse,"vient de se connecter au serveur !"
while 1:
        RequeteDuClient = client.recv(255) # on recoit 255 caracteres grand max
        if not RequeteDuClient: # si on ne recoit plus rien
                break  # on break la boucle (sinon les bips vont se repeter)
        print RequeteDuClient,"\a"         # affiche les donnees envoyees, suivi d'un bip sonore