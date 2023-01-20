# script to Data standardization: 
# the script will take file formate as input and convert it to the desired format

import json
import os
import sys


def json_checker(formate_file, data_file):
    # check if the formate file is in json format
    if not os.path.isfile(formate_file):
        print("File does not exist")
        sys.exit(1)
    # check if the data file is in json format
    if not os.path.isfile(data_file):
        print("File does not exist")
        sys.exit(1)
    # open the formate file and read the formate
    with open(formate_file) as f:
        formate = json.load(f)
    # open the data file and read the data
    with open(data_file) as f:
        data = json.load(f)
    # check if the data is in the formate
    for i, d in enumerate(data):
        for key in d.keys():
            if key not in formate.keys():
                print("Data point: ", i)
                print("Invalid key: ", key)
                print("Valid keys: ", formate.keys())
                sys.exit(1)
            if type(d[key]) != formate[key]:
                print("Data point: ", i)
                print("Invalid value type: ", key)
                print("Valid type: ", formate[key])
                sys.exit(1)
    print("Data is in the correct format")

def csv_checker(formate_file, data_file):
    # check if the formate file is in csv format
    if not os.path.isfile(formate_file):
        print("File does not exist")
        sys.exit(1)
    # check if the data file is in csv format
    if not os.path.isfile(data_file):
        print("File does not exist")
        sys.exit(1)
    # open the formate file and read the formate
    with open(formate_file) as f:
        formate = f.readline().strip().split(",")
    # open the data file and read the data
    with open(data_file) as f:
        data = f.readlines()
    # check if the data is in the formate
    for i, d in enumerate(data):
        d = d.strip().split(",")
        if len(d) != len(formate):
            print("Data point: ", i)
            print("Invalid number of values")
            print("Valid number of values: ", len(formate))
            sys.exit(1)
        for j, key in enumerate(d):
            if key not in formate[j]:
                print("Data point: ", i)
                print("Invalid value: ", key)
                print("Valid values: ", formate[j])
                sys.exit(1)
    print("Data is in the correct format")

def xml_checker(formate_file, data_file):
    # check if the formate file is in xml format
    if not os.path.isfile(formate_file):
        print("File does not exist")
        sys.exit(1)
    # check if the data file is in xml format
    if not os.path.isfile(data_file):
        print("File does not exist")
        sys.exit(1)
    # open the formate file and read the formate
    with open(formate_file) as f:
        formate = f.readlines()
    # open the data file and read the data
    with open(data_file) as f:
        data = f.readlines()
    # check if the data is in the formate
    for i, d in enumerate(data):
        d = d.strip().split(",")
        if len(d) != len(formate):
            print("Data point: ", i)
            print("Invalid number of values")
            print("Valid number of values: ", len(formate))
            sys.exit(1)
        for j, key in enumerate(d):
            if key not in formate[j]:
                print("Data point: ", i)
                print("Invalid value: ", key)
                print("Valid values: ", formate[j])
                sys.exit(1)
    print("Data is in the correct format")
def txt_checker(formate_file, data_file):
    # check if the formate file is in txt format
    if not os.path.isfile(formate_file):
        print("File does not exist")
        sys.exit(1)
    # check if the data file is in txt format
    if not os.path.isfile(data_file):
        print("File does not exist")
        sys.exit(1)
    # open the formate file and read the formate
    with open(formate_file) as f:
        formate = f.readlines()
    # open the data file and read the data
    with open(data_file) as f:
        data = f.readlines()
    # check if the data is in the formate
    for i, d in enumerate(data):
        d = d.strip().split(",")
        if len(d) != len(formate):
            print("Data point: ", i)
            print("Invalid number of values")
            print("Valid number of values: ", len(formate))
            sys.exit(1)
        for j, key in enumerate(d):
            if key not in formate[j]:
                print("Data point: ", i)
                print("Invalid value: ", key)
                print("Valid values: ", formate[j])
                sys.exit(1)
    print("Data is in the correct format")
# what are different type of data format 
# for example json, csv, xml, txt, etc
if __name__ == "__main__":

    if sys.argv[1] == "json":
        json_checker(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == "csv":
        csv_checker(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == "xml":
        xml_checker(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == "txt":
        txt_checker(sys.argv[2], sys.argv[3])
    else:
        print("Invalid data format")
        sys.exit(1)