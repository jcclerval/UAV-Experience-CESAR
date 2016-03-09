# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 10:09:44 2016

@author: jc
"""

#!/usr/bin/env python
# coding: utf-8

import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('', 15555))

while True:
        socket.listen(5)
        client, address = socket.accept()
        print "{} connected".format( address )

        response = client.recv(255)
        if response != "":
                print response

print "Close"
client.close()
socket.close()