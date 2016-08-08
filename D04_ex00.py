#!/usr/bin/env python
# D04_ex00

# Create a program that does the following:
#     - creates a random integer from 1 - 25
#     - asks the user to guess what the number is
#     - validates input is a number
#     - tells the user if they guess correctly
#         - if not: tells them too high/low
#     - only lets the user guess five times
#         - then ends the program
################################################################################
# Imports
import random

# Body
number = random.randrange(1,25)
guess = ''
x = 1
while True:
	try:
		while x <= 5:
			guess = int(input('Enter a guess from 1 to 25! '))
			if guess == number:
				print('You guessed correctly! The number was',number)
				break
			if guess < number:
				print('Try higher!')
			if guess > number:
				print('Try lower!')
			x += 1
		print('THE NUMBER WAS',number)
		break
	except:
		print('Nice try, enter an integer')



################################################################################
def main():

	print
    
    

if __name__ == '__main__':
    main()