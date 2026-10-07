from nltk.stem import WordNetLemmatizer
Lemmatizer = WordNetLemmatizer()
print(Lemmatizer.lemmatize("Cats"))
print(Lemmatizer.lemmatize("Cacti"))
print(Lemmatizer.lemmatize("geese"))
print(Lemmatizer.lemmatize("rocks"))
print(Lemmatizer.lemmatize("python"))
print(Lemmatizer.lemmatize("better", pos = "a"))
print(Lemmatizer.lemmatize("happy", pos = "a"))