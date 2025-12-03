import chat_conversor
import pandas as pd
import utils
import markov_chain_model
import phrase_generator
import naive_bayes_model



# chat_conversor.convertChatToCsv('_chat.txt')

# def showPhrase(start:str):
#     print(phrase_generator.generate_hybrid_story(hybrid_markov,limit=10,start=start))
    
gplaysDf = pd.read_csv("_chat.csv",encoding="utf-16")

targets = ['Spot','Antony']
markov_models = {}
for target in targets:
    cleaned_mgs = utils.process_df_msgs(gplaysDf,target,8)
    markov_models[target] = markov_chain_model.make_hybrid_markov_model(cleaned_mgs,max_gram=3,target=target)
    print(f"Modelo Markov para {target} criado.")

nbModel,vectorizer = naive_bayes_model.make_naive_bayes_model(targets,gplaysDf,minLength=6)
print("Modelo Naive Bayes criado.")
while True:
    user_input = input("Digite uma frase: ")
    user_input_vectorized = vectorizer.transform([user_input])
    predicted_author = nbModel.predict(user_input_vectorized)[0]
    print(f"Autor previsto: {predicted_author}")
    print("Frase gerada pelo modelo Markov:")
    print(phrase_generator.generate_hybrid_story(markov_models[predicted_author],limit=10))
