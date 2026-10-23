import nltk
from nltk import word_tokenize, pos_tag, RegexpParser
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
sentence = input("Enter a sentence: ")
tokens = word_tokenize(sentence)
tagged_words = pos_tag(tokens)
print("\nPOS Tagged Words:")
print(tagged_words)
grammar = r"""
    NP: {<DT>?<JJ.*>*<NN.*>+}
    PP: {<IN><NP>}
    VP: {<VB.*>+}
"""
chunk_parser = RegexpParser(grammar)
chunk_tree = chunk_parser.parse(tagged_words)
print("\nChunked Output:")
print(chunk_tree)
print("\nIdentified Phrases:")
for subtree in chunk_tree.subtrees():
    if subtree.label() in ['NP', 'VP', 'PP']:
        phrase = " ".join(word for word, tag in subtree.leaves())
        print(subtree.label(), ":", phrase)

chunk_tree.pretty_print()