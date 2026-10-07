import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from collections import Counter
import string

text = input("Enter a paragraph: ")

text = text.lower()

tokens = word_tokenize(text)

tokens = [word for word in tokens if word not in string.punctuation]

stop_words = set(stopwords.words('english'))
filtered_words = [word for word in tokens if word not in stop_words]

ps = PorterStemmer()
stemmed_words = [ps.stem(word) for word in filtered_words]

frequency = Counter(filtered_words)

print("\nOriginal Tokens:")
print(tokens)

print("\nFiltered Words:")
print(filtered_words)

print("\nStemmed Words:")
print(stemmed_words)

print("\nWord Frequency:")
for word, count in frequency.items():
    print(word, ":", count)

'''
Output:
Enter a paragraph: NLP helps computers understand human language and process text efficiently

Original Tokens:
['nlp', 'helps', 'computers', 'understand', 'human', 'language', 'and', 'process', 'text', 'efficiently']

Filtered Words:
['nlp', 'helps', 'computers', 'understand', 'human', 'language', 'process', 'text', 'efficiently']

Stemmed Words:
['nlp', 'help', 'comput', 'understand', 'human', 'languag', 'process', 'text', 'effici']

Word Frequency:
nlp : 1
helps : 1
computers : 1
understand : 1
human : 1
language : 1
process : 1
text : 1
efficiently : 1
'''
