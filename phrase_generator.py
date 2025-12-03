import random
import utils

def generate_story(markov_model, limit=100, start='my god', top_k=5):
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


def generate_hybrid_story(markov_model, limit=100, start='my god', top_k=10):
    start = random.choice(list(markov_model.keys()))
    story_words = start.split() # Transforma a string inicial em lista
    n = 0
    last_transition_size = 0
    while n < limit:
        last_three_words = " ".join(story_words[-3:])
        last_two_words = " ".join(story_words[-2:])
        last_one_word = story_words[-1]

        transitions = None
        # LÓGICA DE BACKOFF:
        # print("iteracao:",n)

        if last_three_words in markov_model and last_transition_size!=1:
            transitions = markov_model[last_three_words]
            # utils.show_transition_info(transitions,last_three_words)
  
        # 1. Tenta achar a chave de 2 palavras
        elif last_two_words in markov_model:
            transitions = markov_model[last_two_words]
            # utils.show_transition_info(transitions,last_two_words)

        # 2. Se falhar, tenta achar a chave de 1 palavra
        elif last_one_word in markov_model:
            transitions = markov_model[last_one_word]
            # utils.show_transition_info(transitions,last_one_word)

        # 3. Se falhar tudo, escolhe uma palavra aleatória do modelo para 'destravar'
        else:
            # print("chegou num final sem sentido")
            transitions = markov_model[random.choice(list(markov_model.keys()))]

        last_transition_size = len(transitions)
        if(limit - n == 1 and last_transition_size>3):
            n-=1
        # --- APLICA O SEU TOP-K ---
        sorted_transitions = sorted(transitions.items(), key=lambda item: item[1], reverse=True)
        top_n_transitions = sorted_transitions[:top_k]
        
        options = [item[0] for item in top_n_transitions]
        weights = [item[1] for item in top_n_transitions]
        
        next_word = random.choices(options, weights=weights)[0]
        
        story_words.append(next_word)
        n += 1
        
    return " ".join(story_words)
