import nltk
from nltk.tokenize import word_tokenize

sentence = input("Enter a sentence: ")
tokens = word_tokenize(sentence)
tagged = nltk.pos_tag(tokens)

grammar = r"NP: {<DT>?<JJ>*<NN>+}"

chunk_parser = nltk.RegexpParser(grammar)

chunk_tree = chunk_parser.parse(tagged)
print(tagged)
print(chunk_tree)
chunk_tree.draw()
'''
Output
Enter a sentence: The intelligent student won the coding competition.
[('The', 'DT'), ('intelligent', 'JJ'), ('student', 'NN'), ('won', 'VBD'), ('the', 'DT'), ('coding', 'NN'), ('competition', 'NN'), ('.', '.')]
(S
  (NP The/DT intelligent/JJ student/NN)
  won/VBD
  (NP the/DT coding/NN competition/NN)
  ./.)

'''