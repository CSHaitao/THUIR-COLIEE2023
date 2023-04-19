'''
Author: lihaitao
Date: 2023-03-22 16:24:31
LastEditors: Do not edit
LastEditTime: 2023-04-19 15:54:53
FilePath: /Coliee2023/THUIR-COLIEE2023/Legal Case Entailment/inference.py
'''

import os
os.environ["CUDA_VISIBLE_DEVICES"] = '1'
from pygaggle.rerank.base import Query, Text
from pygaggle.rerank.transformer import MonoT5,MonoBERT,DuoT5
from transformers import T5ForConditionalGeneration,DebertaModel,DebertaV2Model,DebertaV2ForSequenceClassification,AutoModelForSequenceClassification,AutoTokenizer,AutoModel
from pyserini.search import SimpleSearcher
import torch

from tqdm import tqdm
import jsonlines

from pygaggle.rerank.base import Reranker
from sentence_transformers import CrossEncoder
from typing import List
from copy import deepcopy

        
if torch.cuda.is_available(): 
    dev = "cuda"
    print(dev, torch.cuda.get_device_name(0))
    device = torch.device(dev)
else: 
    dev = "cpu"
    print(dev) 

# model = T5ForConditionalGeneration.from_pretrained('/home/lht/Coliee2023/Task2/train_t5/sft/monot5-base-marco/checkpoint-10000').to(device).eval()
# reranker = MonoT5(model=model)
# model = DebertaV2ForSequenceClassification.from_pretrained('/home/lht/Coliee2023/Task2/models/deberta-v3-base').to(device).eval()
# reranker = MonoT5(model=model)


model = AutoModelForSequenceClassification.from_pretrained('').to(device).eval()
tokenizer = AutoTokenizer.from_pretrained('', use_fast=False)
reranker = MonoBERT(model,tokenizer)
# reranker = MonoBERT(model,tokenizer)

outfile = open('','w')


def int2str(i):
    """
    Fix numbers using three digits according to database. Used to read data.

    Args:
      i: An integer number between 1 and 650

    Returns:
      An integer with 3 digits between 1 and 650.
    """
    if i < 10:
        j = '00' + str(i)
    elif i >= 10 and i < 100:
        j = '0' + str(i)
    else:
        j = str(i)

    return j


def get_base_case (path_to_file):
    """
    Read one base case and segment it

    Args:
      path_to_file: Path to file

    Returns:
      One segmented base case.
    """
    
    with open(path_to_file) as f:
        contents = f.read()
        f.close()

    contents = contents.replace('\n',' ').replace('FRAGMENT_SUPPRESSED','')
    base_case = ' '.join(contents.split())
    
    return base_case


def get_candidate(path_to_file, i, base_case_number, save): 
    """
    Read one candidate case and segment it. It also saves the candidate case as json to use in Pyserini.

    Args:
      path_to_file: Path to candidate file (string)
      i: Candidate case number (int)
      base_case_number: Base case number (int)
      save: Save as json (bool)
     
    Returns:
      One segmented candidate case.
    """
    with open(path_to_file) as f:
        contents = f.read()
        f.close()

    contents = contents.replace('\n','').replace('FRAGMENT_SUPPRESSED','')
    if len(contents.split()) <= 10:
        contents = contents.replace('<p style=','This is a wrong document. It should have only one segment. Thats it.').replace('FRAGMENT_SUPPRESSED','')
        contents = 'This is a wrong document. It should have only one segment. Thats it.'
  
    candidate_case = ' '.join(contents.split()) 
    dict_ = { "id": "{}_candidate{}.txt_task2".format(str(base_case_number),str(i)), "contents": candidate_case}
        
    if save == True:
        with jsonlines.open('/candidate.jsonl', mode='a') as writer:
            writer.write(dict_)
 
    return candidate_case

def get_one_candidate(base_case_number, k, save):  # get candidates
    """
    Read a candidate case to prepare preprocessing

    Args:
      base_case_number: Base case number
      k: Candidate case number
      save: Save candidate case as json
    Returns:
      One segmented base case.
    """
    n = k
    if int(base_case_number) <= 726:
        candidate_path = '/{}/paragraphs/{}.txt'.format(base_case_number, n)
    else:
        candidate_path = '/{}/paragraphs/{}.txt'.format(base_case_number, n)
       
    list_segments_candidate = get_candidate(candidate_path, n, base_case_number, save)
    list_passage = [str(n),list_segments_candidate]
       
    return list_passage

def main(n_case, n_candidate, save = False):
    """
    Read a base case and segment it

    Args:
      n_case: Base case number
      n_candidate: Candidate case number
      save: Save candidate case as json
    Returns:
      One segmented base case and one segmented candidate case.
    """
    
    base_case_number = int2str(n_case)
    candidate_number = int2str(n_candidate)

    list_candidates = get_one_candidate(base_case_number, candidate_number, save)

    return list_candidates


for casos in tqdm(range(1,626)): 
    base_case_number = int2str(casos)
    query_path = '/{}/entailed_fragment.txt'.format(base_case_number)
    query_case = get_base_case(query_path) 
    query_case = Query(query_case)
    passage = []
    paragraphs = os.listdir('/{}/paragraphs'.format(int2str(casos)))
    for candidatos in range(1, len(paragraphs)+1): 
        list_candidates = main(casos, candidatos, save=False)
        passage.append(list_candidates)
   
    texts = [Text(p[1], {'docid': p[0]}, 0) for p in passage] 
    reranked = reranker.rerank(query_case, texts)
    score = []
    pid = []
    for i in range(len(reranked)):
        score.append(reranked[i].score)
        pid.append(reranked[i].metadata['docid'])
       
    prob_list = list(zip(pid, score))
    prob_list = sorted(prob_list, key=lambda x: x[1], reverse=True)
   
    for i in range(len(prob_list)):
        outfile.write(f"{base_case_number} {prob_list[i][0]} {prob_list[i][1]} {i+1}\n")
      




