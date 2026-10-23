import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
nltk.download('punkt')
text = "All INDIANs are my Bothers and Sisters , INDIA is my Country."
sentences = sent_tokenize(text)
print("Sentences:")
print(sentences)
words = word_tokenize(text)
print("\nWords:")
print(words)