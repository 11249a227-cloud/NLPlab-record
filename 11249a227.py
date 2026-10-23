import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
nltk.download('punkt')
text = "Natural Language Processing is amazing. It helps computers understand human language."
sentences = sent_tokenize(text)
print("Sentences:")
print(sentences)
words = word_tokenize(text)
print("\nWords:")
print(words)