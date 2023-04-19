
import os
import re
names = os.listdir("./task1/task1_train_files_2023")


for name in names:
    with open(f"./task1/task1_train_files_2023/{name}", "r", encoding="utf-8") as f:
        txt = f.read()
        if "Summary:" in txt and "no summary" not in txt and "for this document are in preparation." not in txt:
            idx = txt.find("Summary:")
            end = txt.find("- Topic", idx)
            end2 = txt.rfind("\n", idx, end)
            summ=txt[idx+8:end2].strip()
            if summ.count("\n") > 20:
                continue
            with open(f"./task1/summary/{name}", "w+", encoding="utf-8") as fp:
                if summ == "":
                    print(name)
                fp.write(summ)
