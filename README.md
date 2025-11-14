# POS Tagging with Hidden Markov Models

##Author
Aziz Baran Kurtulus

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

| Model | Accuracy | Runtime |
|-------|----------|---------|
| Bigram HMM | 15.84% | ~4 seconds |
| Trigram HMM | 19.32% | ~19 seconds |

The trigram model provides better context by considering two previous tags instead of one, resulting in improved accuracy.

## Directory Structure

```
.
├── README.md
├── corpus_reader.py          # CoNLL-U format reader
├── hmm_trainer.py            # Bigram transition/emission training
├── viterbi.py                # Bigram Viterbi algorithm
├── evaluate.py               # Bigram model evaluation
├── hmm_trainer_trigram.py    # Trigram transition training
├── viterbi_trigram.py        # Trigram Viterbi algorithm
├── evaluate_trigram.py       # Trigram model evaluation
├── data/                     # Data directory
│   ├── de_gsd-ud-train.conllu    # Training data
│   ├── de_gsd-ud-dev.conllu      # Development data
│   └── de_gsd-ud-test.conllu     # Test data
├── pyproject.toml
└── uv.lock
```

## Additional Details

- I used log probabilities to prevent numerical underflow