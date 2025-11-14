# POS Tagging with Hidden Markov Models Report

## Overview

I implemented a part-of-speech tagger using Hidden Markov Models (HMMs) for German text. The implementation includes both a standard bigram HMM and a trigram HMM for improved accuracy.

---

## Implementation

### Data

I used the Universal Dependencies German GSD corpus:
- Training set: 13,814 sentences
- Test set: 977 sentences

The corpus uses the Universal POS tagset with 17 tags (NOUN, VERB, ADJ, etc.).

### Components

**1. Corpus Reader** (`corpus_reader.py`)

I parsed the CoNLL-U format files using the conllu library. The reader extracts word-tag pairs from each sentence while skipping multi-word tokens (those with non-integer IDs).

**2. HMM Training** (`hmm_trainer.py`)

I trained two types of probabilities:
- **Transition probabilities** P(tag_i | tag_{i-1}): likelihood of a tag given the previous tag
- **Emission probabilities** P(word | tag): likelihood of a word given its tag

The training uses Maximum Likelihood Estimation by counting co-occurrences and normalizing by the appropriate denominators.

**3. Viterbi Algorithm** (`viterbi.py`)

I implemented the Viterbi algorithm for finding the most likely tag sequence.

I used log probabilities throughout to prevent numerical underflow when multiplying many small probabilities.

**4. Unknown Word Handling**

For words not seen during training, I use a uniform probability distribution across all tags.

---

## Results

### Bigram HMM

**Accuracy**: 15.84%
**Runtime**: ~4 seconds

The bigram model considers one previous tag when making predictions. While simple and fast, the accuracy is limited because it has limited context.

### Trigram HMM

**Accuracy**: 19.32%
**Runtime**: ~19 seconds

The trigram model considers two previous tags: P(tag_i | tag_{i-2}, tag_{i-1}). This provides more context and improves accuracy by about 22% relative to the bigram model.

For the implementation I made separate training (`hmm_trainer_trigram.py`) and decoding (`viterbi_trigram.py`) files.

---

## Discussion

### Why is the accuracy low?

The relatively low accuracy (15-19%) is expected for this simple approach:

1. **Unknown word handling**: The uniform distribution for unknown words is naive. Usingh additonal morphological features or character-level models might be helpful.

2. **No smoothing**: We only use Maximum Likelihood Estimation without any smoothing techniques. This means many valid tag transitions get zero probability if they weren't seen in training.

3. **Limited context**: Perhaps the most important factor. Even the trigram model only sees 2 previous tags. If more context is used, the improvement would probably be higher.

### Improvements

1. **Log probabilities**: Using log probabilities prevented numerical underflow and made the algorithm stable.

2. **Trigram improvement**: The 22% relative improvement from bigrams to trigrams shows that additional context helps.

---
