def viterbi(words, transition_probs, emission_probs, all_tags):
    """Find the most likely tag sequence for the given words."""
    n = len(words)
    viterbi_table = [{} for _ in range(n)]
    backpointer = [{} for _ in range(n)]

    # Initialize first word
    for tag in all_tags:
        trans_prob = transition_probs.get(("<START>", tag), 0)
        emit_prob = emission_probs.get((tag, words[0]), 0)
        viterbi_table[0][tag] = trans_prob * emit_prob
        backpointer[0][tag] = "<START>"

    # Fill remaining positions
    for i in range(1, n):
        word = words[i]
        for curr_tag in all_tags:
            max_prob = 0
            best_prev = None

            for prev_tag in all_tags:
                prev_prob = viterbi_table[i - 1].get(prev_tag, 0)
                trans = transition_probs.get((prev_tag, curr_tag), 0)
                emit = emission_probs.get((curr_tag, word), 0)
                prob = prev_prob * trans * emit

                if prob > max_prob:
                    max_prob = prob
                    best_prev = prev_tag

            viterbi_table[i][curr_tag] = max_prob
            backpointer[i][curr_tag] = best_prev

    # Find best final tag
    best_tag = max(viterbi_table[n - 1], key=viterbi_table[n - 1].get)
    best_prob = viterbi_table[n - 1][best_tag]

    # Backtrack
    tags = [best_tag]
    for i in range(n - 1, 0, -1):
        best_tag = backpointer[i][best_tag]
        tags.insert(0, best_tag)

    return tags, best_prob
