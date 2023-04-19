import re
import os
import json

pattern = r'\b(18\d{2}|19\d{2}|200\d|201\d|202[0-3])\b'
label_file_path = "./task1_test_no_labels_2023.json"
output_file_path = "./candidate_test.json"

with open(label_file_path) as f:
    a = json.load(f)

names = os.listdir("./task1_test_files_2023")
yd = {}
for q in names:
    with open(f"./task1_test_files_2023/{q}", "r", encoding="utf-8") as f:
        txt = f.read()
    years = re.findall(pattern, txt)
    years = [int(y) for y in years]
    yd[q] = max(years, default=0)

less = 0
more = 0

dedicate = {}

for q in a.keys():
    if yd[q] == 0:
        dedicate[q] = names
        continue
    dedicate[q] = []
    for doc in names:
        if yd[doc] <= yd[q]:
            dedicate[q].append(doc)

with open(output_file_path, "w+") as f:
    json.dump(dedicate, f)

print(len(dedicate))
print(sum(len(dedicate[q]) for q in dedicate) // len(dedicate))
print(len(names))