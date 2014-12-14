#sos flasher by James Gooding
import RPi.GPIO as GPIO,time #Imports the time and RPI.GPIO module. Shortens RPI.GPIO to GPIO
def setup():
	GPIO.setmode(GPIO.BOARD) #Set the pin numbering system
	GPIO.setup(11,GPIO.OUT)

setup()

def wordEnd():
	GPIO.output(11,True)

def letterPause():
	GPIO.output(11,False)
	time.sleep(0.75)

def dot():
	GPIO.output(11,True)
	time.sleep(0.25)
	GPIO.output(11,False)
	time.sleep(0.25)

def dash():
	GPIO.output(11,True)
	time.sleep(0.75)
	GPIO.output(11,False)
	time.sleep(0.75)

def a():
	dot()
	dash()

def b():
	dash()
	dot()
	dot()
	dot()

def c():
	dash()
	dot()
	dash()
	dot()

def d():
	dash()
	dot()
	dot()

def e():
	dot()

def f():
	dot()
	dot()
	dash()
	dot()

def g():
	dash()
	dash()
	dot()

def h():
	dot()
	dot()
	dot()
	dot()

def i():
	dot()
	dot()

def j():
	dot()
	dash()
	dash()
	dash()

def k():
	dash()
	dot()
	dash()

def l():
	dot()
	dash()
	dot()
	dot()

def m():
	dash()
	dash()

def n():
	dash()
	dot()

def o():
	dash()
	dash()
	dash()

def p():
	dot()
	dash()
	dash()
	dash()

def q():
	dash()
	dash()
	dot()
	dash()

def r():
	dot()
	dash()
	dot()

def s():
	dot()
	dot()
	dot()

def t():
	dash()

def u():
	dot()
	dot()
	dash()

def v():
	dot()
	dot()
	dot()
	dash()

def w():
	dot()
	dash()
	dash()

def x():
	dash()
	dot()
	dot()
	dash()

def y():
	dash()
	dot()
	dash()
	dash()

def z():
	dash()
	dash()
	dot()
	dot()

def letterToMorse(y):
	if y == "a":
		a()
		letterPause()
	elif y == "b":
		b()
		letterPause()
	elif y == "c":
		c()
		letterPause()
	elif y == "d":
		d() 
		letterPause()
        elif y == "e":
		e()
		letterPause()
        elif y == "f":
		f()
		letterPause()
	elif y == "g":
		g()
		letterPause()
        elif y == "h":
		h()
		letterPause()
        elif y == "i":
		i()
		letterPause()
        elif y == "j":
		j()
		letterPause()
        elif y == "k":
		k()
		letterPause()
        elif y == "l":
		l()
		letterPause()
	elif y == "m":
		m()
		letterPause()
        elif y == "n":
                n()
		letterPause()
        elif y == "o":
                o()
		letterPause()
        elif y == "p":
                p()
		letterPause()
        elif y == "q":
                q()
		letterPause()
        elif y == "r":
                r()
		letterPause()
        elif y == "s":
                s()
		letterPause()
        elif y == "t":
                t()
		letterPause()
        elif y == "u":
                u()
		letterPause()
        elif y == "v":
                v()
		letterPause()
        elif y == "w":
                w()
		letterPause()
	elif y == "x":
		x()
		letterPause()
	elif y == "y":
		y()
		letterPause()
	elif y == "z":
		z()
		letterPause()
	else:
		wordEnd()

letter  = input("What word do you want to translate to morse?") #Asks the user for a word

for each in letter.lower():
	letterToMorse(each) #Outputs the variable letter in morse code