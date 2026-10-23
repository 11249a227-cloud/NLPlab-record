import nltk
nlp = nltk.load("en_core_web_sm")
text = "Natural Language Processing is an interesting field."
doc = nlp(text)
print("Tokens:")
for token in doc:
    print(token.text)