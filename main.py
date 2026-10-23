import nltk
from nltk import word_tokenize, pos_tag, RegexpParser

# Download required resources
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

# Input sentence
sentence = input("Enter a sentence: ")

# Step 1: Tokenization
tokens = word_tokenize(sentence)

# Step 2: POS Tagging
tagged_words = pos_tag(tokens)
print("\nPOS Tagged Words:")
print(tagged_words)

# Step 3: Define chunking rules
grammar = r"""
    NP: {<DT>?<JJ.*>*<NN.*>+}
    PP: {<IN><NP>}
    VP: {<MD>?<VB.*>+}
"""

# Step 4: Create chunk parser
parser = RegexpParser(grammar)

# Step 5: Perform chunking
tree = parser.parse(tagged_words)
print("\nChunked Output:")
print(tree)

# Step 6: Display identified phrases
print("\nIdentified Phrases:")
for subtree in tree.subtrees():
    if subtree.label() in ['NP', 'VP', 'PP']:
        phrase = " ".join(word for word, tag in subtree.leaves())
        print(subtree.label(), ":", phrase)

# Step 7: Display tree
print("\nChunk Tree:")
tree.pretty_print()