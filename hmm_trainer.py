def train_transition_probs(sentences):
    """Train transition probabilities from sentences."""
    transition_counts = {}
    tag_counts = {}

    for sentence in sentences:
        prev_tag = "<START>"
        tag_counts[prev_tag] = tag_counts.get(prev_tag, 0) + 1

        for word, tag in sentence:
            key = (prev_tag, tag)
            transition_counts[key] = transition_counts.get(key, 0) + 1
            tag_counts[tag] = tag_counts.get(tag, 0) + 1
            prev_tag = tag

    transition_probs = {}
    for (prev_tag, curr_tag), count in transition_counts.items():
        transition_probs[(prev_tag, curr_tag)] = count / tag_counts[prev_tag]

    return transition_probs


def train_emission_probs(sentences):
    """Train emission probabilities P(word | tag) from sentences."""
    emission_counts = {}
    tag_counts = {}

    for sentence in sentences:
        for word, tag in sentence:
            key = (tag, word)
            emission_counts[key] = emission_counts.get(key, 0) + 1
            tag_counts[tag] = tag_counts.get(tag, 0) + 1

    emission_probs = {}
    for (tag, word), count in emission_counts.items():
        emission_probs[(tag, word)] = count / tag_counts[tag]

    return emission_probs
