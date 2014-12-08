from easygui import *

name = enterbox(msg='Say your name: ')

msgbox('Welcome to Dave\'s nice calculator, ' + name + '.')
choice=''
while choice!='Exit':
	choice = buttonbox(msg='Please select an option.', choices=('Addition', 'Subtraction', 'Exit'))
	if choice == 'Addition':

		num1 = enterbox(msg='First number: ')

		num2 = enterbox('Second number: ')

		sum = num1+num2

		msgbox(sum)
		choice = 0
	if choice == 'Subtraction':
            sum = input('First number: ') - input('Second number: ')
            print(sum)
            choice = 0
	if choice == 'Exit':
            print("So long, and thanks for all the fish!")
	

	



	elif choice != 3:
		print('that is not a choice')
