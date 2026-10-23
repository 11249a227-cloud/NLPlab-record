import nltk
from nltk import word_tokenize, pos_tag, RegexpParser
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
sentences = [
    "The tall boy runs fast.",
    "A beautiful flower blooms.",
    "The computer science student studies NLP."
]
grammar = r"""
    NP: {<DT>?<JJ.*>*<NN.*>+}
"""
chunker = RegexpParser(grammar)
for sentence in sentences:
    print("\nSentence:", sentence)
    tokens = word_tokenize(sentence)
    tagged_words = pos_tag(tokens)
    tree = chunker.parse(tagged_words)
    print("POS Tags:", tagged_words)
    print("Chunk Tree:", tree)
    print("Noun Phrases:")
    for subtree in tree.subtrees():
        if subtree.label() == 'NP':
            print(" ".join(word for word, tag in subtree.leaves()))