
import json
# from sklearn.metrics import (accuracy_score, f1_score, classification_report)




def my_classification_report(list_label_ohe, list_answer_ohe):
    """
    Calculate F1, Precision and Recall

    Args:
      list_label_ohe: list of one hot encodings of the labels
      list_answer_ohe: list of one hot encodings of the answers

    Returns:
      F1, Precision, Recall
    """  
    true_positive = 0
    false_positive = 0
    false_negative = 0

    for list_label, list_ohe in zip(list_label_ohe, list_answer_ohe):
      for label in list_label:
        if label in list_ohe:
          true_positive += 1
        else:
          false_negative += 1
      for answer in list_ohe:
        if answer not in list_label:
          false_positive += 1

    precision = true_positive/(true_positive+false_positive)
    recall = true_positive/(true_positive+false_negative)
    f1 = 2*((precision*recall)/(precision + recall))

    return f1, precision, recall


def trec_file_convert(trec_path, topk):
  trec_file = open(trec_path,'r')
  trec_dict = {}
  for line in trec_file:
    line = line.strip().split(' ')
    qid = int(line[0])
    pid = line[2]

    # if pid not in all_dict[str(qid)]:
    #   continue
    if int(pid) == int(qid):
      continue
    if qid not in trec_dict:
      trec_dict[qid] = []
    if len(trec_dict[qid]) < topk:
      trec_dict[qid].append(pid)
  
  # print(trec_dict)
  return trec_dict
    
def rel_file_convert(rel_path):


  valid_list = []
  valid_path = '/valid_qid.tsv'
  valid_file = open(valid_path,'r')
  for line in valid_file.readlines():
      line = line.strip().split(' ')
      qid = line[0]
      valid_list.append(int(qid))

  rel_file = open(rel_path,'r')
  label_dict = json.load(rel_file)
  rel_dcit = {}
  for qid in label_dict.keys():
    # print(qid)
    label_list = label_dict[qid]
    qid = int(qid.split('.')[0])
    if qid not in valid_list:
      continue
    if qid not in rel_dcit:
      rel_dcit[qid] = []
    label_list = list(set(label_list))
    for label in label_list:
      pid = label.split('.')[0]
      rel_dcit[qid].append(pid)

  return rel_dcit




def eval_F1(trec_path,topk):
  answer_dict = trec_file_convert(trec_path, topk)
  rel_path = 'task1_train_labels_2023.json'
  rel_dict = rel_file_convert(rel_path)
  list_answer_ohe = []
  list_label_ohe = []


  for key in rel_dict.keys():
    one_answer = answer_dict[key]
    one_rel = rel_dict[key]
    one_answer = [int(l) for l in one_answer]
    one_rel = [int(l) for l in one_rel]
    list_answer_ohe.append(one_answer)
    list_label_ohe.append(one_rel)


  f1, precision, recall = my_classification_report(list_label_ohe, list_answer_ohe)
  print('Precision',precision)
  print('Recall',recall)
  print('F1_Score',f1)



if __name__ == '__main__':
  trec_path = ' '
  answer_dict = trec_file_convert(trec_path, 5)
  rel_path = 'task1_train_labels_2023.json'
  rel_dict = rel_file_convert(rel_path)


  list_answer_ohe = []
  list_label_ohe = []


  for key in rel_dict.keys():
    one_answer = answer_dict[key]
    one_rel = rel_dict[key]
    one_answer = [int(l) for l in one_answer]
    one_rel = [int(l) for l in one_rel]
    list_answer_ohe.append(one_answer)
    list_label_ohe.append(one_rel)


  f1, precision, recall = my_classification_report(list_label_ohe, list_answer_ohe)
  print('Precision',precision)
  print('Recall',recall)
  print('F1_Score',f1)



