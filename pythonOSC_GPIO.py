#!/usr/bin/python
# some code/ideas borrowed from http://youtu.be/oaf_zQcrg7g

import time, threading
##import RPi.GPIO as GPIO
##GPIO.setmode(GPIO.BCM)
# the pins below will correspond to outlets 1 through n (where n is the number of pins used)
pins = [2, 3, 4, 17, 27, 22, 10, 9, 14, 15, 18, 23, 24, 25, 8, 7]

import OSC # requires pyOSC
receiveAddress = ('0.0.0.0', 9001) # allow it to receive from anyone on port 9000
server = OSC.OSCServer(receiveAddress) # set up the OSC server
server.addDefaultHandlers() # not really necessary, but good practice

def outletHandler(address, typetag, value, source):
   # typetag should be i for integer (1 for outlet on, 0 for off)
   # but remember that "on" is GPIO.LOW
   outlet = int(address.split('/')[2]) # get the outlet number from the OSC address
   pin = pins[outlet-1] # translate the outlet number back to a pin number
   print 'pin:', pin, ' outlet:', outlet, ' value:', value
   if value == [1]:
      print outlet, 'on'
##      GPIO.output(pin, GPIO.LOW) # turn on the outlet
   if value == [0]:
      print outlet, 'off'
##      GPIO.output(pin, GPIO.HIGH) # turn off the outlet
   else:
      print 'unknown command'

outlet = 1 # this is the first outlet, we'll iterate from here
for pin in pins: # iterate through pins to set them up and make sure they are off
##   GPIO.setup(pin, GPIO.OUT)
##   GPIO.output(pin, GPIO.HIGH)
   server.addMsgHandler('/outlet/'+str(outlet), outletHandler)
   print '/outlet/'+str(outlet)
   outlet = outlet + 1

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


