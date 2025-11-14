def train_trigram_transition_probs(sentences):
    """Train trigram transition probabilities P(tag_i | tag_{i-2}, tag_{i-1})."""
    trigram_counts = {}
    bigram_counts = {}

    for sentence in sentences:
        prev_prev_tag = "<START>"
        prev_tag = "<START>"
        bigram_counts[(prev_prev_tag, prev_tag)] = (
            bigram_counts.get((prev_prev_tag, prev_tag), 0) + 1
        )

        for word, tag in sentence:
            key = (prev_prev_tag, prev_tag, tag)
            trigram_counts[key] = trigram_counts.get(key, 0) + 1
            bigram_counts[(prev_prev_tag, prev_tag)] = (
                bigram_counts.get((prev_prev_tag, prev_tag), 0) + 1
            )
            prev_prev_tag = prev_tag
            prev_tag = tag

    trigram_probs = {}
    for (tag1, tag2, tag3), count in trigram_counts.items():
        trigram_probs[(tag1, tag2, tag3)] = count / bigram_counts[(tag1, tag2)]

    return trigram_probs
