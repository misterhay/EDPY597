#!/usr/bin/python
# some code borrowed from http://youtu.be/oaf_zQcrg7g

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

pins = [2, 3, 4, 17, 27, 22, 10, 9]

# iterate through pins to set them up
for i in pins: 
    GPIO.setup(i, GPIO.OUT) 
    GPIO.output(i, GPIO.HIGH)

try:
   while True:
      for i in pins:
         GPIO.output(i, GPIO.LOW)
         GPIO.output(i, GPIO.HIGH)

except KeyboardInterrupt:
  print 'cleaning up'
  GPIO.cleanup()
  print 'done'
