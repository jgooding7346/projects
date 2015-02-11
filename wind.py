import RPi.GPIO as GPIO
import time, math

pin = 17
count = 0
#speedKMpH = 0

def spin(channel):
	global count
	count += 1

def calcSpeed():
	speedCMpS = ((9 * math.pi) * count) / 5
	global speedKMpH
	speedKMpH = (speedCMpS / 100000) * 3600
	return speedKMpH

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)
GPIO.add_event_detect(pin, GPIO.FALLING, callback=spin, bouncetime=300)


while True:
	count = 0
	time.sleep(5)
	speedKMpH = calcSpeed()
	print(speedKMpH)
	print(count)


input("Press enter to exit...")

