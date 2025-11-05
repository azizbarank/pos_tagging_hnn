import conllu


def read_corpus(file_path):
    """Read a CoNLL-U file and return sentences as lists of (word, tag) tuples."""
    with open(file_path, "r", encoding="utf-8") as f:
        sentences = conllu.parse(f.read())

    result = []
    for sentence in sentences:
        words_tags = []
        for token in sentence:
            if not isinstance(token["id"], int):
                continue
            word = token["form"]
            tag = token["upos"]
            words_tags.append((word, tag))
        result.append(words_tags)

    return result
