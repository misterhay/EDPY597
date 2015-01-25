#!/usr/bin/python
# some code/ideas borrowed from http://youtu.be/oaf_zQcrg7g
import time
delayTime = 0.25
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
pins = [2, 3, 4, 17, 27, 22, 10, 9, 14, 15, 18, 23, 24, 25, 8, 7]
#pins = [2, 3, 4, 17, 27, 22, 10, 9, 11]
#pins = [14, 15, 18, 23, 24, 25]

# iterate through pins to set them up and flash them
for pin in pins:
   GPIO.setup(pin, GPIO.OUT) 
   GPIO.output(pin, GPIO.LOW)
   time.sleep(0.001)
   GPIO.output(pin, GPIO.HIGH)
   time.sleep(0.001)
GPIO.cleanup

'''
try:
   while True:
      for i in pins:
         GPIO.output(i, GPIO.LOW)
         time.sleep(delayTime)
         GPIO.output(i, GPIO.HIGH)

except KeyboardInterrupt:
  print 'cleaning up'
  GPIO.cleanup()
  print 'done'
'''
