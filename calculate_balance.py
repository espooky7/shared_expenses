def import_data(wd, file_name):
	"""
	Import the data from the Home folder and load it into the file
	"""

	file_path = os.path.join(wd,file_name)
	data = pd.read_csv(file_path)

	return data


def write_data(data, wd, file_name):
	'''
	Simple function to write a dataframe to a csv (given the file name) once it has been calculated.
	'''

	file_path = os.path.join(wd, file_name)
	data.to_csv(file_path, index = False)


def calculate_expenses(data):
	'''
	This one is a bit hairy, but it takes the new cost line and calculates the balances owed.
	It returns two variables: the fina calculation of what Em and Zhen each owe.
	'''
	#First add up all the expenses
	data_exp = data[data.Type == 'Expense']
	total_expenses = data_exp['Cost'].sum()

	#Calculate how much each person has paid toward expenses
	em_exp_paid_stg = data_exp[data_exp.Paid_by == 'Emily']
	em_exp_paid = em_exp_paid_stg['Cost'].sum()
	
	zhen_exp_paid_stg = data_exp[data_exp.Paid_by == 'Zhenya']
	zhen_exp_paid = zhen_exp_paid_stg['Cost'].sum()

	#Calculate how much each has paid to the other to even out costs
	zhen_paid_even_stg = data[data.Type == 'To Emily']
	zhen_paid_even = zhen_paid_even_stg['Cost'].sum()

	em_paid_even_stg = data[data.Type == 'To Zhenya']
	em_paid_even = em_paid_even_stg['Cost'].sum()

	#Finally calculate how much each owes the other. 
	em_owe = total_expenses/2 - em_exp_paid - em_paid_even + zhen_paid_even
	zhen_owe = total_expenses/2 - zhen_exp_paid - zhen_paid_even + em_paid_even

	em_owe = round(em_owe,2)
	zhen_owe = round(zhen_owe,2)

	return em_owe, zhen_owe


def add_new_row(data, new_row):
	'''
	Give the function the existing dataset and the new row, and it will append.
	'''
	data = data.append(new_row, ignore_index = True)
	return data


def update_file(data, result):
	'''
	Once the new balance has been calculated, enter it into the last two columns
	'''

	i = len(data) - 1

	if math.isnan(data.Em_owes[i]):
		data['Em_owes'].loc[i] = result[0]
		data['Zhen_owes'].loc[i] = result[1]

	return data


def print_result(result):
	'''
	When running the script, we want to know what the current balance is, this prints it out.
	'''
	emily_owes = round(result[0],2)
	zhenya_owes = round(result[1],2)

	if emily_owes > 0:
		print "Emily owes Zhenya $%s" % repr(emily_owes)

	if zhenya_owes > 0:
		print "Zhenya owes Emily $%s" % repr(zhenya_owes)

	return


def main(argvs):
	wd = '/Users/emily.dahlberg/Documents/Home/'
	persistent_file = 'emzhen_pandas.csv'

	data = import_data(wd, persistent_file)

	#Ask if you want to enter a new cost, or just check the balance.
	add_new = raw_input("Would you like to add a new entry? y/n: ")
	
	#If you do want to add a new cost, run through the necessary functions
	if add_new == "y":
		new_row = new.get_new_row()
		check = new.verify(new_row)
		if check == 0:
			main(sys.argv)
		data = add_new_row(data, new_row)

	#Calculate the balance of the dataset
	balance = calculate_expenses(data)

	#Print the new balance to the command line
	print_result(balance)

	#Append the new line to the file and save it to the csv.
	data = update_file(data, balance)
	write_data(data, wd, persistent_file)


if __name__ == "__main__":
	import sys
	import pandas as pd
	import datetime as dt
	import os
	import math
	import input_new as new

	main(sys.argv)