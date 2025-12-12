# AuthoGen (Python)

**Disciplina:** Introdução à Inteligência Artificial  
**Semestre:** 2025.2  
**Professor:** [Andre Luis Fonseca Faustino]  
**Turma:** [T04]

## Integrantes do Grupo
- Jonas Rafael Silva Cavalcanti - 20230054378
- Matheus Gabriel Souto de Lira Freitas - 20230054930
- Gabriel Guilherme Carvalho Viana - 20230042250 

**Descrição do Projeto**
- **Resumo:** Repositório com ferramentas para converter chats, treinar modelos de autoria (Naive Bayes) e gerar frases/trechos com modelos de Markov híbridos. O objetivo é analisar conversas (chat logs) e gerar frases no estilo dos participantes identificados.
- **Principais componentes:** processamento/conversão de chat (`chat_conversor.py`), pré-processamento (`utils.py`), modelos de Markov (`markov_chain_model.py`), classificador Naive Bayes (`naive_bayes_model.py`) e gerador de frases (`phrase_generator.py`). Há também um `main.py` que demonstra um fluxo interativo (prever autor e gerar frase).

**Dependências principais (detectadas no código)**
- `pandas`, `numpy`, `nltk`, `demoji`, `scikit-learn`

## Guia de Instalação e Execução

**1. Pré-requisitos**
- Clone o repositório
- Instale o Python 3.8+.
- Recomendo criar um ambiente virtual antes de instalar dependências.

```bash
git clone https://github.com/jonas07br/AuthoGen-PYTHON.git
cd AuthoGen-PYTHON
# macOS / zsh
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

# Instalação manual
pip install pandas numpy nltk demoji scikit-learn
```

**2. Baixar dados do NLTK (necessário para tokenização/stopwords)**

```bash
python -c "import nltk; nltk.download('punkt'); nltk.download('punkt_tab'); nltk.download('stopwords')"
```

**3. Preparar o dataset de chat**
- Se você tem um arquivo de chat em texto (ex.: `_chat01-12-2025.txt`), converta para CSV com a função do módulo `chat_conversor`.
- Existe um arquivo com conversas simuladas para testes simples ( `chat-fake.csv`)

```bash
python -c "from helpers import chat_conversor; chat_conversor.convertChatToCsv('data/_chat.txt')"
# Isso gera `_chat01-12-2025.csv` (encoding UTF-16) usado por `main.py`.
```

**4. Executar o fluxo principal (exemplo)**
- O `main.py` carrega um CSV de chat, cria modelos Markov por autor e treina um Naive Bayes para prever autores.

```bash
python main.py
```

Durante a execução interativa, digite frases para o classificador prever o autor e para o gerador Markov produzir uma frase no estilo do autor previsto.

## Estrutura de arquivos (resumo)
- `chat_conversor.py`: converte chat .txt em .csv
- `utils.py`: pré-processamento e funções utilitárias (usa NLTK)
- `markov_chain_model.py`: construção de modelos Markov híbridos
- `naive_bayes_model.py`: treino e validação do classificador
- `phrase_generator.py`: geração de frases a partir dos modelos
- `main.py`: exemplo de execução / fluxo interativo
- modelos JSON: `modelo_markov_*.json` — exemplos de modelos salvos

## Referências
- Ferramentas e libs usadas: `pandas`, `numpy`, `nltk`, `scikit-learn`, `demoji`.
