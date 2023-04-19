
# Legal Case Entailment

We try traditional lexical matching methods and pre-trained language models with different sizes.Furthermore, learning-to-rank methods are employed to further improve performance.



## Traditional Lexical Matching Models

We implement BM25 and QLD with the [Pyserini](https://github.com/castorini/pyserini).

`lexical models` directory provides an example for reproduction.

## Cross Encoder

`cross encoder` directory provides the training code for cross encoder.

Reference: [Link](https://github.com/luyug/Reranker)


## Sequence-to-Sequence Model

`T5` directory provides the training code for sequence-to-sequence model.

## Inference

Inference.py provides the inference code for cross encoder and t5


## Evaluation

The evaluation code can refer to the evaluation code of Task 1.

