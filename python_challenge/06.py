"""
Downloaded a zip file with a ton of txt files with the same 'Next nothing is...' format. 
Here we go again...?

Found hint in readme: 

welcome to my zipped list.

hint1: start from 90052
hint2: answer is inside the zip

There are 911 files in the folder, hence the while limit

"""

import re, zipfile

starting_no = '90052'
filename = 'channel.zip'
file_ext = '.txt'

challengezip = zipfile.ZipFile(filename)

i = 0
still_going = True
number = starting_no

collect_comments = list()

while ((i < 950) & still_going):
	comment = challengezip.getinfo(number + file_ext).comment
	collect_comments.append(comment)

	textfile = challengezip.open(number + file_ext)
	clue = textfile.read()

	if 'Next nothing is' not in clue:
		print clue, number, i
		still_going = False
		break

	number = re.search('[0-9]+', clue).group()
	comment = clue.replace('Next nothing is %s' % (number), '')
	if comment != '':
		collect_comments[i] = comment

	i += 1

print ''.join(collect_comments)