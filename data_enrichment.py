# CLI interface to manually add datapoint to new file
# data enrichment is the process of adding more data to the dataset
# This script will add more data to the dataset and more information to the dataset

import json
import os
import sys

# read the data from the file
# show the data to the users and ask them to add more information to each data point
# take json file as input and add more information to the dataset
# save the new data to a new file

def data_enrichment(file_name):
    file_name = file_name.split(".")[0] + "_cleaned.json"
    if not os.path.isfile(file_name):
        print("File does not exist")
        sys.exit(1)
    with open(file_name) as f:
        data = json.load(f)
    for i, d in enumerate(data):
        print("Data point: ", i)
        print(d)
        print("Enter the new value or press enter to skip")
        for key in d.keys():
            new_value = input(key + ": ")
            if new_value != "":
                d[key] = new_value
    # save the new data to a new file
    file_name = file_name.split(".")[0] + "_enriched.json"
    with open(file_name, "w") as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    file_name = sys.argv[1]
    data_enrichment(file_name)

