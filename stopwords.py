from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
input_text = "I love swimming in river, but I was shocked to see the waves"
stopwords = set(stopwords.words("english"))
words = word_tokenize(input_text)
filtered_sentence = []
for w in words:
    if w not in stopwords:
        filtered_sentence.append(w)
print(filtered_sentence)
