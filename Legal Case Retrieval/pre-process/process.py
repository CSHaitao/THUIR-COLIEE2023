import os
import re
from langdetect import detect
from langdetect import detect_langs
from langdetect import DetectorFactory
DetectorFactory.seed = 0


names = os.listdir("./task1/task1_train_files_2023")
have_sum = os.listdir("./task1/summary")

last_lang = "en"

def is_sentence(s):
    return s == "" or s.strip().endswith(('.', ':', ';'))

def remove(match):
    result = match.group()
    return result.replace("[", "").replace("]", "").replace(" ", "")

def remove2(match):
    result = match.group()
    return result.replace("[", "").replace("]", "")

def rep(match):
    result = match.group()
    return result.replace("[", "{").replace("]", "}")

def rep2(match):
    result = match.group()
    return result.replace("{}", "[").replace("}", "]")
total = 0
for name in names:
    with open(f"./task1/task1_train_files_2023/{name}", "r", encoding="utf-8") as f:
        t = f.read()
        idx_ = t.find("[1]")
        if idx_ != -1:
            t = t[idx_:]
        lines = t.splitlines()
        lines = [line.strip() for line in lines]
        sentence_list = []
        flag = True
        
        for l in lines:
            if flag and (
                "<FRAGMENT_SUPPRESSED>" in l
                or " FRAGMENT_SUPPRESSED" in l
                or l == ""
            ):
                continue
            flag = False
            l1 = l.replace("<FRAGMENT_SUPPRESSED>", "").replace("FRAGMENT_SUPPRESSED", "").strip()
            l2 = re.sub('\[\d{1,3}\]', "", l1).strip()
            if (
                (len(l2) == 1 or
                    (
                        l2 != ""
                        and l2[0] != "("
                        and len(l2) > 1
                        and l2[1] != ")"
                        and not l2[0].isdigit()
                    ))
                and sentence_list
                and not is_sentence(sentence_list[-1])
            ):
                sentence_list[-1] += f" {l2}"
            else:
                sentence_list.append(l2)
    txt = "\n".join(sentence_list)

    txt = re.sub("\. *(\. *)+", "", txt)
    txt = re.sub("[A-Z]*_SUPPRESSED", "", txt)
    
    need_to_removed = ["[translation]", "[Translation]", "[sic]", "[ sic ]", "[Emphasis added.]",
                       "[emphasis added]", 
                       "[End of document]", "*", "[  ]", "[]", "[ ]",
                        "[DATE_SUPPRESSED]", "[TRANSLATION]", 
                       "[English language version follows French language version]", 
                       "[La version anglaise vient à la suite de la version française]", 
                       "[Diagram omitted - see printed version]", 
                       "[French language version follows English language version]",
                       "[La version française vient à la suite de la version anglaise]", 
                       "[Traduction]"]
    for token in need_to_removed:
        txt = txt.replace(token, "")


    txt = re.sub("\[[A-Z][A-Z]+\]", rep, txt)
    txt = re.sub("[^a-zA-Z]\[[b-zB-Z]\] ", remove, txt)
    txt = re.sub("\[[a-zA-Z][a-zA-Z \.']*\]", remove2, txt)
    txt = re.sub("\{[A-Z][A-Z]+\}", rep2, txt)
    txt = re.sub("\n\n+", "\n\n", txt)
    txt = re.sub("\.\.+", ".", txt)
    txt = re.sub("\n\.\n", "\n\n", txt)
    
    new_lines = txt.split("\n")
    for i in range(len(new_lines)):
        if len(new_lines[i]) > 0:
            try:
                lang = detect(new_lines[i])
            except:
                if last_lang == "fr":
                    new_lines[i] = ""
                   
            if lang == "fr":
                last_lang = "fr"
                new_lines[i] = ""
            elif lang != "en":
                if last_lang == "fr":
                    new_lines[i] = ""
            else:
                last_lang = "en"
    
    txt = "\n".join(new_lines)     
    txt = re.sub("\n\n+", "\n\n", txt)
    
    if "Summary:" not in txt and name in have_sum:
        with open(f"./task1/summary/{name}", "r", encoding="utf-8") as f:
            sum_ = f.read()
            txt = f"Summary:\n{sum_}\n{txt}"
    with open(f"./task1/processed/{name}", "w+", encoding="utf-8") as f:
        f.write(txt)
        
    total += 1
    if total % 100 == 0:
        print(f"{total}, and total {len(names)}")