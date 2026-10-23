import nltk
from nltk import word_tokenize, pos_tag, RegexpParser
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
sentences = [
    "A student.",
    "The very intelligent student."
]
grammar = r"""
    NP: {<DT>?<RB.*>*<JJ.*>*<NN.*>+}
"""
chunker = RegexpParser(grammar)
for sentence in sentences:
    tokens = word_tokenize(sentence)
    tagged_words = pos_tag(tokens)
    tree = chunker.parse(tagged_words)
    print("\nSentence:", sentence)
    print("POS Tags:", tagged_words)
    print("Chunk Tree:", tree)
    for subtree in tree.subtrees():
        if subtree.label() == 'NP':
            phrase = " ".join(word for word, tag in subtree.leaves())
            print("NP:", phrase)