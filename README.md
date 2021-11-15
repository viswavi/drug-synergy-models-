# drug-synergy-models-
Code to accompany a new dataset for extracting information about the efficacy of drug combinations from biomedical text.

<img width="776" alt="Screen Shot 2021-11-15 at 2 23 19 AM" src="https://user-images.githubusercontent.com/2577384/141739083-4fec1b00-fac1-4627-a48a-29b768adee2a.png">


### Data
Data can be found in `data/final_train_set.jsonl` and `data/final_test_set.jsonl`.

### Usage
To run with default settings, you can simply run `python train.py`.

```
usage: train.py [--pretrained-lm PRETRAINED_LM (defaults to "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract")] \
                [--training-file TRAINING_FILE  (defaults to data/examples2_80.jsonl)] \
                [--test-file TEST_FILE  (defaults to data/examples2_20.jsonl)] \
                [--batch-size BATCH_SIZE (defaults to 12)] \
                [--dev-train-split DEV_TRAIN_SPLIT (defaults to 0.1)] \
                [--max-seq-length MAX_SEQ_LENGTH (defaults to 512)]
                [--preserve-case (defaults to False)] \
                [--num-train-epochs NUM_TRAIN_EPOCHS (defaults to 3)]
```

To train 8 models with different foundation models (SciBERT, PubmedBert, etc), run:
```
./scripts/launch_trainings_with_foundation_models.sh
```

### Requirements
[PyTorch](https://pytorch.org/get-started/locally/)

pytorch_lightning

jsonlines


