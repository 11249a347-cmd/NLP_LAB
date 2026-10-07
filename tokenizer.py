import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
text = "She drank watermelon juice, but it didn't satisfy her thirst"
print(sent_tokenize(text))
print(word_tokenize(text))