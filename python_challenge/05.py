#!/usr/bin/python

'''
Only clues given from page source:

<!-- urllib may help. DON'T TRY ALL NOTHINGS, since it will never 
end. 400 times is more than enough. -->

<a href="linkedlist.php?nothing=12345"><img src="chainsaw.jpg" border="0"></a>
'''
import urllib2 as url
import re

def loop_for_numbers(url_base, starting_no, i, key_dict):
	"""
	Read the webpage for the number given and then redirect with the new number.
	If the message stops saying 'and the next nothing is nnnnn', then break out of
	the loop and return the current values.

	There is also a catch near the end where the message still includes 'and the next nothing is',
	but it's a trick and has two numbers in it. To work around this, the regex only looks for the
	number after those exact words.
	"""
	number = starting_no
	still_going = True

	while((i < 400) & (still_going)):
		response = url.urlopen(base_url + number)
		clue = response.read()
		key_dict[i] = number

		if 'and the next nothing is' not in clue:
			still_going = False
			break

		catch = re.search('the next nothing is [0-9]+', clue).group()
		number = catch[len('the next nothing is '):] #grab just the number that comes after the statement
		
		#Give some sort of progress indicator, but not for every i, because that's too many!
		if i % 10 == 0:
			print i
		i += 1

	return clue, number, i, key_dict

#Starting vars
base_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
starting_no = '12345'

#Build a dictionary with the 'nothings' for each iteration. Used to backtrack, but not necessary
# for final solution
complete_keys = {}

#Start going with the first given number!!
first_iteration = loop_for_numbers(base_url, starting_no, 0, complete_keys)

#Progress update
print "After %s iterations, you get a different message stating: %s \nContinuing on with this information..."\
	% (str(first_iteration[2]), first_iteration[0])

#Redefine vars for continuing after dividing.
first_to_second_no = str(int(first_iteration[1])/2)
first_to_second_i = int(first_iteration[2])
complete_keys = first_iteration[3]

#Keep going!
second_iteration = loop_for_numbers(base_url, first_to_second_no, first_to_second_i, complete_keys)

#Finally did it. Print out answer.
print "Phew! We did it! After a total of %s iterations, the final result is: %s" % \
		(str(second_iteration[2]), second_iteration[0])







