from sys import argv
#from os.path import exists
import string

script, filename = argv

def count_characters(filename):
	in_file = open(filename).read()
	low_letters = in_file.lower() 
	# letter_count = len(low_letters)

	i = 0
	for i in range(97, 123): # Count through A-Z the alphabet starting at ASCII 97 == "a"
		#i = 0
		AZcount = 97
		for num_char in letter_count: # for each letter in the object of all lower-case letters	
			#print "low_letters(i) = %d" % low_letters[i]
			num_char = 0		
			if ord('x') == AZcount:   # or is it just ord(i)? OR low_letters(i).ord
				num_char += 1
				x += 1
				print num_char
			AZcount += 1

count_characters(filename)

