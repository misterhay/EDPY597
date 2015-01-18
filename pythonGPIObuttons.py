#!/usr/bin/python
#this depends on RPi.GPIO https://pypi.python.org/packages/source/R/RPi.GPIO/

#import RPi.GPIO as GPIO
#GPIO.setmode(GPIO.BCM)
pins = [2, 3, 4, 17, 27, 22, 10, 9, 11, 14, 15, 18, 23, 24, 25, 8, 7]
#for i in pins: #set up the pins as outputs
#    GPIO.setup(i, GPIO.OUT) 
#    GPIO.output(i, GPIO.1)

from Tkinter import * #for the GUI
#import tkMessageBox #for the GUI

#define a function for setting the pin states, so that we can call it later
def pinOut(pin, state):
    print pin
    print state #remember that for the pin state 1 means off and 0 means on
    if state == 'on':
        stateNumber = 0
    if state == 'off':
        stateNumber = 1
    #GPIO.output(i, stateNumber) #

window = Tk() #we're going to create a window full of buttons
window.title('GPIO Output Buttons') #set the title of the window
onColour = 'green' #the colour of the on buttons we'll use below
offColour = 'red' #the colour of the off buttons
columnNumber = 0 #initialize a variable for counting the columns

'''
for pin in pins: #we'll make an on button and an off button for each pin in the array declared above
    print pins[columnNumber]
    Button(window, text=pin, background=onColour, command=lambda: pinOut(pins[columnNumber], 'on')).grid(row=1, column=columnNumber)
    Button(window, text=pin, background=offColour, command=lambda: pinOut(pins[columnNumber], 'off')).grid(row=2, column=columnNumber)
    columnNumber = columnNumber + 1 #increase this variable by one to prepare for the next run through
'''

'''
Button(window, text='1 on', background=onColour, command=lambda: pinOut(1, 'on')).grid(row=1, column=1)
Button(window, text='1 off', background=offColour, command=lambda: pinOut(1, 'off')).grid(row=2, column=1)
Button(window, text='2 on', background=onColour, command=lambda: pinOut(2, 0)).grid(row=1, column=2)
Button(window, text='2 off', background=offColour, command=lambda: pinOut(2, 1)).grid(row=2, column=2)
#etc...
'''
Button(window, text=4, command=lambda: pinOut(Button.config('text'), 0)).grid(row=1, column=1) #this doesn't work
window.mainloop() #show the window
