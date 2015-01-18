#!/usr/bin/python
#this depends on RPi.GPIO https://pypi.python.org/packages/source/R/RPi.GPIO/

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
pins = [2, 3, 4, 17, 27, 22, 10, 9, 11, 14, 15, 18, 23, 24, 25, 8, 7]
for pin in pins: #iterate through the array list declared above
    GPIO.setup(pin, GPIO.OUT) #set up the pin as an output
    GPIO.output(pin, 1) #turn the pin off (0 is on)

from Tkinter import * #for the interface

#define a function for setting the pin states, so that we can call it later
def pinOut(pin, state):
    print pin, state #remember that for the pin state 1 means off and 0 means on
    if state == 'on':
        stateNumber = 0
    if state == 'off':
        stateNumber = 1
    GPIO.output(i, stateNumber) #

def setAll(state):
    print 'Turning them all', state
    if state == 'on':
        stateNumber = 0
    if state == 'off':
        stateNumber = 1
    for pin in pins:
        GPIO.output(pin, stateNumber)
        print pin, state

controlWindow = Tk() #we're going to create a window full of buttons
controlWindow.title('GPIO Output Buttons') #set the title of the window
onColour = 'green' #the colour of the on buttons we'll use below
offColour = 'red' #the colour of the off buttons
columnNumber = 0 #initialize a variable for counting the columns

for pin in pins:
    #make two buttons (on and off) for each pin in the array declared above
    #
    Button(controlWindow, text=pin, background=onColour, command=lambda pin=pin: pinOut(pin, 'on')).grid(row=1, column=columnNumber)
    Button(controlWindow, text=pin, background=offColour, command=lambda pin=pin: pinOut(pin, 'off')).grid(row=2, column=columnNumber)
    columnNumber = columnNumber + 1 #increase this variable by one to prepare for the next iteration
Button(controlWindow, text='all', background=onColour, command=lambda: setAll('on')).grid(row=1, column=columnNumber)
Button(controlWindow, text='all', background=offColour, command=lambda setAll('off')).grid(row=2, column=columnNumber)
controlWindow.mainloop() #show the window
