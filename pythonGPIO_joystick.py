#!/usr/bin/python

####### Change settings in this section #######

# specify the output pins you will be using (in BCM style)
outputs = [2, 3, 4, 17, 27, 22, 10, 9, 14, 15, 18, 23, 24, 25, 8, 7]

# set to False if using LEDs or True if using a relay board (which activates on LOW)
relayBoard = True

####### End of settings section #######

import pygame
## remove the double-pound comments to turn on GPIO functions
##import RPi.GPIO as GPIO
##GPIO.setmode(GPIO.BCM)

pygame.init()
joystickCount = pygame.joystick.get_count()
print (joystickCount, 'joystick(s)')
if joystickCount == 0:
   print ('no joysticks attached')
else:
   joystickInput = pygame.joystick.Joystick(0)
   joystickInput.init()

outputNumber = 0 # this is the first output, we'll iterate from here
for pin in outputs: # iterate through pins to set them up and make sure they are off
   outputNumber = outputNumber + 1 # iterate the counting variable
##   GPIO.setup(pin, GPIO.OUT)
   if relayBoard == True:
      print 'making sure the relay pin', pin, 'is off'
##      GPIO.output(pin, GPIO.HIGH)
print 'we set up', outputNumber, 'pins as outputs'

def setPin(pin, state):
   if relayBoard == True:
      if state == 0: # will invert the output if you set relayBoard to True
         state = 1
      else:
         state = 0
   if state == 0:
##      GPIO.output(pin, GPIO.LOW) # turn off the pin
      print pin, 'off'
   if state == 1:
##      GPIO.output(pin, GPIO.HIGH) # turn on the pin
      print pin, 'on'

try:
   while 1:
      for event in pygame.event.get():
         if event.type == 10: # button down
            #print event.button
            pin = event.button + 1 # since the buttons start at 0
            #print pin
            setPin(pin, 1) 
         if event.type == 11: # button up
            pin = event.button + 1
            setPin(pin, 0)
         #if event.type == 7: # axis move
            #print event.axis
            #print event.value  
      pygame.event.clear()
except KeyboardInterrupt:
   print 'Done'
