

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
ps = PorterStemmer()
new_text = "I want to walk today evening, but yesterday I walked a lot. I love walking. Walker walks us "
words = word_tokenize(new_text)
for w in words:
    print(ps.stem(w))