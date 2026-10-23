# DFA for Vowel Recognition

def vowel(word):

    vowels = "AEIOUaeiou"

    for ch in word:
        if ch in vowels:
            print(ch, "-> Vowel")
        else:
            print(ch, "-> Not Vowel")

text = input("Enter a Word: ")

vowel(text)