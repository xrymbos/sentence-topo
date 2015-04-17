#!/usr/bin/python
import nltk
from nltk.stem.snowball import SnowballStemmer
import string

ONLY_CAPITALS = True

stemmer = SnowballStemmer("english")

FILE = "alice.txt"

def stems_for_sentence(sentence):
    nopunct = sentence.translate(string.maketrans("",""), string.punctuation).lower()
    stems = [stemmer.stem(word) for word in nopunct.split(" ")]
    return set(stems)

def starts_with_capital(sentence):
    if(len(sentence) == 0):
        return False
    stripped = sentence.translate(string.maketrans("",""), string.punctuation)
    return stripped[0] != stripped[0].lower()
   

sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')

raw_text = open(FILE, "r").read()
raw_text = raw_text.decode('latin-1').encode("utf-8")
raw_text = raw_text.replace("\r\n", " ")
sentences = sent_detector.tokenize(raw_text.strip())
if (ONLY_CAPITALS):
    sentences = [s for s in sentences if starts_with_capital(s)]

sentence_stems = [stems_for_sentence(s) for s in sentences]
added = [False for s in sentences]
#print(sentence_stems)

known_stems = set()
num = 0
while (True):
    best = -1
    best_index = -1 
    for index, stem_set in enumerate(sentence_stems):
        if (added[index]):
            continue
        new_stems = len(stem_set.difference(known_stems))
        if (best == -1 or new_stems < best):
            best = new_stems
            best_index = index
    if (best == -1):
        break
    added[best_index] = True
    known_stems = known_stems.union(sentence_stems[best_index])
    num = num + 1
    print("words known: {} this delta: {} num sentences: {}".format(len(known_stems), best, num))
    print(sentences[best_index] + "\n")

