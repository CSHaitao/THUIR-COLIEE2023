'''
Author: lihaitao
Date: 2023-04-19 15:21:57
LastEditors: Do not edit
LastEditTime: 2023-04-19 15:21:58
FilePath: /Coliee2023/THUIR-COLIEE2023/Legal Case Retrieval/lightgbm/src/trees/convert_output_test.py
'''
import json



path = '/output.tsv'
file = open(path,'r')
qry_did_score = {}
output = open('output_order.tsv','w')
for line in file.readlines():
   
    line = line.strip()
    # print(line.split('\t'))
    qid, did, score = line.split('\t')
    score = float(score.strip(']').strip('['))
            
    if qid not in qry_did_score:
        qry_did_score[qid] = []
    qry_did_score[qid].append((did, score))

from operator import itemgetter, attrgetter
for qid in qry_did_score:
    qry_did_score[qid].sort(key=itemgetter(1), reverse=True)


for qid in qry_did_score:

    candidata = qry_did_score[qid]
  
    for i in range(0, len(candidata)):
        did = candidata[i][0]
        if qid != did:
            # already_qd.add((qid,did))
            score = candidata[i][1]
            output.write(f'{str(int(qid))} Q0 {did} {i + 1} {score} LHT\n')
output.close()