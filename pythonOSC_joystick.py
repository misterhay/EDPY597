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

def sendOSC(button, state):
   message = OSC.OSCMessage('/output/'+str(button))
   message.append(state)
   client.send(message)

#sendOSC(2, 0)

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
            print event.button
            sendOSC(event.button, 1)
         if event.type == 11: # button up
            print event.button
            sendOSC(event.button, 0)
except KeyboardInterrupt:
   print 'Done'
