# POS Tagging with Hidden Markov Models

This project implements part-of-speech tagging using Hidden Markov Models (HMMs) for German text from the Universal Dependencies GSD corpus.

## What I Implemented

The project includes:
- Corpus reader for CoNLL-U format
- HMM training (transition and emission probabilities)
- Viterbi algorithm with unknown word handling
- Evaluation on test data
- Trigram HMM extension for improved accuracy

## Requirements

- Python 3.13+
- conllu library

## Installation

### Option 1: Using UV (recommended)
```bash
uv sync
```

### Option 2: Using pip
```bash
pip install conllu
```

## Data Setup

The German GSD corpus files should be placed in the `data/` directory:
- `de_gsd-ud-train.conllu`
- `de_gsd-ud-dev.conllu`
- `de_gsd-ud-test.conllu`

## How to Run

### Bigram HMM Model
```bash
# Using UV
uv run python evaluate.py

# Using pip
python evaluate.py
```

### Trigram HMM Model
```bash
# Using UV
uv run python evaluate_trigram.py

# Using pip
python evaluate_trigram.py
```

## Results

- **Bigram Model**: 15.82% accuracy
- **Trigram Model**: 19.36% accuracy

The trigram model provides better context by considering two previous tags instead of one, resulting in improved accuracy.

## Project Structure

```
corpus_reader.py          - CoNLL-U format reader
hmm_trainer.py            - Bigram transition/emission training
viterbi.py                - Bigram Viterbi algorithm
evaluate.py               - Bigram model evaluation
hmm_trainer_trigram.py    - Trigram transition training
viterbi_trigram.py        - Trigram Viterbi algorithm
evaluate_trigram.py       - Trigram model evaluation
```