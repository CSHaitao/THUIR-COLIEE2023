import json

#EVAL_IN_VALID is true only when you want to eval the validation set.
EVAL_IN_VALID = False

#You can use your own validation set.
label_file_path = "./valid_labels.json"

candidate_file_path = "./candidate_train.json"
score_file_path = "./score_valid_output_order.json"
delete_query = True

def my_classification_report(list_label_ohe, list_answer_ohe):
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
    if precision == 0 or recall == 0:
        return 0, precision, recall
    f1 = 2*((precision*recall)/(precision + recall))
    return f1, precision, recall


with open(score_file_path) as f:
    score = json.load(f)

with open(label_file_path) as f:
    valid = json.load(f)
    
with open("./task1_train_labels_2023.json") as f:
    all_ = json.load(f)

with open(candidate_file_path) as f:
    candidate = json.load(f)

if EVAL_IN_VALID:
    plist = [s for s in score.keys() if f"{s}.txt" not in valid.keys()]
    for p in plist:
        score.pop(p)
else:
    valid = all_

is_query = valid.keys()
label = []
all_answer = []

#Year candidate
for qid in score.keys():
    sc = list(score[qid].items())
    sc.sort(key=lambda x: int(x[1]["rank"]), reverse=False)
    if delete_query:
        an = [(f"{aa[0]}.txt", float(aa[1]["score"])) for aa in sc if aa[0] != qid and f"{aa[0]}.txt" in candidate[f"{qid}.txt"] and f"{aa[0]}.txt" not in is_query]
    else:
        an = [(f"{aa[0]}.txt", float(aa[1]["score"])) for aa in sc if aa[0] != qid and f"{aa[0]}.txt" in candidate[f"{qid}.txt"]]
    all_answer.append(an)
    label.append(valid[f"{qid}.txt"])


#You can change the range and step if you want.
rs = []
for percent in range(10, 100, 2):
    p = percent / 100
    for h in range(4, 20):
        for l in range(1, h):
            new_answer = []
            for j, qid in enumerate(score.keys()):
                now_answer = [all_answer[j][i][0] for i in range(l)]
                biggest = all_answer[j][0][1]
                for i in range(l, h):
                    if biggest > 0:
                        if all_answer[j][i][1] >= p * biggest:
                            now_answer.append(all_answer[j][i][0])
                        else:
                            break
                    elif all_answer[j][i][1] >= biggest / p:
                        now_answer.append(all_answer[j][i][0])
                    else:
                        break
                new_answer.append(now_answer)
            rs.append(((p, h, l), my_classification_report(label, new_answer)))

rs.sort(key=lambda x: x[1][0], reverse=True)
print(rs[:10])
print(rs[-10:])




