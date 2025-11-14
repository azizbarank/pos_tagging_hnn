import math


def get_emission_prob(word, tag, emission_probs, all_tags):
    """Get log emission probability, using uniform probability for unknown words."""
    key = (tag, word)
    if key in emission_probs:
        return math.log(emission_probs[key])
    return math.log(1.0 / len(all_tags))


def viterbi_trigram(words, trigram_probs, emission_probs, all_tags):
    """Find the most likely tag sequence using trigram transitions."""
    n = len(words)
    if n == 0:
        return [], 0

    viterbi_table = [{} for _ in range(n)]
    backpointer = [{} for _ in range(n)]

    # First word
    for tag in all_tags:
        key = ("<START>", "<START>", tag)
        trans = trigram_probs.get(key, 1e-10)
        emit = get_emission_prob(words[0], tag, emission_probs, all_tags)
        viterbi_table[0][tag] = math.log(trans) + emit
        backpointer[0][tag] = "<START>"

    if n == 1:
        best_tag = max(viterbi_table[0], key=viterbi_table[0].get)
        return [best_tag], viterbi_table[0][best_tag]

    # Second word
    for prev_tag in all_tags:
        prev_log_prob = viterbi_table[0].get(prev_tag, float("-inf"))

        for curr_tag in all_tags:
            key = ("<START>", prev_tag, curr_tag)
            trans = trigram_probs.get(key, 1e-10)
            emit = get_emission_prob(words[1], curr_tag, emission_probs, all_tags)
            log_prob = prev_log_prob + math.log(trans) + emit

            if (
                curr_tag not in viterbi_table[1]
                or log_prob > viterbi_table[1][curr_tag]
            ):
                viterbi_table[1][curr_tag] = log_prob
                backpointer[1][curr_tag] = prev_tag

    # Remaining words
    for i in range(2, n):
        word = words[i]

        for curr_tag in all_tags:
            max_log_prob = float("-inf")
            best_prev = None

            for prev_tag in all_tags:
                prev_log_prob = viterbi_table[i - 1].get(prev_tag, float("-inf"))
                if prev_log_prob == float("-inf"):
                    continue

                for prev_prev_tag in all_tags:
                    key = (prev_prev_tag, prev_tag, curr_tag)
                    trans = trigram_probs.get(key, 1e-10)
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
