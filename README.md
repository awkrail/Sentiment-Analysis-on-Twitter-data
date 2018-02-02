# Sentiment-Analysis-on-Twitter-data
Sentiment-Analysis-on-Twitter-data

## Usage

### 1. Download Dataset
Download dataset from here(https://archive.ics.uci.edu/ml/datasets/Sentiment+Labelled+Sentences), and add all .txt file to dataset directory.

### 2. build docker image from Dockerfile

```bash
docker build -t [imagename]/[tagname]:1.0 .
docker run -it [imagename]/[tagname]:1.0 /bin/bash
python train.py
# 0.71 <- accuracy
```
