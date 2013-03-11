from sys import argv
#from os.path import exists
import string

script, filename = argv

def count_characters(filename):
	in_file = open(filename).read() #open and reading
	low_letters = in_file.lower() #lowercasing

	alphabet = string.ascii_lowercase #creating alphabet string
	alphabet_list = list(alphabet) #making list out of alphabet string

	count = 0
	for character in low_letters:
		if i in range(ord('a'), ord('z') + 1):
			count = count + 1
			print count

count_characters(filename)

#want for loop to count each incidence of letter in low_letters and add toward corresponding index in alphabet_list