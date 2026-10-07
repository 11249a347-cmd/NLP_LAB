import nltk
from nltk.tokenize import word_tokenize

sentence = input("Enter a sentence: ")

tokens = word_tokenize(sentence)
tagged_words = nltk.pos_tag(tokens)

grammar = r"""
           NP: {<DT>?<JJ>*<NN.*>+} 
           VP:{<VB.*><DT>?<JJ>*<NN.*>+}
           """

chunker = nltk.RegexpParser(grammar)

chunk_tree = chunker.parse(tagged_words)

print("\n POS Tagged Sentence")
print(tagged_words)

print("\n Chunk Tree")
print(chunk_tree)

chunk_tree.draw()

'''
output
Enter a sentence: The intelligent student completed the machine learning project.

 POS Tagged Sentence
[('The', 'DT'), ('intelligent', 'JJ'), ('student', 'NN'), ('completed', 'VBD'), ('the', 'DT'), ('machine', 'NN'), ('learning', 'NN'), ('project', 'NN'), ('.', '.')]

 Chunk Tree
(S
  (NP The/DT intelligent/JJ student/NN)
  completed/VBD
  (NP the/DT machine/NN learning/NN project/NN)
  ./.)
'''

