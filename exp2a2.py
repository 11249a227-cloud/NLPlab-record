import nltk
from nltk import word_tokenize, pos_tag, RegexpParser
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
sentence = "The teacher explains the lesson in the classroom."
tokens = word_tokenize(sentence)
tagged_words = pos_tag(tokens)
grammar = r"""
    NP: {<DT>?<JJ.*>*<NN.*>+}
    PP: {<IN><NP>}
"""
chunker = RegexpParser(grammar)
tree = chunker.parse(tagged_words)
print("Sentence:", sentence)
print("\nPOS Tagged Words:")
print(tagged_words)
print("\nChunked Output:")
print(tree)
print("\nIdentified Phrases:")
for subtree in tree.subtrees():
    if subtree.label() in ['NP', 'PP']:
        phrase = " ".join(word for word, tag in subtree.leaves())
        print(subtree.label(), ":", phrase)