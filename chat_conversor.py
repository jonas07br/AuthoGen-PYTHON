import pandas as pd
import re
import demoji
import model
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
        "this message was deleted"
    ]
    
    if any(term in message for term in ignored_terms):
        return True

    if not message.startswith("["):
        pass 

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
    basicList = parse_file(filePath)
    df['authors'] = basicList[0]
    df['messages'] = basicList[1]

    #removendo mencoes
    df['messages'] = df['messages'].str.replace(r'@\d+', '', regex=True)
    newFilePath = filePath.replace(".txt","")+".csv"
    df.to_csv(newFilePath,encoding="utf-16")

