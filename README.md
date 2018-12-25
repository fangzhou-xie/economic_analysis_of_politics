# economic_analysis_of_politics

This repo consists of some files related to the term paper for Economic Analysis of Politics at NYU.

For the empitical part, I have basically based on [BERT](https://github.com/google-research/bert#fine-tuning-with-bert) model,
and made some fine-tuning modification, as shown in the run_classifer_1.py.
However, this file cannot be run by itself, and must be companied by others at BERT website.

The training setting is as follows:

> export BERT_BASE_DIR=/path/to/bert/uncased_L-12_H-768_A-12\
> export POLI_DIR=/path/to/rwcp
> 
> python run_classifier_1.py \\\
>  --task_name=POLI \\\
>  --do_train=true \\\
>  --do_eval=true \\\
>  --data_dir=$POLI_DIR/ \\\
>  --vocab_file=$BERT_BASE_DIR/vocab.txt \\\
>  --bert_config_file=$BERT_BASE_DIR/bert_config.json \\\
>  --init_checkpoint=$BERT_BASE_DIR/bert_model.ckpt \\\
>  --max_seq_length=64 \\\
>  --train_batch_size=64 \\\
>  --learning_rate=2e-5 \\\
>  --num_train_epochs=3.0 \\\
>  --output_dir=$POLI_DIR/output/
  
And the testing setting is:

> export TRAINED_CLASSIFIER=/path/to/trained/classifier
>
> python run_classifier_1.py \\\
>   --task_name=POLI \\\
>   --do_predict=true \\\
>   --data_dir=$POLI_DIR/ \\\
>   --vocab_file=$BERT_BASE_DIR/vocab.txt \\\
>   --bert_config_file=$BERT_BASE_DIR/bert_config.json \\\
>   --init_checkpoint=$TRAINED_CLASSIFIER \\\
>   --max_seq_length=64 \\\
>   --output_dir=$POLI_DIR/poli_predict/


The training set is all.tsv, where each column was seperated by Tab ('\t'), instead of CSV file (using ',').
The whole file was splited into three (test.tsv, train.tsv, dev.tsv), which is required by the classifier model.
I split the whole set into three by wikidiv.py. After training, the test.tsv set is used to evaluate accuracy of 
this model and the result is in eval_results.txt file, which reports as follows:

> eval_accuracy = 0.8078547\
> eval_loss = 0.49700302\
> global_step = 2043\
> loss = 0.49700302

Further I chose two articles from Wikipedia, namely 
[Democratic Party](https://en.wikipedia.org/wiki/Democratic_Party_(United_States)) and 
[Republican Party](https://en.wikipedia.org/wiki/Republican_Party_(United_States)), 
and classify each sentence. Results are in dem_test_results.tsv and rep_test_results.tsv, respectively.
