# %%
#Load formatted data and do NER

import pandas as pd
import spacy
from spacy import displacy
import csv

#Load data 
df = pd.read_csv('ENTER_PATH_TO_DATA.csv')

# Getting the pipeline of your model
NER = spacy.load("output/model-best") 
ner=NER.get_pipe("ner")

results = []


textData = df['Title']

for text in textData:
    text1 = NER(str(text))
    for word in text1.ents:
        results.append([str(word.text),str(word.label_)])
        
df1 = pd.DataFrame(results, columns=['Word', 'Cryptocurrency'])

df1.to_csv('ner-output-data.csv')