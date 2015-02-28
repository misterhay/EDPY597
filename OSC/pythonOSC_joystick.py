#!/usr/bin/python

# change this to the IP address and port that will receive our OSC messages, if applicable
remoteIP = '10.0.0.111'
remotePort = 9000

import time, threading
import OSC # requires pyOSC from https://trac.v2.nl/wiki/pyOSC or https://gitorious.org/pyosc
import pygame

sendAddress = (remoteIP, remotePort)
client = OSC.OSCClient() # set up then connect to the OSC receiving server
client.connect((sendAddress)) #not sure if we need both sets of parentheses

def sendOSC(pin, state):
   message = OSC.OSCMessage('/output/'+str(pin))
   message.append(state)
   print message
   client.send(message)

pygame.init()
joystickCount = pygame.joystick.get_count()
print (joystickCount, 'joystick(s)')
if joystickCount == 0:
   print ('no joysticks attached')
else:
   joystickInput = pygame.joystick.Joystick(0)
   joystickInput.init()

try:
   while 1:
      for event in pygame.event.get():
         if event.type == 10: # button down
            #print event.button
            pin = event.button + 1 # since the buttons start at 0
            #print pin
            sendOSC(pin, 1) 
         if event.type == 11: # button up
            pin = event.button + 1
            sendOSC(pin, 0)
         #if event.type == 7: # axis move
            #print event.axis
            #print event.value  
      pygame.event.clear()
except KeyboardInterrupt:
   print 'Done'
