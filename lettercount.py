from sys import argv

script, filename = argv

def count_characters(filename):
	in_file = open(filename).read() 
	low_letters = in_file.lower() 

	counter = [0] * 26

	for characters in low_letters:
		int_value = ord(characters)

		if int_value >= 97 and int_value <= 122:
			index_num = int_value - 97 # this translates back the letter order starting from a= 0
			counter[index_num] += 1 # this increases the tally for the letter above in the list called, "counter"

	for i in counter:
		print i

count_characters(filename)