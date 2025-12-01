from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import GridSearchCV

import pandas as pd


def make_naive_bayes_model(targets,df):
    vectorizer = TfidfVectorizer(ngram_range=(1, 2),max_df=0.9)
    df = pd.read_csv("_chat.csv",encoding="utf-16")
    df = df[df['authors'].isin(targets)]
    df = df[df['messages'].astype(str).str.split().str.len() >= 3]
    print(df['authors'].value_counts(normalize=True))
    X = vectorizer.fit_transform(df['messages']) 
    y = df['authors']


    # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=112, stratify=y)

    clf = MultinomialNB()

    param_grid = {'alpha': [0.01, 0.1, 0.5, 1.0, 1.5, 2.0]}
    
    # CV=5 faz o papel do K-Folds (5 dobras)
    grid_search = GridSearchCV(clf, param_grid, cv=5, scoring='accuracy', n_jobs=-1)
    grid_search.fit(X, y)

    print(f"Melhor Alpha encontrado: {grid_search.best_params_['alpha']}")
    print(f"Melhor Acurácia (Média Cruzada): {grid_search.best_score_:.2%}")

    # clf.fit(X_train, y_train)
    # print("Acurácia do modelo Naive Bayes:", clf.score(X_test, y_test))
    return grid_search.best_estimator_,vectorizer

