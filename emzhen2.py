

def import_data(wd, file_name):
	"""
	Import the data from the Home folder and load it into the file
	"""

	file_path = os.path.join(wd,file_name)
	data = pd.read_csv(file_path)

	return data


def write_data(data, wd, file_name):

	file_path = os.path.join(wd, file_name)
	data.to_csv(file_path, index = False)


def calculate_expenses(data):
	data_exp = data[data.Type == 'Expense']
	total_expenses = data_exp['Cost'].sum()

	em_exp_paid_stg = data_exp[data_exp.Paid_by == 'Emily']
	em_exp_paid = em_exp_paid_stg['Cost'].sum()
	
	zhen_exp_paid_stg = data_exp[data_exp.Paid_by == 'Zhenya']
	zhen_exp_paid = zhen_exp_paid_stg['Cost'].sum()

	#em_owe = total_expenses - em_exp_paid
	#zhen_owe = total_expenses - zhen_exp_paid

	zhen_paid_even_stg = data[data.Type == 'To Emily']
	zhen_paid_even = zhen_paid_even_stg['Cost'].sum()

	em_paid_even_stg = data[data.Type == 'To Zhenya']
	em_paid_even = em_paid_even_stg['Cost'].sum()

	em_owe = total_expenses/2 - em_exp_paid - em_paid_even + zhen_paid_even
	zhen_owe = total_expenses/2 - zhen_exp_paid - zhen_paid_even + em_paid_even

	return em_owe, zhen_owe


def print_result(result):
	emily_owes = round(result[0],2)
	zhenya_owes = round(result[1],2)

	if emily_owes > 0:
		print "Emily owes Zhenya $%f" % emily_owes

	if zhenya_owes > 0:
		print "Zhenya owes Emily $%f" % zhenya_owes

	return


def main(argvs):
	wd = '/Users/emily.dahlberg/Documents/Home/'
	persistent_file = 'emzhen_pandas.csv'

	data = import_data(wd, persistent_file)

	balance = calculate_expenses(data)

	print_result(balance)

	write_data(data, wd, persistent_file)


if __name__ == "__main__":
	import sys
	import pandas as pd
	import numpy as np
	import datetime as dt
	import os

	main(sys.argv)