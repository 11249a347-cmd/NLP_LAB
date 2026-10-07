import nltk
def generate_words(word):


    if word.endswith('y'):
        plural = word[:-1]+"ies"
    elif word.endswith(('s', 'x', 'z', 'ch', 'sh')):
        plural = word + "es"
    else:
        plural = word + "s"

    if word.endswith('e') and not word.endswith('ee'):
        ing = word[:-1] + "sing"
    else:
        ing = word + "ing"

    if word.endswith('e'):
        past = word + "d"
    else:
        past = word + "ed"

    print("\n Generated Word Forms")
    print(" =======================")
    print("Root Word: ", word)
    print("Plural form : ", plural)
    print("Present Participle: ", ing)
    print("Past Tense: ", past)
word = input("Enter a root word: ").lower()
generate_words(word)

