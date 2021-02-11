#!/bin/bash
#chkconfig: 2345 80 90
#description: 启动BERT分类模型 

echo '正在启动 BERT SERVICE...'
cd /home/gildata/bert/service
sudo rm -rf tmp*

export BERT_BASE_DIR=/home/gildata/bert/vocab_file/chinese_L-12_H-768_A-12
export TRAINED_CLASSIFIER=/home/gildata/bert/bert/output

bert-base-serving-start  
-model_dir $TRAINED_CLASSIFIER 
-bert_model_dir $BERT_BASE_DIR 
-model_pb_dir $TRAINED_CLASSIFIER 
-mode CLASS 
-max_seq_len 128 
-http_port 8091 
-port 5575
-port_out 5576