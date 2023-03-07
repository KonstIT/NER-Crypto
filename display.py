# %%
#Show identified objects in a text that have been recognised by your trained model

import spacy
from spacy import displacy

text = "EXAMPLE: BITCOIN MINER BITNILE RELOCATES 6,572 BITCOIN MINERS TO MICHIGAN"

#Enter Path to your trained model
nlp = spacy.load("output/model-best")
doc = nlp(text)
displacy.serve(doc, style="ent")
# %%
