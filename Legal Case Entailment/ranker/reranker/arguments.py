# Copyright 2021 Reranker Author. All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

import os
from dataclasses import dataclass, field
from typing import Optional, Union, List
from transformers import TrainingArguments


@dataclass
class ModelArguments:
    """
    Arguments pertaining to which model/config/tokenizer we are going to fine-tune from.
    """

    model_name_or_path: str = field(
        metadata={"help": "Path to pretrained model or model identifier from huggingface.co/models"}
    )
    config_name: Optional[str] = field(
        default=None, metadata={"help": "Pretrained config name or path if not the same as model_name"}
    )
    tokenizer_name: Optional[str] = field(
        default=None, metadata={"help": "Pretrained tokenizer name or path if not the same as model_name"}
    )
    cache_dir: Optional[str] = field(
        default=None, metadata={"help": "Where do you want to store the pretrained models downloaded from s3"}
    )
    temperature: Optional[float] = field(default=None)


@dataclass
class DataArguments:
    train_dir: str = field(
        default=None, metadata={"help": "Path to train directory"}
    )
    train_path: Union[str] = field(
        default=None, metadata={"help": "Path to train data"}
    )
    train_group_size: int = field(default=8)
    dev_path: str = field(
        default=None, metadata={"help": "Path to dev data"}
    )
    pred_path: List[str] = field(default=None, metadata={"help": "Path to prediction data"})
    pred_dir: str = field(
        default=None, metadata={"help": "Path to prediction directory"}
    )
    pred_id_file: str = field(default=None)
    rank_score_path: str = field(default=None, metadata={"help": "where to save the match score"})
    max_len: int = field(
        default=128,
        metadata={
            "help": "The maximum total input sequence length after tokenization for passage. Sequences longer "
                    "than this will be truncated, sequences shorter will be padded."
        },
    )

    # def __post_init__(self):
    #     if self.train_dir is not None:
    #         files = os.listdir(self.train_dir)
    #         self.train_path = [
    #             os.path.join(self.train_dir, f)
    #             for f in files
    #             if f.endswith('tsv') or f.endswith('json')
    #         ]
    #     if self.pred_dir is not None:
    #         files = os.listdir(self.pred_dir)
    #         self.pred_path = [
    #             os.path.join(self.pred_dir, f)
    #             for f in files
    #         ]


@dataclass
class RerankerTrainingArguments(TrainingArguments):
    warmup_ratio: float = field(default=0.1)
    distance_cache: bool = field(default=False)
    distance_cache_stride: int = field(default=2)

    collaborative: bool = field(default=False)
    warmup_ratio: float = field(default=0.1)
    remove_unused_columns: bool = field(default=False)
    ##缺很多参数
    local_rank: int = field(default=-1, metadata={"help": "For distributed training: local_rank"})
    fp16: bool = field(
        default=True,
        metadata={"help": "Whether to use 16-bit (mixed) precision (through NVIDIA apex) instead of 32-bit"},
    )
    # distributed: bool = field(
    #     default=False,
    #     metadata={"help": "Whether to use 16-bit (mixed) precision (through NVIDIA apex) instead of 32-bit"},
    # )


    output_dir: str = field(default=None) # where to output
    logging_dir: str = field(default=None)

    no_cuda: bool = field(default=False, metadata={"help": "Do not use CUDA even when it is available"})
    seed: int = field(default=42, metadata={"help": "random seed for initialization"})

    padding: bool = field(default=True)
    optimizer_str: str = field(default="lamb") # or lamb
    overwrite_output_dir: bool = field(default=False)    
    per_device_train_batch_size: int = field(
        default=48, metadata={"help": "Batch size per GPU/TPU core/CPU for training."})
    gradient_accumulation_steps: int = field(
        default=3,
        metadata={"help": "Number of updates steps to accumulate before performing a backward/update pass."},)

    learning_rate: float = field(default=1e-3, metadata={"help": "The initial learning rate for Adam."})
    weight_decay: float = field(default=0.01, metadata={"help": "Weight decay if we apply some."})
    adam_beta1: float = field(default=0.9, metadata={"help": "Beta1 for Adam optimizer"})
    adam_beta2: float = field(default=0.999, metadata={"help": "Beta2 for Adam optimizer"})
    adam_epsilon: float = field(default=1e-8, metadata={"help": "Epsilon for Adam optimizer."})
    max_grad_norm: float = field(default=1.0, metadata={"help": "Max gradient norm."})

    num_train_epochs: float = field(default=3, metadata={"help": "Total number of training epochs to perform."})
    max_steps: int = field(
        default=-1,
        metadata={"help": "If > 0: set total number of training steps to perform. Override num_train_epochs."},
    )
    # warmup_steps: int = field(default=5000, metadata={"help": "Linear warmup over warmup_steps."})

    logging_first_step: bool = field(default=False, metadata={"help": "Log and eval the first global_step"})
    logging_steps: int = field(default=50, metadata={"help": "Log every X updates steps."}) 
    save_steps: int = field(default=2000, metadata={"help": "Save checkpoint every X updates steps."})
    
    do_train: bool = field(default=True)
