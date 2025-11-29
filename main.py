import chat_conversor
import pandas as pd
import utils
import model
import phrase_generator
# chat_conversor.convertChatToCsv('_chat.txt')

def showPhrase(start:str):
    print(phrase_generator.generate_hybrid_story(hybrid_markov,limit=10,start=start))
    
gplaysDf = pd.read_csv("_chat.csv",encoding="utf-16")

cleaned_mgs = utils.process_df_msgs(gplaysDf,'gabriel bocão',8)

# hybrid_markov = model.make_hybrid_markov_model()

hybrid_markov = model.load_model_from_json('modelo_markov.json')

# for i in range(1):
#     print(phrase_generator.generate_hybrid_story(hybrid_markov,limit=10,start="eu quero ver esse"))
while True:
    start = input("Insira o texto: ")
    showPhrase(start)
    