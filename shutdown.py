# !/bin/python

# Script that reboots the Raspberry Pi at the push of a button!

import RPi.GPIO as GPIO

import time

import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def Shutdown(channel):
	print ("Rebooting now..."); 
	time.sleep(1);
	os.system("sudo reboot") 

GPIO.add_event_detect(21, GPIO.FALLING, callback=Shutdown, bouncetime=2000)

while 1:
	time.sleep(1)
