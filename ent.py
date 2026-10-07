import spacy
nlp = spacy.load("en_core_web_sm")
text = input("Enter a sentence: ")
doc = nlp(text)
print("\nNamed Entities")
print("-" * 40)

for ent in doc.ents:
    print(f"Entity: {ent.text}")
    print(f"Label: {ent.label_}")
    print("-" * 40)
'''
Output:
Enter a sentence: Modi is the prime minister. Sundar Picchai is the CEO of Google. Microsoft is dream company

Named Entities
----------------------------------------
Entity: Sundar Picchai
Label: PERSON
----------------------------------------
Entity: Google
Label: ORG
----------------------------------------
Entity: Microsoft
Label: ORG
----------------------------------------
'''
