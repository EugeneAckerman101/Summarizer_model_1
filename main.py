#import models
import spacy
import pytextrank
import git

git.refresh('/path/to/git')

#in terminal run: python -m spacy download en_core_web_lg
# {for large model, for small model en_core_web_sm}

#define spaCy pipeline

nlp = spacy.load("en_core_web_lg")

#modify pipeline to include TextRank algorythm

nlp.add_pipe("textrank")

with open("text.txt", "r") as text:
    example_text = text.read()
    print(example_text)



