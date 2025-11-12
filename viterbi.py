import math


def get_emission_prob(word, tag, emission_probs, all_tags):
    """Get log emission probability, using uniform probability for unknown words."""
    key = (tag, word)
    if key in emission_probs:
        return math.log(emission_probs[key])
    return math.log(1.0 / len(all_tags))


def viterbi(words, transition_probs, emission_probs, all_tags):
    """Find the most likely tag sequence for the given words."""
    n = len(words)
    viterbi_table = [{} for _ in range(n)]
    backpointer = [{} for _ in range(n)]

    # Initialize first word
    for tag in all_tags:
        trans_prob = transition_probs.get(("<START>", tag), 1e-10)
        emit_prob = get_emission_prob(words[0], tag, emission_probs, all_tags)
        viterbi_table[0][tag] = math.log(trans_prob) + emit_prob
        backpointer[0][tag] = "<START>"

    # Fill remaining positions
    for i in range(1, n):
        word = words[i]
        for curr_tag in all_tags:
            max_log_prob = float("-inf")
            best_prev = None

            for prev_tag in all_tags:
                prev_log_prob = viterbi_table[i - 1].get(prev_tag, float("-inf"))
                trans = transition_probs.get((prev_tag, curr_tag), 1e-10)
                emit = get_emission_prob(word, curr_tag, emission_probs, all_tags)
                log_prob = prev_log_prob + math.log(trans) + emit

                if log_prob > max_log_prob:
                    max_log_prob = log_prob
                    best_prev = prev_tag

            viterbi_table[i][curr_tag] = max_log_prob
            backpointer[i][curr_tag] = best_prev

    # Find best final tag
    best_tag = max(viterbi_table[n - 1], key=viterbi_table[n - 1].get)
    best_log_prob = viterbi_table[n - 1][best_tag]

    # Backtrack
    tags = [best_tag]
    for i in range(n - 1, 0, -1):
        best_tag = backpointer[i][best_tag]
        tags.insert(0, best_tag)

    return tags, best_log_prob
