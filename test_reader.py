from corpus_reader import read_corpus

# Test with dev set (smaller)
sentences = read_corpus("data/de_gsd-ud-dev.conllu")

print(f"Total sentences: {len(sentences)}")
print("\nFirst 3 sentences:")
for i, sent in enumerate(sentences[:3]):
    print(f"\nSentence {i + 1}:")
    print(sent)
