import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk

def clean_txt(txt):
    cleaned_txt = []
    for line in txt:
        line = line.lower()
        line = re.sub(r"[,.\"\'!@#$%^&*(){}?/;`~:<>+=-\\]", "", line)
        tokens = word_tokenize(line)
        words = [word for word in tokens if word.isalpha()]
        cleaned_txt+=words
    return cleaned_txt

def process_df_msgs(dataFrame,author:str,minMsgLength=1):
    authorFilter = dataFrame['authors'] == author
    authorMsgs = dataFrame.loc[authorFilter,'messages']

    filter = lambda x: len(str(x).split()) > minMsgLength

    authorMsgs_filtered = authorMsgs[authorMsgs.apply(filter)]

    return clean_txt(authorMsgs_filtered.tolist())

def show_transition_info(transition,state:str):
    print(len(transition),"-Transicoes para o estado:",state)
    for option in transition:
        print(option)
