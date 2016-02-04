# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 08:59:19 2016

@author: jc
"""

###############################################################################
#                                                                             #
#                                                                             #
#                       Controle de la machine                                #
#                                                                             #
#                                                                             # 
###############################################################################

# C'est parti !!

# Importation des bibliothèques -----------------------------------------------

import time                                                                    # Importation de la bibliothèque time
import cv2
import sys

# Définition des variables ----------------------------------------------------



t = time.time()

# Début du script -------------------------------------------------------------

print ('début du script')

# Boncle principale
while(True):
    
    
    # détection interactions utilisateur (codé ici car pratique avec opencv)
    k = cv2.waitKey(0)
    user_input = ''
    
    # début mission
    if k == ord('s'):
      print ('start')
    # arrêt mission
    if k == ord('a'):
      print ('abort')
    # arrêt hard mission
    if k == ord('e'):
      print ('emergency')
    # fin du programme
    if k == ord('q'):
      print ('quit')
    if k == ord('m'):
      print ('manuel')
print ('fin du script')
   