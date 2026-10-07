import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

sentence = input("Enter a sentence: ")
tokens = word_tokenize(sentence)

tagged_words = pos_tag(tokens)

print("\n Part-of-Speech Tagged Sentence")
print("-"*40)
for word, tag in tagged_words:
    print(f"{word:<15}  {tag}")

# Artificial Intelligence is transforming modern healthcare

''' output
 Part-of-Speech Tagged Sentence
----------------------------------------
Artificial       JJ
Intelligence     NNP
is               VBZ
transforming     VBG
modern           JJ
healthcare       NN
'''