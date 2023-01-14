# CLI tool to maunlly add datapoint to new file

import json
import os
import sys

def main(file_name):
    if len(sys.argv) != 2:
        print("Usage: python data_cleaning.py <file_name>")
        sys.exit(1)
    if not os.path.isfile(file_name):
        print("File does not exist")
        sys.exit(1)
    existing_file_name = file_name.split(".")[0] + "_cleaned.json"

    if os.path.isfile(existing_file_name):
        file_name = existing_file_name
        print("Some of the data has already been checked") 
    
    with open(file_name) as f:
        data = json.load(f)
    # open data_clenaned.json and check if it exists

    for i, d in enumerate(data):
        if "is_paraphrase" in d.keys():
            continue
        
        # color code the Original and Paraphrase in the terminal
        print("Data point: ", i)

        print("\033[1;31;40m Original: \033[0m", d["original"])
        print("\033[1;32;40m Paraphrase: \033[0m", d["paraphrase"])
        # color code the Is paraphrase? in the terminal
        print("\033[1;33;40m Is paraphrase? (y/n): \033[0m", end="")
        ans = input()
        
        if ans == "y":
            d["is_paraphrase"] = True
        elif ans == "n":
            d["is_paraphrase"] = False
        elif ans == "q":
            break
        else:
            print("Invalid input. Skipping")
            continue
    # save to new file
    print("scan all the files, Saving to file")
    saved_file_name = file_name.split(".")[0] + "_cleaned.json"

    with open(saved_file_name, "w") as f:
    # save only the data points that have been checked
        json.dump(data, f, indent=4)
if __name__ == "__main__":
    main(sys.argv[1])
