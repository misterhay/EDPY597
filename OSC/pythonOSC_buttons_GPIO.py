#!/usr/bin/python

####### Change settings in this section #######

# specify the output and input pins you will be using (in BCM style)
outputs = [2, 3, 4, 17, 27, 22, 10, 9, 14, 15, 18, 23, 24, 25, 8, 7]
inputs = [11]
# uncomment the following line if you are not using any outputs
#outputs = []
# uncomment the following line if you are not using any inputs
#inputs = []

# set to False if using LEDs or True if using a relay board (which activates on LOW)
relayBoard = True

# change this to the IP address and port that will receive our OSC messages, if applicable
remoteIP = '10.0.0.94'
remotePort = 9000

####### End of settings section #######

import time, threading
import OSC # requires pyOSC from https://trac.v2.nl/wiki/pyOSC or https://gitorious.org/pyosc
## remove the double-pound comments to turn on GPIO functions
##import RPi.GPIO as GPIO
##GPIO.setmode(GPIO.BCM)
sendAddress = (remoteIP, remotePort)
receiveAddress = ('0.0.0.0', 9000) # allow it to receive from any IP on port 9000
server = OSC.OSCServer(receiveAddress) # set up the OSC server
server.addDefaultHandlers() # not really necessary, but won't hurt

def outputHandler(address, typetag, value, source):
   # typetag should be i for integer (1 for output on, 0 for off)
   output = int(address.split('/')[2]) # get the output number from the OSC address
   pin = outputs[output-1] # translate the output number back to a pin number from the outputs list
   if relayBoard == True: # will invert the output if you set relayBoard to True
      if value == [0]:
         value = [1] # because for the relayBoard "HIGH" is "off"
      else:
         value = [0]
   if value == [0]:
      print 'turning off pin', output
##      GPIO.output(pin, GPIO.LOW) # turn off the pin
   if value == [1]:
      print 'turning on pin', output
##      GPIO.output(pin, GPIO.HIGH) # turn on the pin

if outputs: # if the outputs list is not empty
   outputNumber = 0 # this is the first output, we'll iterate from here
   
   # some things for the interface window
   from Tkinter import *
   controlWindow = Tk() #we're going to create a window full of buttons
   controlWindow.title('GPIO Output Buttons') #set the title of the window
   onColour = 'green' #the colour of the on buttons we'll use below
   offColour = 'red' #the colour of the off buttons
   columnNumber = 0 #initialize a variable for counting the columns

   for pin in outputs: # iterate through pins to set them up and make sure they are off
      outputNumber = outputNumber + 1 # iterate the counting variable
##      GPIO.setup(pin, GPIO.OUT)
      if relayBoard == True:
         print 'making sure the relay pin', pin, 'is off'
##      GPIO.output(pin, GPIO.HIGH)
      outputMessage = '/output/'+str(outputNumber)
      server.addMsgHandler(outputMessage, outputHandler)
      print 'To turn on pin', pin, 'send', outputMessage, '[1]'
      
      #make two buttons (on and off) for each pin in the array declared above
      Button(controlWindow, text=pin, background=onColour, command=lambda pin=pin: pinOut(pin, 'on')).grid(row=1, column=columnNumber)
      Button(controlWindow, text=pin, background=offColour, command=lambda pin=pin: pinOut(pin, 'off')).grid(row=2, column=columnNumber)
      columnNumber = columnNumber + 1 #increase this variable by one to prepare for the next iteration
   
   print 'we set up', outputNumber, 'pins as outputs'
   controlWindow.mainloop() #show the interface window

if inputs:
   client = OSC.OSCClient() # set up then connect to the OSC receiving server
   client.connect((sendAddress)) #not sure if we need both sets of parentheses
   inputNumber = 0
   for pin in inputs:
      inputNumber = inputNumber + 1
      print 'setting up pin', pin, 'as input number', inputNumber
##      GPIO.setup(pin, GPIO.IN)

threadingServer = threading.Thread(target = server.serve_forever)
threadingServer.start() # start the server thread we just defined
print 'OSC receiving server is running, press ctrl-c to quit'

try:
    while 1: # almost the same as while True:
       #time.sleep(5) # do nothing here, just wait for ctrl-c
       for pin in inputs:
          print 'checking pin', pin
##          if (GPIO.input(pin) == False): # because we're using a pull-up resistor
##             print 'pin', pin, 'is low, so you probably pushed a button'
##             message = OSC.OSCMessage('/input/'+str(pin))
##             message.append(1)
##             client.send(message)
          
except KeyboardInterrupt: # what to do if there's a ctrl-c
    print 'Stopping the OSC receiving server...'
    server.close()
    print 'Waiting...'
    threadingServer.join() # stop the thread
##    GPIO.cleanup # we can't forget to clean up the GPIO pins
    print 'Done'


