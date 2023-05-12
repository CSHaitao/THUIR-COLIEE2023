
# THUIR-COLIEE2023
This repository presents the code of THUIR team in COLIEE2023 Task 1 and Task 2. Details can be found in the relevant papers.

In task 1 Legal Case Retrieval, THUIR won the championship [paper](https://arxiv.org/abs/2305.06812). In task 2 Legal Case Entailment, THUIR received the third place [paper](https://arxiv.org/abs/2305.06817).

# Task 1: Legal Case Retrieval

This legal case competition focuses on two aspects of legal information processing related to a database of predominantly Federal Court of Canada case laws, provided by Compass Law.

The legal case retrieval task involves reading a new case Q, and extracting supporting cases S1, S2, ... Sn for the decision of Q from the entire case law corpus. Through the document, we will call the supporting cases for the decision of a new case 'noticed cases'.


## Results

|  Team  |    Submission     | Precision | Recall | F1 score |
| :----: | :---------------: | :-------: | :----: | :------: |
| THUIR  |     thuirrun2     |  0.2379   | 0.4063 |  0.3001  |
| THUIR  |     thuirrun3     |  0.2173   | 0.4389 |  0.2907  |
| IITDLI | iitdli_task1_run3 |  0.2447   | 0.3481 |  0.2874  |
| THUIR  |     thuirrun1     |  0.2186   | 0.3782 |  0.2771  |
|  NOWJ  |  nowj.d-ensemble  |  0.2263   | 0.3527 |  0.2757  |



# Task 2: Legal Case Entailment

This task involves the identification of a paragraph from existing cases that entails the decision of a new case.

Given a decision Q of a new case and a relevant case R, a specific paragraph that entails the decision Q needs to be identified. We confirmed that the answer paragraph can not be identified merely by information retrieval techniques using some examples. Because the case R is a relevant case to Q, many paragraphs in R can be relevant to Q regardless of entailment.

This task requires one to identify a paragraph which entails the decision of Q, so a specific entailment method is required which compares the meaning of each paragraph in R and Q in this task.

## Results

|  Team   |    Submission    | Precision | Recall | F1 score |
| :-----: | :--------------: | :-------: | :----: | :------: |
| CAPTAIN |     mt5l-ed      |  0.7870   | 0.7083 |  0.7456  |
| CAPTAIN |     mt5l-ed4     |  0.7864   | 0.6750 |  0.7265  |
|  THUIR  |   thuir-monot5   |  0.7900   | 0.6583 |  0.7182  |
| CAPTAIN |     mt5l-e2      |  0.7596   | 0.6583 |  0.7054  |
|  THUIR  | thuir-ensemble_2 |  0.7315   | 0.6583 |  0.6930  |




## Dataset

Please visit [COLIEE 2023](https://sites.ualberta.ca/~rabelo/COLIEE2023/) to apply for the whole dataset.


## Citation
```
@misc{li2023sailer,
      title={SAILER: Structure-aware Pre-trained Language Model for Legal Case Retrieval}, 
      author={Haitao Li and Qingyao Ai and Jia Chen and Qian Dong and Yueyue Wu and Yiqun Liu and Chong Chen and Qi Tian},
      year={2023},
      eprint={2304.11370},
      archivePrefix={arXiv},
      primaryClass={cs.IR}
}
```

```
@misc{li2023thuircoliee,
      title={THUIR@COLIEE 2023: Incorporating Structural Knowledge into Pre-trained Language Models for Legal Case Retrieval}, 
      author={Haitao Li and Weihang Su and Changyue Wang and Yueyue Wu and Qingyao Ai and Yiqun Liu},
      year={2023},
      eprint={2305.06812},
      archivePrefix={arXiv},
      primaryClass={cs.IR}
}
```

```
@misc{li2023thuircoliee,
      title={THUIR@COLIEE 2023: More Parameters and Legal Knowledge for Legal Case Entailment}, 
      author={Haitao Li and Changyue Wang and Weihang Su and Yueyue Wu and Qingyao Ai and Yiqun Liu},
      year={2023},
      eprint={2305.06817},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

## Contact

If you find our work useful, please do not save your star!

If you have any questions, please email liht22@mails.tsinghua.edu.cn
