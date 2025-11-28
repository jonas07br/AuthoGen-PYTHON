import numpy as np
import pandas as pd
import os
import re


from collections import defaultdict, Counter

def make_markov_model(cleaned_stories, n_gram=2):
    markov_model = {}
    for i in range(len(cleaned_stories)-n_gram-1):
        curr_state, next_state = "", ""
        for j in range(n_gram):
            curr_state += cleaned_stories[i+j] + " "
            next_state += cleaned_stories[i+j+n_gram] + " "
        curr_state = curr_state[:-1]
        next_state = next_state[:-1]
        if curr_state not in markov_model:
            markov_model[curr_state] = {}
            markov_model[curr_state][next_state] = 1
        else:
            if next_state in markov_model[curr_state]:
                markov_model[curr_state][next_state] += 1
            else:
                markov_model[curr_state][next_state] = 1
    
    # calculating transition probabilities
    for curr_state, transition in markov_model.items():
        total = sum(transition.values())
        for state, count in transition.items():
            markov_model[curr_state][state] = count/total
        
    return markov_model

def make_hybrid_markov_model(cleaned_stories, max_gram=3):
    markov_model = {}

    # Vamos iterar de 1 até max_gram (ou seja, aprende n=1 e n=2)
    for n in range(1, max_gram + 1):
        for i in range(len(cleaned_stories) - n):
            # Estado atual: pega 'n' palavras
            curr_state = " ".join(cleaned_stories[i:i+n])
            # Próximo estado: pega SEMPRE apenas a 1 próxima palavra
            next_state = cleaned_stories[i+n]

            if curr_state not in markov_model:
                markov_model[curr_state] = {}
                markov_model[curr_state][next_state] = 0 # Inicializa com 0
            
            if next_state not in markov_model[curr_state]:
                markov_model[curr_state][next_state] = 0
            
            markov_model[curr_state][next_state] += 1

    # Cálculo de probabilidades
    for curr_state, transition in markov_model.items():
        total = sum(transition.values())
        for state, count in transition.items():
            markov_model[curr_state][state] = count / total
            
    return markov_model
