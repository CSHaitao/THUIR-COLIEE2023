import json

p = 0.34
l = 3
h = 7
test_score_file_path = "./score_test_output_order.json"
delete_query = True
output_file_name = f"./{p}_{l}_{h}_delete_query_v2.json"

with open(test_score_file_path) as f:
    score = json.load(f)

with open("./task1_test_no_labels_2023.json") as f:
    valid = json.load(f)

with open("./candidate_test.json") as f:
    candidate = json.load(f)

is_query = valid.keys()

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

end_answer = {}
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
    end_answer[f"{qid}.txt"] = now_answer

with open(output_file_name, "w+") as f:
    f.write(json.dumps(end_answer, indent=1))


