import socket,os
from PIL import *
import pygame,sys
import pygame.camera
from pygame.locals import *

#Create server:
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("10.16.155.25",5000))
server.listen(5)

#Start Pygame
pygame.init()
pygame.camera.init()

screen = pygame.display.set_mode((320,240))

cam = pygame.camera.Camera("/dev/video0",(320,240),"RGB")
cam.start()

#Send data
while True:
    s,add = server.accept()
    print "Connected from",add
    image = cam.get_image()
#    data = image.tostring('raw','RGB')
#    data = image.convert('RGBA').tostring('raw','RGBA')
    data = cam.get_raw()
    s.sendall(data)

#Interupt
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
