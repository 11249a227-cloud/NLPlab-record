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

def bigram_probability(sentence):
    words = sentence.split()

    probability = word_freq.get(words[0], 0) / total_words

    for i in range(len(words)-1):
        pair = (words[i], words[i+1])

        if pair in bigram_freq:
            probability *= bigram_freq[pair] / word_freq[words[i]]
        else:
            return 0

    return probability

s1 = "I like NLP"
s2 = "Python like I"

p1 = bigram_probability(s1)
p2 = bigram_probability(s2)

print("Sentence:", s1)
print("Probability:", p1)

print("\nSentence:", s2)
print("Probability:", p2)

if p1 > p2:
    print("\nMore Probable Sentence: I like NLP")
else:
    print("\nMore Probable Sentence: Python like I")