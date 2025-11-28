import chat_conversor
import pandas as pd
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk
import model
import random

import random

import random

def generate_story(markov_model, limit=100, start='my god', top_k=10):
    n = 0
    curr_state = start
    story = curr_state + " "
    
    while n < limit:
        # Verifica se o estado atual existe no modelo (evita erros se chegar num beco sem saída)
        if curr_state not in markov_model:
            break
            
        transitions = markov_model[curr_state]
        
        # 1. ORDENAR: Transforma o dicionário em lista de tuplas e ordena pelo valor (probabilidade)
        # Ex: [('palavra A', 0.5), ('palavra B', 0.2), ...]
        sorted_transitions = sorted(transitions.items(), key=lambda item: item[1], reverse=True)
        
        # 2. FILTRAR (Top-K): Pega apenas os primeiros 'top_k' elementos (ex: 10)
        # O slice [:top_k] funciona mesmo se a lista tiver menos que 10 itens
        top_n_transitions = sorted_transitions[:top_k]
        print("Melhores estados para",curr_state)
        print(top_n_transitions)
        print("\n")
        # 3. SEPARAR: Separa em duas listas para o random.choices
        options = [item[0] for item in top_n_transitions]
        weights = [item[1] for item in top_n_transitions]
        
        # 4. ESCOLHER: Sorteia baseado nos pesos (pesos maiores têm mais chance)
        # random.choices retorna uma lista, pegamos o primeiro elemento [0]
        next_state_val = random.choices(options, weights=weights)[0]
        
        curr_state = next_state_val
        story += curr_state + " "
        n += 1
        
    return story

def generate_hybrid_story(markov_model, limit=100, start='my god', top_k=1):
    story_words = start.split() # Transforma a string inicial em lista
    n = 0
    
    while n < limit:
        last_tree_words = " ".join(story_words[-3:])
        # Tenta pegar as últimas 2 palavras (Contexto Rico)
        last_two_words = " ".join(story_words[-2:])
        # Tenta pegar a última 1 palavra (Contexto Simples/Backoff)
        last_one_word = story_words[-1]

        transitions = None
        # LÓGICA DE BACKOFF:
        print("iteracao:",n)
        print(last_tree_words)
        print(last_two_words)
        print(last_one_word)
        print("\n")
        if last_tree_words in markov_model:
            if(len(markov_model[last_tree_words])>1):
                transitions = markov_model[last_tree_words]
                print("3-Transicoes para:",last_tree_words)
                print(len(transitions))
                print("\n")
        # 1. Tenta achar a chave de 2 palavras
        if last_two_words in markov_model and len(last_tree_words.split(" "))==2 and transitions == None:
            if(len(markov_model[last_two_words])>1):
                transitions = markov_model[last_two_words]
                print("2-Transicoes para:",last_two_words)
                print(len(transitions))
                print("\n")
        # 2. Se falhar, tenta achar a chave de 1 palavra
        if last_one_word in markov_model and transitions == None:
            transitions = markov_model[last_one_word]
            print("1-Transicoes para:",last_one_word)
            print(len(transitions))
            print("\n")
        # 3. Se falhar tudo, escolhe uma palavra aleatória do modelo para 'destravar'
        if transitions == None:
            print("chegou num final sem sentido")
            transitions = markov_model[random.choice(list(markov_model.keys()))]

        print(transitions.keys())
        
        # --- APLICA O SEU TOP-K ---
        sorted_transitions = sorted(transitions.items(), key=lambda item: item[1], reverse=True)
        top_n_transitions = sorted_transitions[:top_k]
        
        options = [item[0] for item in top_n_transitions]
        weights = [item[1] for item in top_n_transitions]
        
        next_word = random.choices(options, weights=weights)[0]
        
        story_words.append(next_word)
        n += 1
        
    return " ".join(story_words)

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

zangadoFilter = gplaysDf['authors'] == 'Laércio Morais'
zangadoMsgs = gplaysDf.loc[zangadoFilter,'messages']

criterio = lambda x: len(str(x).split()) > 1

zangadoMsgs_filtradas = zangadoMsgs[zangadoMsgs.apply(criterio)]

cleaned_txt = clean_txt(zangadoMsgs_filtradas.tolist())

# markov_model = model.make_markov_model(cleaned_txt,n_gram=1)

# for i in range(20):
#     print(str(i)+". ", generate_story(markov_model, start="eu", limit=8))
# print(generate_story(markov_model,start="eu",limit=8))

hybrid_markov = model.make_hybrid_markov_model(cleaned_txt)

for i in range(1):
    print(generate_hybrid_story(hybrid_markov,limit=15,start="eu"))
