from corpus_reader import read_corpus
from hmm_trainer import train_transition_probs, train_emission_probs
from viterbi import viterbi


def evaluate(test_sentences, trans_probs, emit_probs, all_tags):
    """Evaluate tagging accuracy on test sentences."""
    correct = 0
    total = 0

    for sentence in test_sentences:
        words = [word for word, tag in sentence]
        gold_tags = [tag for word, tag in sentence]

        predicted_tags, _ = viterbi(words, trans_probs, emit_probs, all_tags)

        for pred, gold in zip(predicted_tags, gold_tags):
            if pred == gold:
                correct += 1
            total += 1

    accuracy = correct / total if total > 0 else 0
    return accuracy


# Train on training data
print("Loading training data...")
train_sentences = read_corpus("data/de_gsd-ud-train.conllu")
print(f"Training sentences: {len(train_sentences)}")

print("\nTraining HMM...")
trans_probs = train_transition_probs(train_sentences)
emit_probs = train_emission_probs(train_sentences)

all_tags = set()
for sent in train_sentences:
    for word, tag in sent:
        all_tags.add(tag)

# Evaluate on test data
print("\nLoading test data...")
test_sentences = read_corpus("data/de_gsd-ud-test.conllu")
print(f"Test sentences: {len(test_sentences)}")

print("\nEvaluating...")
accuracy = evaluate(test_sentences, trans_probs, emit_probs, all_tags)
print(f"\nAccuracy: {accuracy:.4f} ({accuracy * 100:.2f}%)")
