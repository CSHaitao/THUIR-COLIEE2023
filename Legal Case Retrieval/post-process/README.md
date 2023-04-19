# POSTPROCESS

## grid_search.py

`grid_search.py` file is used for searching the hyperparameters (p, l, h), where `p` denotes the truncation percentage relative to the highest score, `l` denotes the minimum number of answers, and `h` denotes the maximum number of answers. This file requires two JSON files: one for year filtering and another for score results.

## inference.py

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

## year.py

`year.py` file is used for generating the JSON file for year filtering. Note that this file uses raw documents, which are not included in this folder. Please make sure the necessary documents are provided before running this script.