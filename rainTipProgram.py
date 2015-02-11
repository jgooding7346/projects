import RPi.GPIO as GPIO
import time

pin = 27
count = 0

def bucket_tipped_seconds(channel):
	global count
	count += 1

def bucket_tipped(channel):
	global count
	count += 1
	print(count * 0.2794)

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)
GPIO.add_event_detect(pin, GPIO.FALLING, callback=bucket_tipped_seconds, bouncetime=3000)

while True:
	print(count * 0.2794)
	time.sleep(1)

input("Press enter to exit...")

