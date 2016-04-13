# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 15:23:00 2016

@author: jc
"""
#Importation des bibliothèques nécessaires ------------------------------------

import pygame

from pygame.locals import *
import socket                                                                  # on importe le module
Sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)                        # on cree notre socket

 
# Definition des informations -------------------------------------------------
# Host = '192.168.43.151'
Host = '10.42.0.14'
Port = 15550

# On se connecte sur le serveur avec les informations ci-dessus
# Assurez-vous d'avoir mis en marche le serveur !
Sock.connect((Host,Port))

# Lancemement de PyGame -------------------------------------------------------
pygame.init()


# Ouverture de la fenêtre Pygame ----------------------------------------------

fenetre = pygame.display.set_mode((640, 480))


# Chargement et collage du fond -----------------------------------------------

fond = pygame.image.load("background.jpg").convert()

fenetre.blit(fond, (0,0))


# Chargement et collage du personnage -----------------------------------------

perso = pygame.image.load("perso.png").convert_alpha()

position_perso = perso.get_rect()

fenetre.blit(perso, position_perso)


# Rafraîchissement de l'écran -------------------------------------------------

pygame.display.flip()


# On compte les joysticks -----------------------------------------------------

nb_joysticks = pygame.joystick.get_count()

# BOUCLE INFINIE --------------------------------------------------------------

continuer = 1
pygame.key.set_repeat(10, 50)


if nb_joysticks > 0:
    mon_joystick = pygame.joystick.Joystick(0)


    mon_joystick.init()
    
    while continuer:
        for event in pygame.event.get():
            if event.type == QUIT:
                print("Fermeture de la connexion")
                continuer = 0
                
            x = mon_joystick.get_axis(0);
            x = int(x*100)
            y = mon_joystick.get_axis(1);
            y = int(y*100)
                       
            data = (x,y)
            Sock.send(data)
            position_perso = position_perso.move(int(x/10),int(y/10)
        # Re-collage ----------------------------------------------------------

        fenetre.blit(fond, (0,0))   

        fenetre.blit(perso, position_perso)

        # Rafraichissement ----------------------------------------------------

        pygame.display.flip()

    while continuer:

        for event in pygame.event.get():                                       # Attente des événements
        
            if event.type == QUIT:
                print("Fermeture de la connexion")
                continuer = 0

            if event.type == KEYDOWN:
                
                if event.key == K_DOWN:                                        # Si "flèche bas"
                    position_perso = position_perso.move(0,3)
                    Sock.send('arriere')                                       # On envoie ces donnees
            
                if event.key == K_UP:                                          # Si "flèche haut"
                    position_perso = position_perso.move(0,-3)
                    Sock.send('avant')                                         # On envoie ces donnees
                
                if event.key == K_RIGHT:                                       # Si "flèche droite"
                    position_perso = position_perso.move(3,0)
                    Sock.send('droit')                                         # On envoie ces donnees
            
                if event.key == K_LEFT:                                        # Si "flèche gauche"
                    position_perso = position_perso.move(-3,0)
                    Sock.send('gauche')                                        # On envoie ces donnees

                if event.key == K_SPACE:                                       # Si "flèche gauche"
                    position_perso = position_perso.move(-3,0)
                    Sock.send('stop')                                          # On envoie ces donnees


    

        # Re-collage ----------------------------------------------------------

        fenetre.blit(fond, (0,0))   

        fenetre.blit(perso, position_perso)

        # Rafraichissement ----------------------------------------------------

        pygame.display.flip()
    
print("Fin du script")

