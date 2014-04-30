
def import_data(filename, wd):
	"""
	Import the data needed for analysis - just takes the file name and a directory
	"""
	file_path = os.path.join(wd, filename)
	data = pd.read_csv(file_path)

	return data


def random_samples(data, n_data, n_samples):
	"""
	This is the function that generates n samples of m size. It creates a dictionary of
	datasets with the random samples and returns the dictionary.
	"""
	data_dict = {}

	for i in range(1,n_samples+1):
		sample_index = rand.sample(data.index, n_data)
		sample_data = data.ix[sample_index]
		sample_data = sample_data.reset_index()
		del sample_data['index']
		data_dict[i] = sample_data

	return data_dict


def write_files(data_dict, n_samples, month, wd):
	"""
	Writes a .csv file for each of the random samples taken. 
	"""
	
	for i in range(1, n_samples+1):
		file_name = '2014-04-29_sample_' + month + '_%d' % i + '.csv'
		file_path = os.path.join(wd, file_name)
		data_dict[i].to_csv(file_path, index=False)

	return


def main():

	"""
	This is where you define your variables - the filepath for both the raw datasets and where
	the samples will be stored, the size of samples you want to generate, and the number of sample
	sets you want.

	For this particular file, the file names (both for raw sets and finalized), the names are hard-coded.

	File could be generalized with argvs set to find the raw data, and size of samples.
	"""

	wd = '/Users/emily.dahlberg/Documents/ad_hoc/CSVs/'
	n_data = 5000
	n_samples = 10

	january = import_data('2014-04-29_january_newuser.csv', wd)
	february = import_data('2014-04-29_february_newuser.csv', wd)
	march = import_data('2014-04-29_march_newuser.csv', wd)

	january_samples = random_samples(january, n_data, n_samples)
	february_samples = random_samples(february, n_data, n_samples)
	march_samples = random_samples(march, n_data, n_samples)

	write_files(january_samples, n_samples, 'january', wd)
	write_files(february_samples, n_samples, 'february', wd)
	write_files(march_samples, n_samples, 'march', wd)


if __name__ == '__main__':
	import sys
	import pandas as pd
	import random as rand
	import os

	main()