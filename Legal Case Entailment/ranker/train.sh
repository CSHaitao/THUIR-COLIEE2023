
###
 # @Author: lihaitao
 # @Date: 2023-03-28 19:36:21
 # @LastEditors: Do not edit
 # @LastEditTime: 2023-04-09 22:16:55
 # @FilePath: /Coliee2023/Task2/Reranker-main/train.sh
### 
# python -m torch.distributed.launch --nproc_per_node 1 --master_port 29507 \
# CUDA_VISIBLE_DEVICES=1
# python  
CUDA_VISIBLE_DEVICES=1,8
# deepspeed --master_port 29500 --num_gpus=4 run_train.py
python -m torch.distributed.launch --nproc_per_node 2 --master_port 29507 run_train.py \
    --output_dir /home/lht/Coliee2023/Task2/Reranker-main/output/sailer_40000 \
    --model_name_or_path /home/lht/Coliee2023/Sailer \
    --tokenizer_name /home/lht/models/bert \
    --do_train \
    --logging_steps 10 \
    --save_steps 50 \
    --train_path /home/lht/Coliee2023/Task2/Reranker-main/data/train.json \
    --max_len 512 \
    --fp16 \
    --per_device_train_batch_size 1 \
    --train_group_size 8 \
    --gradient_accumulation_steps 16 \
    --per_device_eval_batch_size 2 \
    --warmup_ratio 0.1 \
    --weight_decay 0.01 \
    --learning_rate 1e-5 \
    --num_train_epochs 20 \
    --overwrite_output_dir \
    --dataloader_num_workers 8