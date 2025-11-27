import chat_conversor
import pandas as pd
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk
import model
import random

import random

def generate_story(markov_model, limit=100, start='my god'):
    n = 0
    curr_state = start
    next_state = None
    story = ""
    story+=curr_state+" "
    while n<limit:
        next_state = random.choices(list(markov_model[curr_state].keys()),
                                    list(markov_model[curr_state].values()))
        
        curr_state = next_state[0]
        story+=curr_state+" "
        n+=1
    return story

def clean_txt(txt):
    cleaned_txt = []
    for line in txt:
        line = line.lower()
        line = re.sub(r"[,.\"\'!@#$%^&*(){}?/;`~:<>+=-\\]", "", line)
        tokens = word_tokenize(line)
        words = [word for word in tokens if word.isalpha()]
        cleaned_txt+=words
    return cleaned_txt

# chat_conversor.convertChatToCsv('_chat.txt')

gplaysDf = pd.read_csv("_chat.csv",encoding="utf-16")

zangadoFilter = gplaysDf['authors'] == 'gabriel bocão'

zangadoMsgs = gplaysDf.loc[zangadoFilter,'messages']

cleaned_txt = clean_txt(zangadoMsgs.tolist())

markov_model = model.make_markov_model(cleaned_txt,n_gram=1)

for i in range(20):
    print(str(i)+". ", generate_story(markov_model, start="eu quero", limit=10))

