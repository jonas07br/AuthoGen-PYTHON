import pandas as pd

from helpers import markov_chain_model, phrase_generator, naive_bayes_model, selecionar_autores, utils
    
gplaysDf = pd.read_csv("data/_chat.csv",encoding="utf-16")
authors = gplaysDf["authors"].value_counts(normalize=True).head(20).keys().tolist()

targets = selecionar_autores.selecionar_autores_interativo(authors)

if not targets:
    print("Nenhum autor selecionado. Encerrando...")
    exit()

markov_models = {}
for target in targets:
    cleaned_mgs = utils.process_df_msgs(gplaysDf,target,8)
    markov_models[target] = markov_chain_model.make_hybrid_markov_model(cleaned_mgs,max_gram=3,target=target)
    print(f"Modelo Markov para {target} criado.")

nbModel,vectorizer = naive_bayes_model.make_naive_bayes_model(targets,gplaysDf,"data/_chat.csv",minLength=6)
print("Modelo Naive Bayes criado.")
while True:
    user_input = input("\nDigite uma frase: ")
    user_input_vectorized = vectorizer.transform([user_input])
    predicted_author = nbModel.predict(user_input_vectorized)[0]
    print(f"Autor previsto: {predicted_author}")
    print("Frase gerada pelo modelo Markov:")
    print(phrase_generator.generate_hybrid_story(markov_models[predicted_author],limit=10))
