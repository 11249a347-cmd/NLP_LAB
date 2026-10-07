import nltk
from nltk.tokenize import word_tokenize
sentence = input("Enter a sentence: ")
words = word_tokenize(sentence)
pos_tags= nltk.pos_tag(words)
print("\n Word  \t \Pos Tag")
print("_"*30)
for word, tag in pos_tags:
    print(f"{word:<15} \t \t {tag}")
