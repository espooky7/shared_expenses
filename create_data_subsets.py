#!/usr/bin/python

def parse_args(argv):
	arg_parser = argparse.ArgumentParser(
		description = '''
		Generate subsets of data for training and testing models.
        '''
    )
	arg_parser.add_argument(
		'-s', '--size',
		default = 5000,
		help = 'How many rows do you want in your subsets? (default = 5,000)'
	)
	arg_parser.add_argument(
		'-n', '--number_sets',
		default = 10,
		help = 'How many separate subsets do you want to generate? These will \
		each go in a separate csv. (default = 10)'
	)
	arg_parser.add_argument(
		'-f', '--filename',
		help = 'Name of the file that contains the full data set.'
	)
	args = arg_parser.parse_args()

	return args


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


def write_files(data_dict, n_samples, wd):
	"""
	Writes a .csv file for each of the random samples taken. 
	"""
	
	for i in range(1, n_samples+1):
		file_name = str(d.today()) + '_%d' % i + '.csv'
		file_path = os.path.join(wd, file_name)
		data_dict[i].to_csv(file_path, index=False)

	return


def main(argv):

	"""
	This is where you define your variables - the filepath for both the raw datasets and where
	the samples will be stored, the size of samples you want to generate, and the number of sample
	sets you want.

	For this particular file, the file names (both for raw sets and finalized), the names are hard-coded.

	File could be generalized with argvs set to find the raw data, and size of samples.
	"""

	args = parse_args(argv)

	file_name = str(args.filename)
	sample_size = int(args.size)
	num_samples = int(args.number_sets)

	print "Subsetting your file %s into %d samples of %d rows..." % (file_name\
		, num_samples, sample_size)

	wd = '/Users/emily.dahlberg/Documents/ad_hoc/CSVs/'

	full_data = import_data(file_name, wd)

	samples = random_samples(full_data, sample_size, num_samples)

	print "Saving new subsets as csv files in %s" % wd
	write_files(samples, num_samples, wd)

	print "Complete!"


if __name__ == '__main__':
	import sys
	import pandas as pd
	import random as rand
	import os
	from datetime import date as d
	import argparse

	main(sys.argv)