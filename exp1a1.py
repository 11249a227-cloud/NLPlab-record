import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
sentence = "Ravi plays cricket every evening."
tokens = nltk.word_tokenize(sentence)
tagged_words = nltk.pos_tag(tokens)
print("Word\tPOS Tag")
print("-" * 25)
for word, tag in tagged_words:
    print(f"{word}\t{tag}")
print("\nNouns, Verbs, and Adverbs:")
for word, tag in tagged_words:
    if tag.startswith('NN'):
        print(word, "- Noun")
    elif tag.startswith('VB'):
        print(word, "- Verb")
    elif tag.startswith('RB'):
        print(word, "- Adverb")