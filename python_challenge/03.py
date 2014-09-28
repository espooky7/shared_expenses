
def import_chunk(filename):
	"""
	Again, read in the block of text, saved in a separate txt file.
	Remove \n and \t before returning the string.
	"""
	file_obj = open(filename, 'r')
	text = file_obj.read()
	text = text.replace('\n', '')
	text = text.replace(' ','')
	file_obj.close()

	return text


def find_pattern(string, regex):
	"""
	The challenge states 'one small letter, surrounded by exactly three big bodyguards.
	Therefore the sequence should be oOOOoOOOo. Look for this pattern, and return the 
	middle value, which is the letter needed for the answer. Then join these letters together
	and return the final answer!
	"""
	found = regex.finditer(string)
	results = list()
	for match in found:
		chunk = match.group()
		letter = chunk[4]
		results.append(letter)
	
	answer = ''.join(results)					
	return answer


import re
# Define RegExp that looks for a lower case, followed by exactly 3 upper case, 1 lower case,
# three more Upper, and one more lower

text = import_chunk('04_jibberish.txt')
expression = re.compile(r'([a-z][A-Z]{3}){2}([a-z])')
answer = find_pattern(text, expression)

print answer