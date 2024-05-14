import pandas as pd
import argparse
import os

# Define command line arguments for input and output files
parser = argparse.ArgumentParser(description='Transform Global Biodiversity Information Facility data')
parser.add_argument('infile', type=str, help='The input file to transform')
parser.add_argument('outfile', type=str, help='The output file to write the transformed data to')
args = parser.parse_args()

# Read the input CSV file, specifying the separator, header row, decimal, and parsing dates
data = pd.read_csv(args.infile, sep=',', header=0, decimal='.', parse_dates=['eventDate'], encoding='utf-8').sort_values(['eventDate'])

# Write the data to the output Parquet file
data.to_parquet(args.outfile, index=False)
