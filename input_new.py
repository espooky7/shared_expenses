
import sys
import pandas as pd 
from datetime import datetime as dt


def get_new_row():
	"""
	Ask user for new input
	"""
	new_row = {}
	n = dt.now()

	print "\nPlease enter the data for the new row below: \n"

	new_row['Date'] = n.strftime("%Y-%m-%d %H:%M:%S")
	paid = raw_input("Who paid? Emily [e] or Zhenya [z]?: ")

	if paid == 'E' or paid == 'e':
		new_row['Paid_by'] = 'Emily'
	elif paid == 'Z' or paid == 'z':
		new_row['Paid_by'] = 'Zhenya'
	else:
		print "Invalid input! Please restart."
		sys.exit(1)

	type_exp = raw_input("What type of payment is it? Expense [exp], Emily paying Zhenya [ez], or Zhenya paying Emily [ze]?: ")

	if type_exp == 'exp':
		new_row['Type'] = 'Expense'
	elif type_exp == 'ez':
		new_row['Type'] = 'To Zhenya'
	elif type_exp == 'ze':
		new_row['Type'] = 'To Emily'
	else:
		print "Invalid input! Please restart."
		sys.exit(1)

	new_row['Cost'] = float(raw_input("How much was paid?: "))
	new_row['Description'] = raw_input("Please briefly describe the expense: ")

	return new_row


def verify(new_row):
	print "Please verify the information is correct:\nDate: %s\nPaid by: %s\nType of payment: %s\nCost: %s \nDescription: %s\n" % (new_row['Date'], new_row['Paid_by'], new_row['Type'], new_row['Cost'], new_row['Description'])

	verify = raw_input("Is this correct? y/n: ")

	if verify == 'y':
		return 1
	elif verify == 'n':
		return 0
	else:
		print "Invalid input! Please restart."
		sys.exit(1)