#!/usr/bin/python
# some code/ideas borrowed from http://youtu.be/oaf_zQcrg7g
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

pins = [2, 3, 4]

delayTime = 0.25

# iterate through pins to set them up
for i in pins: 
    GPIO.setup(i, GPIO.OUT) 
    GPIO.output(i, GPIO.HIGH)

def on(pin):
    GPIO.output(pin, GPIO.LOW)
    print pin, 'on'

def off(pin):
    GPIO.output(pin, GPIO.HIGH)
    print pin, 'off'

print 'testing outputs'
for i in pins:
    on(i)
    time.sleep(delayTime)
    off(i)
print 'done'
GPIO.cleanup()

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
