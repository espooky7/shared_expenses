#!/usr/bin/python

def read_jibberish(filename):
	"""
	Since the string is so huge, I saved it in another text file and read it in.
	Not sure if supposed to, but remove line breaks.
	"""
	text_file = open(filename,'r')
	text = text_file.read()
	text = text.replace('\n','')
	text_file.close()

	return text 


def find_counts(string):
	"""
	Define an array of the unique characters in the set.
	"""
	#set_chars = list(set(string)) # Not preserving order
	#char_count = dict.fromkeys(set_chars)

	set_chars = col.OrderedDict.fromkeys(string)

	for i in set_chars.iterkeys():
		set_chars[i] = string.count(i)

	return set_chars 


def find_rare_chars(dict_counts):
	rare_chars = []

	for i in dict_counts.iterkeys():
		if dict_counts[i] == 1:
			rare_chars.append(i)

	word = ''.join(rare_chars)
	return word


import collections as col 
jibberish = read_jibberish('03_jibberish.txt')
counts = find_counts(jibberish)
rare_characters = find_rare_chars(counts)

print rare_characters
