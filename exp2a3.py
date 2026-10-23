import nltk
from nltk import word_tokenize, pos_tag, RegexpParser
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
sentence = "The young researcher develops an AI model."
tokens = word_tokenize(sentence)
tagged_words = pos_tag(tokens)
grammar = r"""
    NP: {<DT>?<JJ.*>*<NN.*>+}
"""
chunker = RegexpParser(grammar)
tree = chunker.parse(tagged_words)
print("Sentence:", sentence)
print("\nPOS Tagged Sequence:")
for word, tag in tagged_words:
    print(f"{word}/{tag}", end=" ")
print()
print("\nChunked Sentence:")
print(tree)
print("\nNoun Phrases:")
for subtree in tree.subtrees():
    if subtree.label() == 'NP':
        phrase = " ".join(word for word, tag in subtree.leaves())
        print("[", phrase, "] NP")