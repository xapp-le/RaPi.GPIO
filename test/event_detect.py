#!/usr/bin/env python
import RaPi.GPIO as GPIO
import time
from threading import Timer

SWITCH_PIN = 18
GPIO.setmode(GPIO.BOARD)
GPIO.setup(SWITCH_PIN,GPIO.IN,GPIO.PUD_UP)
print "\n value_%d = %d\n" %(SWITCH_PIN,GPIO.input(SWITCH_PIN))

GPIO.add_event_detect(SWITCH_PIN, GPIO.RISING,bouncetime=200)  # add rising edge detection on a channel

switchcount = 0
while switchcount < 2:   
	if GPIO.event_detected(SWITCH_PIN):
		switchcount += 1
		print 'Button pressed',switchcount
		print "\n value_%d = %d\n" %(SWITCH_PIN,GPIO.input(SWITCH_PIN))
		

GPIO.remove_event_detect(SWITCH_PIN)
