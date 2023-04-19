
###
 # @Author: lihaitao
 # @Date: 2023-03-27 11:50:37
 # @LastEditors: Do not edit
 # @LastEditTime: 2023-03-27 20:11:23
 # @FilePath: /Coliee2023/Task2/train_t5/sft/train.sh
### 

deepspeed --master_port 29500 --num_gpus=1 train_gptj_summarize.py --deepspeed ds_config_gptj.json
# CUDA_VISIBLE_DEVICES=5
# accelerate launch --main_process_port=29500 --num_processes=1 train_gptj_summarize.py

# CUDA_VISIBLE_DEVICES=2
# python3 -m torch.distributed.launch \
#   --nproc_per_node 1 \
#   --master_port 29508 \
#   train_gptj_summarize.py \
#   --fp16 \