import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
text = input("Enter a sentence: ")

tokens = word_tokenize(text)
tags = pos_tag(tokens)
print("\n Part-of-Speech Tags")
print("-"*35)

for word, tag in tags:
    print(f"{word:<15} {tag}")

# The quick brown fox jumps over the lazy dog