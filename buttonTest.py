import RPi.GPIO as GPIO
import time

pin = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)

while True:
	if GPIO.input(pin) == True:
		print("LOW")
	else:
		print("HIGH")
	time.sleep(0.5)
