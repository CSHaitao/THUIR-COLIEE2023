import json
import os
import re
from tqdm import tqdm
raw_path = '/search/odin/TianGongQP/qian/COLIEE2023/coliee23/dataset/processed'

file_dir = os.listdir(raw_path)
outfile = open('/search/odin/TianGongQP/qian/COLIEE2023/lht_process/BM25/corpus/corpus.json','w')  

# for a_file in file_dir:
#     pid = a_file.split('.')[0]
#     path = f'{raw_path}/{a_file}'
#     text_ = ''
    
#     with open(path, encoding='utf-8') as fin:
#         lines = fin.readlines()
#         for line in lines:
#             line = line.replace("\n", "")
#             text_ = text_ + line
  
#     save_dict = {}
#     save_dict['id'] = pid
#     save_dict['contents'] = text_
#     # print(save_dict)
#     outline = json.dumps(save_dict,ensure_ascii=False)+'\n'
#     outfile.write(outline)
#     # break
save_dict = {}
for a_file in tqdm(file_dir):
    pid = a_file.split('.')[0]
    path = f'{raw_path}/{a_file}'
    text_ = ''
    
    with open(path, encoding='utf-8') as fin:
        lines = fin.readlines()
        for line in lines:
            line = line.replace("\n", "")
            text_ = text_ + line

    save_dict = {}
    save_dict['id'] = pid
    save_dict['contents'] = text_
    # print(save_dict)
    outline = json.dumps(save_dict,ensure_ascii=False)+'\n'
    outfile.write(outline)

    # save_dict[str(pid)] = text_
    # save_dict['contents'] = text_
    # print(save_dict)
    # outline = json.dumps(save_dict,ensure_ascii=False)+'\n'
    # outfile.write(outline)
    # # break
# with open('/search/odin/TianGongQP/qian/COLIEE2023/coliee23/dataset/corpus_all.json','w',encoding='utf-8') as fp:
#     json.dump(save_dict,fp,ensure_ascii=False)