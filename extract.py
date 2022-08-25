import csv
import argparse
import sys
from tqdm import tqdm

def read_and_write(file_name):
    with open('salaries_cyber.csv', 'r') as file:
        reader = csv.reader(file)
            
        with open(file_name, 'w', newline= '') as inFile:
            writer = csv.writer(inFile, delimiter=',')
        
            for row in reader:
                writer.writerow(row)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', dest='file_name', type=str, required=True, default='new.csv')
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = main()
    read_and_write(args.file_name)
    