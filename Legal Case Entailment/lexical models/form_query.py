import json
from tqdm import tqdm
import jieba

from tqdm import tqdm

import re
import os
import numpy as np
import json
from collections import defaultdict
# import utils

from tqdm import tqdm






import json
import os
import re
from tqdm import tqdm
raw_path = '/search/odin/TianGongQP/qian/COLIEE2023/coliee23/dataset/processed'
file_dir = os.listdir(raw_path)
outfile = open('/search/odin/TianGongQP/qian/COLIEE2023/lht_process/BM25/query_valid.tsv','w')


train_file = []
label_path = '/search/odin/TianGongQP/qian/COLIEE2023/coliee23/dataset/task1_raw_files/task1_train_labels_2023.json'
label_file = open(label_path,'r')
label_dict = json.load(label_file)
for key in label_dict.keys():
    pid = key.split('.')[0]
    train_file.append(pid)

valid_list = []
valid_path = '/search/odin/TianGongQP/qian/COLIEE2023/lht_process/datasets/valid_qid.tsv'
valid_file = open(valid_path,'r')
for line in valid_file.readlines():
    line = line.strip().split(' ')
    qid = line[0]
    valid_list.append(qid)

# print(train_file)
max_len =0
for a_file in file_dir:
    pid = a_file.split('.')[0]
    if pid not in valid_list:
        continue

    path = f'{raw_path}/{a_file}'
    text_ = ""
    
    with open(path, encoding='utf-8') as fin:
        lines = fin.readlines()
        for line in lines:
            line = line.replace("\n", " ").replace("\t"," ").strip()
            if len(line) != 0:
                text_ = text_ + line
            # break
  
    # print(text_)
    # break
    if len(text_)>max_len:
        max_len = len(text_)
        print(max_len)
    if len(text_) > 30000:
        text_ = text_[:10000]
    outfile.write(pid + '\t' + text_ + '\n')
        # qid_idx_writer.write(key + '\t' + body_str + '\n')
print(max_len)