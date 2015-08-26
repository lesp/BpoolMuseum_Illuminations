import RPi.GPIO as GPIO
import time
from energenie import switch_on, switch_off
import os

GPIO.setmode(GPIO.BCM)

GPIO.setup(26, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(21, GPIO.OUT)
switch_off()
#status = "off"
GPIO.output(21,True)
while True:
    GPIO.output(21,True)
    time.sleep(0.2)
    GPIO.output(21,False)
    time.sleep(0.2)
    GPIO.wait_for_edge(26, GPIO.FALLING)
    os.system("omxplayer -o local Journey.mp4 &")
    switch_on()
    time.sleep(2)
    switch_off()
