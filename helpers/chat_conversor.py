import pandas as pd
import re
import demoji
from typing import List

df = pd.DataFrame()

def is_useless_message(message: str) -> bool:
    if not isinstance(message, str):
        return True
        
    ignored_terms = [
        "Waiting for this message",
        "image omitted",
        "sticker omitted",
        "audio omitted",
        "video omitted",
        "You added",
        "left",
        "changed the group name to",
        "security code changed",
        "Contact card omitted",
        "GIF omitted",
        "document omitted",
        "video note omitted",
        "removed",
        "changed this group's icon",
        "https",
        "this message was deleted",
        "This message",
        "You deleted this message",
        "changed this group's settings",
        "joined using this group's invite link",
        "VINIMUNEWS",
        "JRMUNEWS"
    ]
    
    if any(term in message for term in ignored_terms):
        return True

    if not message.startswith("["):
        return True 

    return False

def detectAuthor(message:str):
    dateIndex = message.find(']')
    doubleDotIndex = message.find(": ")
    return message[dateIndex+2:doubleDotIndex]

def formatMessage(message:str,author:str):
    startMessageIndex = message.find(author+":")
    endMessageIndex = message.find("'\n'")
    return message[startMessageIndex+len(author)+1:endMessageIndex]

def removeEmojis(message:str):
    return demoji.replace(message,"")

def parse_file(text_file):
    messages = []
    authors = []
    
    with open(text_file,encoding='utf8') as f:
        for a in f:
            line = f.readline()
            if(not is_useless_message(line)):
                line = re.sub(r'[\u202a-\u202e\u200e\u200f]', '', line)
                line = removeEmojis(line)
                authors.append(detectAuthor(line))
                messages.append(formatMessage(line,authors[-1]))
        return [authors,messages]


def convertChatToCsv(filePath:str):
    print("Convertendo chat para CSV...")
    basicList = parse_file(filePath)
    df['authors'] = basicList[0]
    df['messages'] = basicList[1]

    #removendo mencoes
    df['messages'] = df['messages'].str.replace(r'@\d+', '', regex=True)
    newFilePath = filePath.replace(".txt","")+".csv"
    df.to_csv(newFilePath,encoding="utf-16")
    print(f"Chat convertido e salvo em {newFilePath}")

def get_contacts_from_csv(csv_path: str) -> List[str]:
    encodings = ['utf-16', 'utf-8', 'latin1']
    last_exception = None
    for enc in encodings:
        try:
            df_local = pd.read_csv(csv_path, encoding=enc)
            break
        except Exception as e:
            last_exception = e
    else:
        raise last_exception

    if 'authors' not in df_local.columns:
        possible = [c for c in df_local.columns if 'author' in c.lower() or 'authors' in c.lower() or 'autor' in c.lower()]
        if possible:
            authors_series = df_local[possible[0]]
        else:
            return []

    else:
        authors_series = df_local['authors']

    authors_series = authors_series.fillna('').astype(str).str.strip()

    # preservar ordem de primeira aparição
    seen = set()
    unique_authors = []
    for name in authors_series:
        if name == '':
            continue
        if name not in seen:
            seen.add(name)
            unique_authors.append(name)

    return unique_authors

