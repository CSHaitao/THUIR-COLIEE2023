
# Legal Case Entailment

We try traditional lexical matching methods and pre-trained language models with different sizes.Furthermore, learning-to-rank methods are employed to further improve performance.



## Traditional Lexical Matching Models

We implement BM25 and QLD with the [Pyserini](https://github.com/castorini/pyserini).

`lexical models` directory provides an example for reproduction.

## Cross Encoder

`cross encoder` directory provides the training code for cross encoder.

Reference: [Link](https://github.com/luyug/Reranker)

You can run by the following command:

```
sh ./ranker/train.sh
```


## Sequence-to-Sequence Model

`T5` directory provides the training code for sequence-to-sequence model.

You can run by the following command:

```
sh ./T5/train.sh
```



## Inference

Inference.py provides the inference code for cross encoder and t5

For T5:
```
model = T5ForConditionalGeneration.from_pretrained('checkpoint-10000').to(device).eval()
reranker = MonoT5(model=model)
```

For cross encoder:

```
model = AutoModelForSequenceClassification.from_pretrained('/').to(device).eval()
tokenizer = AutoTokenizer.from_pretrained('', use_fast=False)
reranker = MonoBERT(model,tokenizer)
```

## Evaluation

The evaluation code can refer to the evaluation code of Task 1.

