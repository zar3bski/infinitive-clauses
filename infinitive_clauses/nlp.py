import spacy
import os
import pickle

nlp = spacy.load("en_core_web_trf")

if os.path.exists("{}/infinitive_clauses/__pycache__/64843-0.pickle".format(os.getcwd())):
    parsed = pickle.load(open("{}/infinitive_clauses/__pycache__/64843-0.pickle".format(os.getcwd()),"rb"))
else:
    with open("{}/tests/texts/64843-0.txt".format(os.getcwd())) as text: 
        parsed = nlp(text.read()[100:78000])
        pickle.dump(parsed, open("{}/infinitive_clauses/__pycache__/64843-0.pickle".format(os.getcwd()),"wb"))


print(dir(parsed))

#print("Noun phrases:", [chunk.text for chunk in parsed if chunk.pos_ == "VERB"])

print("First sentences: ", [sentence for sentence in parsed.sents][47:67])
