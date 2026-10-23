from collections import Counter

corpus = [
    "I like NLP",
    "I like Python",
    "I study NLP"
]

word_freq = Counter()
bigram_freq = Counter()

for sentence in corpus:
    words = sentence.split()
    word_freq.update(words)

    for i in range(len(words)-1):
        bigram_freq[(words[i], words[i+1])] += 1

total_words = sum(word_freq.values())
vocabulary = len(word_freq)

def laplace_probability(sentence):
    words = sentence.split()

    probability = (word_freq.get(words[0], 0) + 1) / (total_words + vocabulary)

    for i in range(len(words)-1):
        pair = (words[i], words[i+1])

        numerator = bigram_freq.get(pair, 0) + 1
        denominator = word_freq.get(words[i], 0) + vocabulary

        probability *= numerator / denominator

    return probability

s1 = "I like NLP"
s2 = "Python like I"

print("Sentence:", s1)
print("Probability:", laplace_probability(s1))

print("\nSentence:", s2)
print("Probability:", laplace_probability(s2))