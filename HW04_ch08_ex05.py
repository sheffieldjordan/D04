# Structure this script entirely on your own.
# See Chapter 8: Strings Exercise 5 for the task.
# Please do provide function calls that test/demonstrate your
# function.
def rotate_word(word, integer):
	word = word.lower()
	rotated_value = int(integer)
	rotated_letter = ''
	rotated_word = ''
	
	for letter in word:
		x = (ord(letter)) + rotated_value
		if x < ord('a'):
			x = x + 26
		elif x > ord('z'):
			x = x - 26
		rotated_word += (chr(x))
	
	return rotated_word

def main():
	print(rotate_word("Alameda", 13))
	print(rotate_word("Whitney", 1))
	print(rotate_word("Zebra", 1))
	print(rotate_word("Xanadu", 2))
	print(rotate_word("IBM", -1))
if __name__ == '__main__':
    main()