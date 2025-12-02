# IA-GPLAYS - Gerador de Texto com IA

## 📋 Resumo

Sistema híbrido de geração de texto que combina **Cadeias de Markov** e **Naive Bayes** para identificar autores e gerar frases no estilo de diferentes pessoas a partir de conversas do WhatsApp.

## 🎯 Funcionalidades

- **Identificação de Autores**: Classifica frases usando Naive Bayes com TF-IDF
- **Geração de Texto**: Cria frases no estilo de autores específicos usando Cadeias de Markov híbridas (n-gramas variáveis)
- **Processamento de Chat**: Converte conversas do WhatsApp em datasets estruturados

## 🚀 Como Usar

### 1. Instalar Dependências
```bash
pip install -r requirements.txt
```

### 2. Configurar NLTK
```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

### 3. Preparar Dados
- Exporte uma conversa do WhatsApp como `_chat.txt`
- Execute a conversão (se necessário):
```python
import chat_conversor
chat_conversor.convertChatToCsv('_chat.txt')
```

### 4. Executar
```bash
python main.py
```

## 🔧 Estrutura do Projeto

- `main.py` - Ponto de entrada principal
- `naive_bayes_model.py` - Classificador de autores
- `markov_chain_model.py` - Modelo de geração de texto
- `phrase_generator.py` - Gerador de frases com backoff híbrido
- `chat_conversor.py` - Conversor WhatsApp → CSV
- `utils.py` - Funções de limpeza e processamento de texto

## 📊 Fluxo de Funcionamento

1. Usuário digita uma frase
2. Naive Bayes identifica o autor mais provável
3. Cadeia de Markov do autor gera uma resposta no seu estilo

## 🧪 Modelos

- **Naive Bayes**: TF-IDF com GridSearch (alpha otimizado)
- **Markov Híbrido**: Suporta n-gramas de 1 a 3 palavras com backoff inteligente

---

**Autores**: Projeto desenvolvido para análise de IA com dados do WhatsApp
