# read csv file and save to json file with the following format:

# [
#     {
#         "original": "The quick brown fox jumps over the lazy dog",
#         "paraphrase": "The brown fox jumps over the lazy dog",
#         "is_paraphrase": false
#     },
#     {
#         "original": "The quick brown fox jumps over the lazy dog",
#         "paraphrase": "The quick brown fox jumps over the dog",
#         "is_paraphrase": false
#     },
#     {
#         "original": "Fuck You",
#         "paraphrase": "Fuck yeah",
#         "is_paraphrase": true
#     }
# ]

csv_path = "paradata/huggingface.csv"
json_path = "paradata/huggingface.json"

import csv
import json

with open(csv_path, "r") as f:
    reader = csv.reader(f)
    data = list(reader)

data = data[1:]

new_data = []
for d in data:
    new_data.append({"original": d[0], "paraphrase": d[1]})

with open(json_path, "w") as f:
    json.dump(new_data, f, indent=4)


