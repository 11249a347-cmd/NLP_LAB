import nltk
from nltk.tokenize import word_tokenize
from nltk.util import ngrams

text = input("Enter a sentence: ")
tokens = word_tokenize(text)
print("\nOriginal Tokens")
print(tokens)

print("\nUnigrams")
for gram in ngrams(tokens, 1):
    print(gram)
print("\nBigrams")
for gram in ngrams(tokens, 2):
    print(gram)
print("\nTrigrams")
for gram in ngrams(tokens, 3):
    print(gram)

'''output:
Enter a sentence: Natural Language Processing is an exciting field.

 Part-of-Speech Tags
-----------------------------------
Natural         JJ
Language        NNP
Processing      NNP
is              VBZ
an              DT
exciting        JJ
field           NN
.               .
'''
