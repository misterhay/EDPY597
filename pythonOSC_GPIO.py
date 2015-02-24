#!/usr/bin/python
# some code/ideas borrowed from http://youtu.be/oaf_zQcrg7g

relayBoard = True #set to False if using LEDs or True if using a relay board (inverts outputs)

# the pins below will correspond to inputs and outputs
outputs = [2, 3, 4, 17, 27, 22, 10, 9, 14, 15, 18, 23, 24, 25, 8, 7]
inputs = []

import time, threading
import OSC # requires pyOSC
##import RPi.GPIO as GPIO
##GPIO.setmode(GPIO.BCM)
receiveAddress = ('0.0.0.0', 9000) # allow it to receive from anyone on port 9000
server = OSC.OSCServer(receiveAddress) # set up the OSC server
server.addDefaultHandlers() # not really necessary, but a good idea

def outputHandler(address, typetag, value, source):
   # typetag should be i for integer (1 for output on, 0 for off)
   output = int(address.split('/')[2]) # get the output number from the OSC address
   pin = outputs[output-1] # translate the output number back to a pin number from the outputs array
   #print 'pin:', pin, ' output:', output, ' value:', value #print what we've learned
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
   '''
   else:
      print 'unknown command'
   '''

output = 1 # this is the first output, we'll iterate from here
for pin in outputs: # iterate through pins to set them up and make sure they are off
##   GPIO.setup(pin, GPIO.OUT)
   if relayBoard == True:
      print 'making sure the relay pin', pin, 'is off'
##   GPIO.output(pin, GPIO.HIGH)
   outputMessage = '/output/'+str(output)
   server.addMsgHandler(outputMessage, outputHandler)
   print 'To turn on pin', pin, 'send', outputMessage, '[1]'
   output = output + 1 # iterate the counting variable
print 'we set up', output-1, 'pins as outputs'

threadingServer = threading.Thread(target = server.serve_forever)
threadingServer.start() # start the server thread we just defined
print 'OSC receiving server is running, press ctrl-c to quit'

try:
    while 1: # almost the same as while True:
        time.sleep(5) # do nothing here, just wait for ctrl-c
except KeyboardInterrupt: # what to do if there's a ctrl-c
    print 'Stopping the OSC receiving server...'
    server.close()
    print 'Waiting...'
    threadingServer.join() # stop the thread
##    GPIO.cleanup # we can't forget to clean up the GPIO pins
    print 'Done'


