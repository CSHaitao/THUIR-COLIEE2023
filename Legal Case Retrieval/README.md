
# Legal Case Retrieval

To be specific, we design structure-aware pre-trained language models to enhance the understanding of legal cases. Furthermore, we propose heuristic pre-processing and post-processing approaches to reduce the influence of irrelevant messages. In the end, learning-to-rank methods are employed to merge features with different dimensions.


## Pre-processing

`process.py` file is used for preprocessing legal cases, including removing certain symbols and tags, removing French, concatenating abstracts, and more. 

`reference.py` file only retains sentences containing special tags and adjacent sentences. 

`summary.py` file is used for extracting the summary from an unprocessed file. 


## Traditional Lexical Matching Models

We implement BM25 and QLD with the [Pyserini](https://github.com/castorini/pyserini).

`lexical models` directory provides an example for reproduction.

## SAILER

SAILER stands for Structure-aware Pre-trained Language Model for Legal Case Retrieval, which has been accepted by SIGIR2023.

The implementation and checkpoint of SAILER can be viewed at [SAILER](https://github.com/lihaitao18375278/SAILER)



## Learning to rank

`lightgbm` directory provides the implementation of Lightgbm.

python lgb_ltr.py -process process feauture data to feat.txt and group.txt

python lgb_ltr.py -train

python lgb_ltr.py -predict

The format of feauture data (like ranklib):
0 qid:10002 1:0.007477 2:0.000000 ... 45:0.000000 46:0.007042 

Reference: [Link](https://github.com/jiangnanboy/learning_to_rank)

## Post-processing

`year.py` file is used for generating the JSON file filtering by trial date. Note that this file uses raw documents, which are not included in this folder. Please make sure the necessary documents are provided before running this script.

`grid_search.py` file is used for searching the hyperparameters (p, l, h), where `p` denotes the truncation percentage relative to the highest score, `l` denotes the minimum number of answers, and `h` denotes the maximum number of answers. This file requires two JSON files: one for year filtering and another for score results.

`inference.py` file is used for generating the JSON file of test set results with customizable hyperparameters. Like `grid_search.py`, this file requires two JSON files for year filtering and score results.

Files with prefix "score" in the folder are score result files in the following format: 

```json
{
	"query_id1": {
		"doc_id1": {
			"score": _score1,
			"rank": _rank1
		}, 
		"doc_id2": {
			"score": _score2,
			"rank": _rank2
		}, 
		...
	},
	...
}
```


## utils

`eval.py` is the evaluation code we provided. The input result should be in trec format.

`train_qid` and `valid_qid` reflect the ids of our training and validation sets.
